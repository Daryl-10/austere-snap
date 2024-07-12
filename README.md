<h1>Austere version for Web Scrap + Snapshot + Upload</h1>

<h3>In this project, we use an automated script that:</h3>
<p>1) visits a website that provides real-time data of vessels near Singapore, bypassing guardrail against headless chromium requests</p>
<p>2) zooms into the target of interest</p>
<p>3) takes a snapshot after the target is obtained</p>
<p>4) uploads the snapshot to a publicly accessible Google Drive folder</p>

<h3>The above is a pre-cursor to creating a Docker image that will be executed on a regular basis using a CRON job</h3>

Follow up features are explored in ["headless-count" project](https://github.com/Daryl-10/headless-count)

---

<h2>On first run:</h2>
<h4>1) pip install virtual environment</h4>

`pip install virtualenv`

<h4>2) Set up virtual environment in project</h4>

`python<version> -m venv <virtual-environment-name>`

<h4>3) Activate virtual environment</h4>
<h4>4) Navigate to main directory and install from requirements.txt</h4>

`pip install -r requirements.txt`

---

<h3>Note that you should supply your own credentials & values for the following:</h3>
<h4>1) client_secrets.json</h4>
    <p>-> This is a preparation step to link the above 'service' to a Cloud Service provider. Sample format shown below is for Google Cloud project</p>

```json
    {"installed":
        {"client_id":"",
        "project_id":"",
        "auth_uri":"https://accounts.google.com/o/oauth2/auth",
        "token_uri":"https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
        "client_secret":"",
        "redirect_uris":["http://localhost"]
        }
    }
```

<h4>2) mycreds.txt</h4>
    <p>-> When running the code for the first time, mycreds.txt is generated after linking to a Cloud Service provider</p>
    <p>-> Afterwards, mycreds.txt is generated & reused for subsequent invokations.</p>
<h4>3) value for public_folder_id variable in upload.py</h4>
    <p>-> This is used to upload to a specific Google Drive folder. Set up for this publicly accessible folder should be done prior to running screengrab.py (& by extension, upload.py)</p>


---

<h3>Integrate Google Cloud CLI with Docker</h3>
<h4>1) gcloud init</h4>
<p>--> Log into gcloud using CLI: User Authentication will be done through browser</p>
<h4>2) Select appropriate gcloud project</h4>
<p>--> (Optional) It might be necessary to configure a default Compute Region and Zone that corresponds to that of the project's Artifact Registry</p>
<h4>3) Configure Docker with the credentials for the same Compute Region and Zone</h4>
<p>--> Sample code</p>

```
gcloud auth configure-docker us-central1-docker.pkg.dev
```

<p>--> Sample output</p>

```json
 {
  "credHelpers": {
    "us-central1-docker.pkg.dev": "gcloud"
  }
}
```

<h4>4) Build the Docker image</h4>
<p>Sample code below is for MacOS with M1 chip & above</p>

```
docker buildx build --platform linux/amd64 -t imgName .
```

<h4>5) Tag the Docker image</h4>

```
docker tag imgName us-central1-docker.pkg.dev/cloudProjName/artifactRegistry/imgName
```

<p><b>imgName</b> should correspond to the one above in Step 4</p>
<p><b>cloudProjName</b> is determined when creating the project in Google Cloud Console</p>
<p><b>artifactRegistry</b> is determined when creating the Artifact Registry in Google Cloud Console</p>

<p>The naming convention is used to push the Docker image to the intended directory in Artifact Registry</p>

<h4>6) Push the Docker image</h4>

```
docker push us-central1-docker.pkg.dev/cloudProjName/artifactRegistry/imgName
```

---
