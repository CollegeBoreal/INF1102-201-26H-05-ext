variable "pm_url" {
  type = string
}

variable "pm_token_id" {
  type = string
}

variable "pm_token_secret" {
  type      = string
  sensitive = true
}

variable "pm_vm_name" {
  type = string
}

variable "pm_nameserver" {
  type = string
}

variable "vm_ip" {
  type = string
}

variable "clone_vm_id" {
  type = number
}