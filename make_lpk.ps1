$dirname = Split-Path -Path $PWD.Path -Leaf
$zipname =  $dirname + ".zip"
$lpkname = $dirname + ".lpk"

# Write-Output $zipname
# Write-Output $lpkname

7z a $zipname ./scripts/ index.cfg index.xml "-x!*.lpk" "-x!*.zip" "-x!*.ps1" "-x!.git/" "-x!.gitignore"
Move-Item -Force $zipname $lpkname

# Pause
