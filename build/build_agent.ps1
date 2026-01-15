$ProjectRoot = Resolve-Path ".."
$ServiceDir  = "$ProjectRoot\service"
$OutputDir   = "$ProjectRoot\build\output"

pyinstaller `
  --onefile `
  --noconsole `
  --name agent `
  --distpath $OutputDir `
  --workpath "$OutputDir\work" `
  --specpath "$OutputDir\spec" `
  "$ServiceDir\agent_service.py"