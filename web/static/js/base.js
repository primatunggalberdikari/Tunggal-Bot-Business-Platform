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

    /* ---------- Auto-Hide Flash Messages ---------- */
document.addEventListener('DOMContentLoaded', () => {
  const flashMessages = document.querySelectorAll('.flash-message');
  
  flashMessages.forEach((msg) => {
    // Auto hide setelah 5 detik
    setTimeout(() => {
      msg.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      msg.style.opacity = '0';
      msg.style.transform = 'translateY(-10px)';
      
      // Hapus dari DOM setelah animasi
      setTimeout(() => {
        msg.remove();
      }, 500);
    }, 5000);
  });
});