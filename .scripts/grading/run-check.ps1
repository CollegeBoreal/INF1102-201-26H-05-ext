#!/usr/bin/env pwsh
param(
    [switch]$Quiet
)

$dirs = @(
    "3.IaC",
    "4.CRON-TASK",
    "5.BATCH",
    "6.PWSH",
    "7.REGEX",
    "8.Project",
    "9.Ansible"
)

foreach ($dir in $dirs) {
    Write-Output "=> $dir"

    Push-Location $dir
    try {
        if ($Quiet) {
            ./.scripts/grading/push_grades.ps1 *> $null
        }
        else {
            ./.scripts/grading/push_grades.ps1
        }
    }
    finally {
        Pop-Location
    }
}