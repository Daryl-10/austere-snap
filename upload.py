import os
import datetime

from pydrive.auth import GoogleAuth 
from pydrive.drive import GoogleDrive 

def fun_upload():
    gauth = GoogleAuth() 

    # Try to load saved client credentials
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")
    drive = GoogleDrive(gauth)

    # ct stores current date
    ct = datetime.datetime.now().date()
    img_name = "overview_{}.png".format(ct)
    
    # set Google Drive public folder ID
    public_folder_id = ''

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        # if f.endswith(".png"):
        if f == img_name:
            # Read file and set it as the content of this instance. 
            gfile = drive.CreateFile({'parents': [{'id': public_folder_id}]}) #id provided corresponds to public folder
            gfile.SetContentFile(f) 
            gfile.Upload() # Upload the file.
            print("Screenshot has been uploaded: ", f)
