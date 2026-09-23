/* ============================================================ */
/* BASE JS — Global JavaScript untuk Semua Halaman             */
/* ============================================================ */

/* ---------- Theme Toggle ---------- */
document.addEventListener('DOMContentLoaded', () => {
  const toggleButton = document.getElementById('theme-toggle');
  const htmlElement = document.documentElement;

  if (!toggleButton) return;

  // Cek preferensi tersimpan
  const savedTheme = localStorage.getItem('theme');

  if (savedTheme === 'dark') {
    htmlElement.classList.add('dark-mode');
  } else if (savedTheme === 'light') {
    htmlElement.classList.remove('dark-mode');
  } else {
    // Ikuti preferensi sistem
    if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
      htmlElement.classList.add('dark-mode');
    }
  }

  // Handler klik toggle
  toggleButton.addEventListener('click', () => {
    htmlElement.classList.toggle('dark-mode');

    if (htmlElement.classList.contains('dark-mode')) {
      localStorage.setItem('theme', 'dark');
    } else {
      localStorage.setItem('theme', 'light');
    }
  });
});