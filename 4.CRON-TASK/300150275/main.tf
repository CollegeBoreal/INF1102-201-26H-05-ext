terraform {
  required_providers {
    proxmox = {
      source  = "bpg/proxmox"
      version = "0.99.0"
    }
  }
}

provider "proxmox" {
  endpoint  = var.pm_url
  api_token = "${var.pm_token_id}=${var.pm_token_secret}"
  insecure  = true
}

resource "proxmox_virtual_environment_vm" "vm" {
  name      = var.pm_vm_name
  node_name = "labinfo"

  clone {
    vm_id = var.clone_vm_id
  }

  cpu {
    cores = 2
  }

  memory {
    dedicated = 2048
  }

  network_device {
    bridge = "vmbr0"
  }

  initialization {
    ip_config {
      ipv4 {
        address = var.vm_ip
        gateway = "10.7.237.1"
      }
    }

    dns {
      servers = [var.pm_nameserver]
    }
  }
}