# =====================================================================
# CONFIGURATION
# =====================================================================
# Static IDs and flags used throughout participation grading
# =====================================================================

# LMS assignment ID where participation grades will be submitted
$LMSAssignmentID = 25

# Enables verbose/debug output when set to $true
$DEBUG = $false

# Explicit emoji → rubric level mapping for DB execution criterion
# (Used when the emoji represents more than pass/fail)
$EmojiToScore = @{
    ":red_circle:" = 292
    ":green_circle:" = 293
    ":boom:" = 294
    ":link:" = 295
}

# =====================================================================
# PARTICIPATION EXTRACTION FROM README.md
# =====================================================================

function Get-ParticipationGrades {
    <#
        Parses a Markdown table from a README.md file and converts
        emoji-based participation indicators into LMS rubric level IDs.

        Each valid row produces one grading entry keyed by Boréal ID.
    #>
    param (
        [Parameter(Mandatory)]
        [string]$Path
    )

    # Read README.md line-by-line
    $lines = Get-Content $Path
    $results = @()

    foreach ($line in $lines) {

        # Only process Markdown table rows starting with:
        # | <number> |
        if ($line -match '^\|\s*\d+\s*\|') {

            # Split on column separators
            $cols = $line -split '\|'

            # Columns (0 is empty):
            # 1 = index
            # 2 = Boréal ID link column
            # 3-4 = others

            # Extract Boréal ID (expected format: [300000000])
            if ($cols[2] -match '\[(\d{9})\]') {
                $borealId = $matches[1]
            } else {
                # Skip malformed rows
                continue
            }

            # ---------------------------------
            # README.md quantity (fail/silver/gold)
            # ---------------------------------
            $readEmoji = ($cols[3]).Trim()
            $levels = @(285, 286, 287)  # fail, silver, gold
            $readScore = Get-RubricLevelIdFromReadmeEmoji `
                -Emoji $readEmoji `
                -Levels $levels

            # ---------------------------------
            # Images folder presence (pass/fail)
            # ---------------------------------
            $imgEmoji = ($cols[4]).Trim()
            $imgScore = Get-RubricLevelIdFromEmoji `
                -Emoji $imgEmoji `
                -FailLevelId 288 `
                -PassLevelId 289

            # If README.md exceeds expectations,
            # images folder is implicitly considered present
            if ($readScore -gt 287) {
                $imgScore = 289
            }

            $mainEmoji = ($cols[5]).Trim()
            $mainScore = Get-RubricLevelIdFromEmoji `
                -Emoji $mainEmoji `
                -FailLevelId 288 `
                -PassLevelId 289

            # ---------------------------------
            # VM execution
            # matches :green_circle: or :red_circle: 
            # if :x: of revert to null‑coalescing operator (??) default value
            # ---------------------------------
            if ($cols[6] -match '(:[^:]+:)') {
                $vmEmoji = $matches[1]
                $vmScore = $EmojiToScore[$vmEmoji]  ?? $EmojiToScore[':red_circle:']
            }

            # ---------------------------------
            # VM execution
            # matches :link: or :boom: 
            # if :x: of revert to null‑coalescing operator (??) default value
            # ---------------------------------
            if ($cols[7] -match '(:[^:]+:)') {
                $linkEmoji = $matches[1]
                $linkScore = $EmojiToScore[$linkEmoji] ?? $EmojiToScore[':boom:']
            }

            if ($DEBUG) {
                Write-Output $borealId
                    , $readEmoji, $readScore
                    , $imgEmoji, $imgScore
                    , $mainEmoji, $mainScore
                    , $vmScore, $vmEmoji
                    , $linkScore, $linkEmoji
            }

            $results += [PSCustomObject]@{
                borealId  = $borealId
                readme    = $readScore
                image     = $imgScore
                main      = $mainScore
                vm        = $vmScore
                link      = $linkScore
            }
        }
    }

    return $results
}

function New-LMSRubricFromEntry {
    param (
        [Parameter(Mandatory)]
        [object]$Entry
    )

    # Validate required fields exist
    $requiredFields = @(
         "readme"
        , "image"
        , "main"
        , "vm"
        , "link"
    )

    foreach ($field in $requiredFields) {
        if (-not $Entry.PSObject.Properties.Name -contains $field) {
            throw "Missing field '$field' in entry"
        }
    }

    # Build rubric
    $rubric = @(
        @{ criterionid = 123;  levelid = $Entry.readme;    remark = "Quantité README.md " }
        @{ criterionid = 124;  levelid = $Entry.image;     remark = "Présence répertoire images " }
        @{ criterionid = 125;  levelid = $Entry.main;      remark = "Présence code source" }
        @{ criterionid = 126;  levelid = $Entry.vm;        remark = "Présence de la VM" }
        @{ criterionid = 127;  levelid = $Entry.link;      remark = "Présence du la clé SSH Prof" }
    )

    # Validate level IDs (avoid Moodle crash)
    foreach ($r in $rubric) {
        if (-not $r.levelid) {
            throw "Invalid levelid for criterion $($r.criterionid)"
        }
    }

    return $rubric
}