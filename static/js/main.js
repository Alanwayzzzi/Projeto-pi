// Menu "+" da navbar
document.querySelectorAll("[data-menu]").forEach((botao) => {
  const lista = document.getElementById(botao.dataset.menu);
  botao.addEventListener("click", (e) => {
    e.stopPropagation();
    lista.hidden = !lista.hidden;
  });
  document.addEventListener("click", () => (lista.hidden = true));
});

// Abrir e fechar janelas (modais)
document.querySelectorAll("[data-abrir]").forEach((botao) => {
  botao.addEventListener("click", () => {
    document.getElementById(botao.dataset.abrir).showModal();
  });
});
document.querySelectorAll("[data-fechar]").forEach((botao) => {
  botao.addEventListener("click", () => botao.closest("dialog").close());
});

// Pedir confirmação antes de excluir
document.querySelectorAll("form[data-confirmar]").forEach((form) => {
  form.addEventListener("submit", (e) => {
    if (!confirm(form.dataset.confirmar)) e.preventDefault();
  });
});

// Esconder mensagens depois de alguns segundos
document.querySelectorAll(".mensagem").forEach((m) => {
  setTimeout(() => m.remove(), 5000);
});
