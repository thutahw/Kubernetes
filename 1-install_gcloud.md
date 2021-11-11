# Windows
### 1. Open powershell
```shell
(New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")
& $env:Temp\GoogleCloudSDKInstaller.exe
```
## Installation
### 2. Set auth login
```shell
gcloud auth activate-service-account --key-file=ninja-van-experiments-4a88642b9759.json
```
### 3. Initialise gcloud
```shell
gcloud init
```
Please select these configurations
- 1
- kube-talk
- ninja-van-experiments
- 30

### 4. Install kubectl
Run install_kubectl.bat

# Mac
### 1. Open terminal
## 64 Bit
```bash
curl https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-353.0.0-darwin-x86_64.tar.gz --output google-cloud-sdk.tar.gz
```
## M1
```bash
curl https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-353.0.0-darwin-arm.tar.gz --output google-cloud-sdk.tar.gz
```

## Installation
### 2. Unzip file
```bash
tar -xf google-cloud-sdk.tar.gz
```
### 3. Install gcloud
```bash
./google-cloud-sdk/install.sh
```
### 4. Set auth login
```bash
gcloud auth activate-service-account --key-file=ninja-van-experiments-8486831a3ea0.json
```
### 5. Initialise gcloud
```bash
./google-cloud-sdk/bin/gcloud init
```
Please select these configurations
- 1
- test-kube-talk
- ninja-van-experiments
- 30

### 6. Install kubectl
```bash
brew install kubectl
```