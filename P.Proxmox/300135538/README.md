\# 🖥️ TP Proxmox VE — Virtualisation et Services Linux



\## 👤 Informations étudiant



| Champ | Détails |

|---|---|

| Nom | Mohamed Reda El Youssoufi |

| Matricule | 300135538 |

| Travail | TP Proxmox |

| Technologie | Proxmox VE |

| Sujet | Virtualisation et services Linux |



\---



\# 🎯 Objectifs



Ce TP permet de :



\- Comprendre Proxmox VE

\- Comprendre la virtualisation

\- Découvrir les services Proxmox

\- Utiliser systemctl

\- Vérifier les services Linux

\- Comprendre Infrastructure virtuelle



\---



\# 📁 Structure du projet



```text

10.Proxmox/

└── 300135538/

&#x20;   ├── README.md

&#x20;   ├── proxmox-services.txt

&#x20;   ├── commandes.txt

&#x20;   └── images/

&#x20;       ├── structure.png

&#x20;       ├── services.png

&#x20;       └── commandes.png

```



\---



\# 🌐 Définition de Proxmox



Proxmox VE (Virtual Environment) est une plateforme open-source de virtualisation basée sur Debian Linux.



Elle permet de :



\- créer des machines virtuelles (VM)

\- gérer des conteneurs LXC

\- administrer des serveurs virtuels

\- gérer les snapshots et backups



\---



\# ⚙️ Services Proxmox



\## Fichier : `proxmox-services.txt`



```text

pve-cluster

pvedaemon

pveproxy

pvestatd

pve-firewall

qemu-server

lxc

corosync

```



\---



\# 💻 Commandes Linux importantes



\## Fichier : `commandes.txt`



```bash

systemctl restart pveproxy



systemctl restart pvedaemon



systemctl status pveproxy



systemctl status pvedaemon



systemctl list-units --type=service | grep pve



journalctl -u pveproxy -f

```



\---



\# 📸 Captures d’écran



\## Structure du projet



!\[Structure](images/structure.png)



\---



\## Services Proxmox



!\[Services](images/services.png)



\---



\## Commandes Linux



!\[Commandes](images/commandes.png)



\---



\# 🧠 Services essentiels Proxmox



| Service | Rôle |

|---|---|

| pveproxy | Interface Web |

| pvedaemon | API backend |

| pve-cluster | Gestion cluster |

| pvestatd | Statistiques système |

| qemu-server | Gestion VM |

| lxc | Gestion conteneurs |



\---



\# ⚖️ Proxmox vs VirtualBox



| Proxmox | VirtualBox |

|---|---|

| Serveur | Desktop |

| KVM + LXC | VM uniquement |

| Cluster | Non |

| Administration Web | Locale |



\---



\# 🔥 Commandes importantes



\## Redémarrer l’interface Web



```bash

systemctl restart pveproxy

```



\## Vérifier les services



```bash

systemctl status pveproxy

```



\## Voir les services pve



```bash

systemctl list-units --type=service | grep pve

```



\---



\# ☁️ Virtualisation



La virtualisation permet d’exécuter plusieurs systèmes virtuels sur un seul serveur physique.



Proxmox utilise :



\- KVM pour les machines virtuelles

\- LXC pour les conteneurs Linux



\---



\# ✅ Résultat



Le TP a permis :



\- ✔ Comprendre Proxmox VE

\- ✔ Comprendre la virtualisation

\- ✔ Comprendre les services Linux

\- ✔ Utiliser systemctl

\- ✔ Gérer les services Proxmox

\- ✔ Comprendre les VM et conteneurs



\---



\# 📚 Concepts appris



\- Virtualisation

\- Proxmox VE

\- Services Linux

\- systemctl

\- KVM

\- LXC

\- Cluster

\- Interface Web

\- Infrastructure virtuelle



\---



\# 🔚 Conclusion



Proxmox VE est une plateforme puissante de virtualisation basée sur Linux.



Elle simplifie :



\- la gestion des machines virtuelles

\- l’administration système

\- les infrastructures modernes



Elle constitue une solution très utilisée en DevOps et administration système.

