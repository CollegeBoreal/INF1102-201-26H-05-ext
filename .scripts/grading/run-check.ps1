#!/usr/bin/env pwsh

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
        ./.scripts/grading/push_grades.ps1
    }
    finally {
        Pop-Location
    }
}
