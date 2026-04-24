# =====================================================================
# CONFIGURATION
# =====================================================================
# Static IDs and flags used throughout participation grading
# =====================================================================

# LMS assignment ID where participation grades will be submitted
$LMSAssignmentID = 30

# Enables verbose/debug output when set to $true
$DEBUG = $false

# Explicit emoji → rubric level mapping for DB execution criterion
# (Used when the emoji represents more than pass/fail)
$EmojiToScore = @{
    ":grey_question:" = 339
    ":bangbang:" = 340
    ":rocket:" = 341
    ":receipt:" = 345
    ":writing_hand:" = 343
    ":zero:" = 346
    ":one:" = 347
    ":asterisk:" = 348
    ":boom:" = 349
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

            # Column index reference (0 is empty due to leading pipe):
            # 1 = Row index
            # 2 = Boréal ID link
            # 5 = abacus emoji

            if ($DEBUG) { Write-Output $cols. }

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
            $levels = @(334, 335, 336)  # fail, silver, gold
            $readScore = Get-RubricLevelIdFromReadmeEmoji `
                -Emoji $readEmoji `
                -Levels $levels

            # ---------------------------------
            # Images folder presence (pass/fail)
            # ---------------------------------
            $imgEmoji = ($cols[4]).Trim()
            $imgScore = Get-RubricLevelIdFromEmoji `
                -Emoji $imgEmoji `
                -FailLevelId 337 `
                -PassLevelId 338

            # If README.md exceeds expectations,
            # images folder is implicitly considered present
            if ($readScore -gt 336) {
                $imgScore = 338
            }

            # ---------------------------------
            # analyse.py execution
            # ---------------------------------
            $ioEmoji = ($cols[5]).Trim()
            $ioScore = $EmojiToScore[$ioEmoji] ?? 339

            # ---------------------------------
            # RAPPORT presence
            # ---------------------------------
            $receiptScore =
                if ($cols[6] -match '(:[^:]+:)') {
                    $EmojiToScore[$matches[1]]
                }
            $receiptScore = $receiptScore ?? 344

            
            # ---------------------------------
            # Signature presence
            # ---------------------------------
            $sgnScore =
             if ($cols[7] -match '(:[^:]+:)') {
                $EmojiToScore[$matches[1]]
            }
            $sgnScore = $sgnScore ?? 342

            # ---------------------------------
            # Figure presence
            # ---------------------------------
             if ($cols[8] -match '(:[^:]+:)') {
                $figEmoji = $matches[1]
                if ($figEmoji -notmatch ':zero:|:one:') {
                    $figEmoji = ':asterisk:'
                }
                $figScore = $EmojiToScore[$figEmoji]
             }

            # ---------------------------------
            # analyse.ps1 presence
            # ---------------------------------
            if ($cols[9] -match '(:[^:]+:)') {
                $etuEmoji = $matches[1]
                $etuScore = Get-RubricLevelIdFromEmoji `
                    -Emoji $etuEmoji `
                    -FailLevelId 349 `
                    -PassLevelId 350
            }

            # ---------------------------------
            # rapport.txt presence
            # ---------------------------------
            if ($cols[10] -match '(:[^:]+:)') {
                $resEmoji = $matches[1]
                $resScore = Get-RubricLevelIdFromEmoji `
                    -Emoji $resEmoji `
                    -FailLevelId 351 `
                    -PassLevelId 352
            }

            # Debug trace for validation / troubleshooting
            if ($DEBUG) {
                Write-Output $borealId
                    , $readEmoji, $readScore
                    , $imgEmoji, $imgScore
                    , $ioEmoji, $ioScore
                    , $receiptEmoji, $receiptScore
                    , $etuEmoji, $etuScore
                    , $resEmoji, $resScore
            }

            # Accumulate normalized grading entry
            $results += [PSCustomObject]@{
                borealId  = $borealId
                readme    = $readScore
                image     = $imgScore
                io        = $ioScore
                rapport   = $receiptScore
                signature = $sgnScore
                figure    = $figScore
                etudiants = $etuScore
                resultat  = $resScore
            }
        }
    }

    return $results
}

# =====================================================================
# RUBRIC OBJECT BUILDER
# =====================================================================

function New-LMSRubricFromEntry {
    <#
        Converts a normalized participation entry into
        an LMS-compatible rubric payload.

        Designed to prevent invalid submissions that
        could crash Moodle grading APIs.
    #>
    param (
        [Parameter(Mandatory)]
        [object]$Entry
    )

    # Required grading components
    $requiredFields = @(
         "readme"
        , "image"
        , "io"
        , "rapport"
        , "signature"
        , "figure"
        , "etudiants"
        , "resultat"
    )

    # Validate entry completeness
    foreach ($field in $requiredFields) {
        if (-not $Entry.PSObject.Properties.Name -contains $field) {
            throw "Missing field '$field' in entry"
        }
    }

    # Construct rubric payload in LMS criterion order
    $rubric = @(
        @{ criterionid = 145;  levelid = $Entry.readme;    remark = "Quantité README.md " }
        @{ criterionid = 146;  levelid = $Entry.image;     remark = "présence répertoire images " }
        @{ criterionid = 147;  levelid = $Entry.io;        remark = "Éxécution de IO.py" }
        @{ criterionid = 149;  levelid = $Entry.rapport;   remark = "Présence Rapport Jupyter Notebook" }
        @{ criterionid = 148;  levelid = $Entry.signature; remark = "Présence Signature" }
        @{ criterionid = 150; levelid = $Entry.figure;     remark = "Nombre de Figures dans le rapport" }
        @{ criterionid = 151; levelid = $Entry.etudiants;  remark = "Présence analyse.ps1" }
        @{ criterionid = 152; levelid = $Entry.resultat;   remark = "Présence rapport.txt" }
    )

    # Safety check: ensure all level IDs exist
    # (Null level IDs can cause Moodle submission failures)
    foreach ($r in $rubric) {
        if (-not $r.levelid) {
            throw "Invalid levelid for criterion $($r.criterionid)"
        }
    }

    return $rubric
}