resource "proxmox_vm_qemu" "vm1" {

  name        = var.pm_vm_name
  target_node = "labinfo"
  clone       = "ubuntu-jammy-template"
  full_clone  = false

  cores   = 2
  sockets = 1
  memory  = 2048

  scsihw = "virtio-scsi-pci"

  disk {
    size    = "10G"
    type    = "scsi"
    storage = "local-lvm"
  }

  network {
    model  = "virtio"
    bridge = "vmbr0"
  }

  os_type    = "cloud-init"
  ipconfig0  = var.pm_ipconfig0
  nameserver = var.pm_nameserver

  ciuser = "ubuntu"

  # ✅ SSH : seulement TA clé (la clé du prof est invalide chez toi)
  sshkeys = file("C:\\Users\\user\\.ssh\\id_ed25519.clean.pub")
}