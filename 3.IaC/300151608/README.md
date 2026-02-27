terraform {

&nbsp; required\_providers {

&nbsp;   proxmox = {

&nbsp;     source  = "telmate/proxmox"

&nbsp;     version = ">= 2.9.0"

&nbsp;   }

&nbsp; }

}



provider "proxmox" {

&nbsp; pm\_api\_url      = var.pm\_url

&nbsp; pm\_api\_token\_id = var.pm\_token\_id

&nbsp; pm\_api\_token\_secret = var.pm\_token\_secret

&nbsp; pm\_tls\_insecure = true

}

