import os
import dropbox
import zipfile
import sys

OAUTH_KEY = 'YOUR KEY HERE'
dbox = dropbox.Dropbox(OAUTH_KEY)

# Check if windows vs Mac
if os.name == 'nt': # Windows
    saves_location = os.getenv('APPDATA') + '\\.minecraft\\saves\\'
else: # Mac, os.name == 'posix'
    saves_location = os.getenv('HOME') + '/Library/Application Support/minecraft/saves/'

# Modified version of this algorithm: https://github.com/dropbox/dropbox-sdk-python/issues/107#issuecomment-344025564
def upload_save(save_name):
    for dir, dirs, files in os.walk(saves_location + save_name):
        rel = os.path.relpath(dir)
        rel = '/' + rel[rel.index(save_name):].replace('\\','/')
        print('Uploading files from ' + rel)
        for file in files:
            try:
                file_path = os.path.join(dir, file)
                dest_path = rel + '/' + file
                print(f'Uploading {dest_path}')
                with open(file_path, 'rb') as f:
                    dbox.files_upload(f.read(), dest_path, mute=True, mode=dropbox.files.WriteMode('overwrite'))
            except Exception as e:
                print(f"Failed to upload {file}\n{e}")
    print(f'Finished uploading {save_name}')

def download_save(save_name):
    path = '/' + save_name
    zip_file_path = saves_location + f'/{save_name}.zip'
    dbox.files_download_zip_to_file(zip_file_path, path)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(saves_location)
    os.remove(zip_file_path)
    print(f'Downloaded {save_name}')

if __name__ == '__main__':
    command = sys.argv[1]
    world_name = ' '.join(sys.argv[2:])
    if command == '-d' or command == '-download':
        if world_name:
            download_save(world_name)
    elif command == '-u' or command == '-upload':
        if world_name:
            upload_save(world_name)

# To-do
# Look into using parallel computing to upload faster

# Setup
# 1) Create DropBox Dev account
# 2) Change permissions to allow file content writing
# 3) Generate OAuth 2 token
