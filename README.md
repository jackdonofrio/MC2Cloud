# MC2Cloud
Python script to download/upload Minecraft worlds to the cloud directly from your saves folder, all from the comfort of the command line.

## Setup
1) Create a [Dropbox developer account](https://www.dropbox.com/lp/developers)
2) Create a new App. Select "App Folder" as the type of access.
3) In your app, click on the Permissions tab. Check all of the permissions under Files and Folders.
4) Go back to the main Settinsg tab, and scroll down to OAuth 2.
5) Under Generate access token in the OAuth 2 section, click Generate.
6) Copy the OAuth2 token and paste it into the OAUTH_KEY value in the script

## Usage
### Uploading worlds
```
python -u My World
```
Uploads world "My World" directly from your saves folder to your dropbox.

### Downloading worlds
```
python -d My World
```
Downloads world "My World" from dropbox directly into your saves folder.
