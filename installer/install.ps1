$ServiceName = "NetworkObservabilityAgent"
$ExePath = "C:\Program Files\NetworkObservabilityAgent\agent.exe"

New-Service `
  -Name $ServiceName `
  -BinaryPathName "`"$ExePath`"" `
  -DisplayName "Network Observability Agent" `
  -StartupType Automatic

Start-Service $ServiceName
Write-Host "Service '$ServiceName' installed and started successfully."