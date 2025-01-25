terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.17.0"
    }
  }
}

provider "google" {
    credentials = "./keys/my_creds.json"
  project     = "datatalks-terraform"
  region      = "europe-west1-b"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "datatalks-terraform-demo-bucket"
  location      = "EU"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}