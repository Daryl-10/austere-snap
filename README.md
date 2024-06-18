<h1>Austere version for Web Scrap + Snapshot + Upload</h1>

<h3>In this project, we use an automated script that:</h3>
<p>1) visits a website that provides real-time data of vessels near Singapore, bypassing guardrail against headless chromium requests</p>
<p>2) zooms into the target of interest</p>
<p>3) takes a snapshot after the target is obtained</p>
<p>4) uploads the snapshot to a publicly accessible Google Drive folder</p>

<h3>The above is a pre-cursor to creating a Docker image that will be executed on a regular basis using a CRON job</h3>

---

<h3>Note that you should supply your own credentials & values for the following:</h3>
<h4>1) client_secrets.json</h4>
    <p>-> This is a preparation step to link the above 'service' to a Cloud Service provider. Sample format shown below is for Google Cloud project</p>
    <p>{"installed":
    {"client_id":"",
    "project_id":"",
    "auth_uri":"https://accounts.google.com/o/oauth2/auth",
    "token_uri":"https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
    "client_secret":"",
    "redirect_uris":["http://localhost"]}
}</p>
<h4>2) mycreds.txt</h4>
    <p>-> When running the code for the first time, mycreds.txt is generated after linking to a Cloud Service provider</p>
    <p>-> Afterwards, mycreds.txt is generated & reused for subsequent invokations.</p>
<h4>3) value for public_folder_id variable in upload.py</h4>
    <p>-> This is used to upload to a specific Google Drive folder. Set up for this publicly accessible folder should be done prior to running screengrab.py (& by extension, upload.py)</p>