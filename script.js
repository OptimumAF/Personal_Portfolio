document.addEventListener('DOMContentLoaded', function() {
  loadNavbar();
});

function loadNavbar() {
  const navbarElement = document.querySelector('header');
  fetch('navbar.html')
    .then(response => response.text())
    .then(html => {
      navbarElement.innerHTML = html;
    })
    .catch(error => {
      console.warn('Failed to load navbar:', error);
    });
}

function navigateToHomePage() {
  window.location.href = "main.html";
}
