provider "google" {
  project = "your-project-name"
  region = "europe-west3" #Change, if necessary
  zone = "europe-west3-b" #Change, if necessary
}

resource "google_cloudbuild_trigger" "NAME" {
  name = "TRIGGER NAME"
  description = "DESCRIPTION"
  trigger_template {
    branch_name = "NAME OF YOUR BRANCH"
    repo_name = "NAME OF YOUR CLOUD REPO"
  }
  filename = "config/cloudbuild.yaml"
}