# Nouveau fichier students.ps1
# Liste des étudiants A25 avec IDS et AVATARS correspondants

$STUDENTS = @(
"300135538|RedaYousfi|133056385"
)


# --------------------------------------
# Division des étudiants en 1 groupe
# --------------------------------------

$TOTAL = $STUDENTS.Count
$GROUP_SIZE = [Math]::Ceiling($TOTAL / 1)

$GROUP_1 = $STUDENTS[0..($GROUP_SIZE - 1)]
$GROUP_2 = $STUDENTS[($GROUP_SIZE)..($TOTAL - 1)]

# --------------------------------------
# Division des VMs en 2 groupes
# --------------------------------------

$SERVERS = @(
"10.7.237.224"
)

$SERVER_GROUP_1 = $SERVERS[0..($GROUP_SIZE - 1)]
$SERVER_GROUP_2 = $SERVERS[($GROUP_SIZE)..($TOTAL - 1)]

# --------------------------------------
# S21	https://10.7.237.19:8006	64	16	272	Virtual Environment 7.4-20
# S25	https://10.7.237.38:8006	64	16	272	Virtual Environment 7.4-20
# --------------------------------------

$PROXMOX_SERVERS = @(
"10.7.237.19"
"10.7.237.38"
)

$PROXMOX_GROUP_1 = $PROXMOX_SERVERS[0] 
$PROXMOX_GROUP_2 = $PROXMOX_SERVERS[1] 

# --------------------------------------
# pm_token_id     = "tofu@pve!opentofu"
# pm_token_secret = "4fa24fc3-bd8c-4916-ba6e-09xxxxxx3b00"
# --------------------------------------

$TOFU_SECRETS = @(
"f2097a3c-f9f0-4558-9a43-5cd0ae718abe"
"1cde2cfc-e100-47b9-9ee2-591ed83cfb8e"
)

$TOFU_SECRET_GROUP_1 = $TOFU_SECRETS[0] 
$TOFU_SECRET_GROUP_2 = $TOFU_SECRETS[1] 

$PK_PROF="b300098957@ramena"

## Cours Moodle
$LMS_COURSE=4
