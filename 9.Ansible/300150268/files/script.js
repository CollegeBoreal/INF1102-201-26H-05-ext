console.log("Site déployé avec Ansible - 300150268");

window.onload = function() {
    const container = document.querySelector('.container');
    container.style.opacity = '0';
    container.style.transition = 'opacity 1.5s ease';
    setTimeout(() => {
        container.style.opacity = '1';
    }, 100);
};