variable INSTANCE_TYPE {
  type = string
  description = "GCP instance type"
}
variable INSTANCE_NAME {
  type = string
  description = "GCP instance name"
}
variable INSTANCE_IMAGE {
  type = string
  description = "GCP instance OS image"
}
variable GCP_PROJECT {
  type = string
  description = "GCP project ID"
}
variable SECURITY_GROUP_ID {
  type = string
  description = "GCP instance security group id"
}
variable CPU_COUNT {
  default = 1
  description = "GCP CPU count"
}
variable DISK_GBS {
  default = 8
  description = "GCP Disk space in GBs"
}
variable SSH_PUB_KEY_FILE {
  type = string
  description = "Path to SSH public key"
}
variable SSH_USER {
  type = string
  description = "SSH username"
}

variable INSTANCE_REGION {
  type = string
  description = "GCP region"
}

variable INSTANCE_ZONE {
  type = string
  description = "GCP zone"
}


resource "google_compute_instance" "cm" {
  name = var.INSTANCE_NAME
  machine_type = var.INSTANCE_TYPE
  zone         = var.INSTANCE_ZONE
  project = var.GCP_PROJECT
  tags = ["cm"]

  boot_disk {
    initialize_params {
      image = var.INSTANCE_IMAGE
      labels = {
        my_label = "value"
      }
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral public IP
    }
  }

  metadata = {
    ssh-keys = "${var.SSH_USER}:${file(var.SSH_PUB_KEY_FILE)}"
  }

  metadata_startup_script = "echo hi > /test.txt"


}
