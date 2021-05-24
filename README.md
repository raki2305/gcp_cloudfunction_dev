# Google Cloud Function Template for local development
This repository shows how Google Cloud Platform (GCP) cloud functions can be developed
locally and automatically deployed on GCP.

## Steps

### Set up automatic authentication of local GCP developments
It is assumed that the Google Cloud SDK is already installed.

1. Open your cmd.
1. Switch to the current project with _gcloud_: `gcloud config set project your-project-name`
1. With _gcloud_ allow local developments and generate a token: `gcloud auth application-default login`
1. A window pops up. Confirm everything. _gcloud_ now generates a key file in json format with which our 
   applications are automatically authenticates itself against the GCP. So **no** credentials need to be specified in 
   the code!
   
### Using this Repo (Template)
1.  First, clone this repository and set it up on the [Google Cloud Source Repositories](https://source.cloud.google.com/) .
1.  Clone the cloud repository you just created.
1.  Create a separate branch for each future cloud function.
1.  Under _src/_ you will find a _main.py_ file and a requirements.txt. 
    - The main.py contains your future cloud function. 
    - After developing the cloud function, specify all used packages in requirements.txt.
1. Under _utils/_ you will find a _main_local.py_. You can use this file to simulate a trigger. **Please note the comments
   in the file.**
1. Under _config/_ you will find a _cloudbuild.yaml_ file that automates the deployment of the cloud function using the 
   [Google Cloud Build](https://console.cloud.google.com/cloud-build) service. Replace the corresponding placeholders 
   there. **Please note the comments in the file**
1. Push your development.   
   
### Using Cloud Build Service for Deployment
Cloud build is used to set up a CI/CD pipeline. 
1. Within the [Google Cloud Build](https://console.cloud.google.com/cloud-build) service on the left side click on "Trigger".
1. Click on [Create Trigger](https://console.cloud.google.com/cloud-build/triggers/add)
1. Please fill in everything accordingly.
    - In section _Event_ please select "Push to branch".
    - In section _Source_ please refer to your cloud repository and your branch which contains your cloud function.
    - In section _Configuration_
        - Type = "Cloud Build configuration file (yaml or json)".
        - Location = /config/cloudbuild.yaml
    
1. Finally click on "Create".

**Note**: With each push to the specified branch, the cloud function is automatically deployed.



