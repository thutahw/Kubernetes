curl -LO https://dl.k8s.io/release/v1.22.0/bin/windows/amd64/kubectl.exe

SET mypath=%~dp0

set PATH=%PATH%;%mypath%kubectl.exe