$ServiceName = "NetworkObservabilityAgent"
Stop-Service $ServiceName -Force
sc.exe delete $ServiceName
Write-Host "Service '$ServiceName' uninstalled successfully."