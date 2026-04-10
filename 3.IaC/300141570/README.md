## 📸 Résultat du déploiement

<p align="center">
  <img src="300141570/images/screenshot.png" width="700"/>
</p>

# 🏗️ Infrastructure as Code (IaC) avec OpenTofu et Proxmox

## 📌 Objectif
Dans ce travail, nous avons découvert le concept de **Infrastructure as Code (IaC)**, qui consiste à gérer et déployer une infrastructure informatique à l’aide de fichiers de configuration plutôt que par des manipulations manuelles. Cette approche permet d’automatiser les déploiements, de réduire les erreurs humaines et de garantir une meilleure reproductibilité des environnements. :contentReference[oaicite:0]{index=0}

## 📖 Ce que nous avons appris
Nous avons étudié la différence entre l’administration système traditionnelle et l’approche IaC. L’administration manuelle entraîne souvent des problèmes comme les incohérences entre serveurs, la lenteur des déploiements et une documentation incomplète. À l’inverse, l’IaC permet de définir l’infrastructure sous forme de code, versionné avec Git, ce qui facilite l’automatisation, la maintenance et le suivi des modifications. :contentReference[oaicite:1]{index=1}

Nous avons aussi vu les deux approches principales :
- **Approche déclarative** : on décrit l’état final souhaité, puis l’outil s’occupe de l’appliquer.
- **Approche impérative** : on exécute une suite d’instructions dans un ordre précis. :contentReference[oaicite:2]{index=2}

## 🛠️ Outils utilisés
Dans cette activité, l’outil principal utilisé est **OpenTofu**, avec le fournisseur **Proxmox**, afin de déployer automatiquement une machine virtuelle Linux à partir d’un template cloud-init. Le travail incluait aussi l’utilisation de **GitHub** pour le versionnement du projet. :contentReference[oaicite:3]{index=3}

## ⚙️ Réalisation
Nous avons créé la structure du projet avec plusieurs fichiers de configuration :
- `provider.tf`
- `main.tf`
- `variables.tf`
- `terraform.tfvars`

Ensuite, nous avons configuré :
- l’accès à l’API Proxmox
- le nom de la machine virtuelle
- l’adresse IP
- le nameserver
- le stockage
- les clés SSH
- les ressources matérielles comme la mémoire et le processeur. :contentReference[oaicite:4]{index=4}

## 🚀 Déploiement
Le déploiement de la machine virtuelle a été réalisé avec les commandes suivantes :

```bash
tofu init
tofu plan
tofu apply


