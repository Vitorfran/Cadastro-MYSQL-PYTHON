function transitionPage(event, url, isCadastro) {
    event.preventDefault(); // Evita o carregamento imediato da página

    // Aplica classe de animação dependendo da página
    document.body.classList.add(isCadastro ? "exit-login" : "exit-cadastro");

    setTimeout(() => {
        window.location.href = url; // Faz a troca de página após a animação
    }, 800); // Tempo da animação
}

// Aplica animação ao carregar a nova página
document.addEventListener("DOMContentLoaded", () => {
    document.body.classList.add("page-transition");
    setTimeout(() => {
        document.body.classList.add("enter-page"); // Garante que os elementos entrem suavemente
    }, 50);
});
