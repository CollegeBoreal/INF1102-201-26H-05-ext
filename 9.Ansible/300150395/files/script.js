// Passer de sombre à clair (et retour)
const body = document.body;
const now = new Date().getHours();
if (now >= 7 && now <= 19) body.setAttribute("data-theme", "light");

// Bouton mode (si tu veux le mettre plus tard)
console.log("Site Ansible + IaC prêt pour le TP 300150395");
