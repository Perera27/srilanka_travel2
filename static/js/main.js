/* Lanka Explorer — main.js */

document.addEventListener('DOMContentLoaded', () => {

  // ---- CSRF helper for AJAX ----
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      document.cookie.split(';').forEach(cookie => {
        const c = cookie.trim();
        if (c.startsWith(name + '=')) {
          cookieValue = decodeURIComponent(c.substring(name.length + 1));
        }
      });
    }
    return cookieValue;
  }
  window.csrfToken = getCookie('csrftoken');

  // ---- Smooth scroll for anchor links ----
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', e => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // ---- Image lazy loading fallback ----
  document.querySelectorAll('img[loading="lazy"]').forEach(img => {
    img.addEventListener('error', () => {
      img.style.display = 'none';
      const placeholder = img.closest('.card-img-wrap, .mini-card-img, .gem-card');
      if (placeholder) {
        const p = document.createElement('div');
        p.className = 'card-img-placeholder';
        p.textContent = '🗺️';
        placeholder.appendChild(p);
      }
    });
  });

  // ---- Filter form: preserve all params on select change ----
  const filterForm = document.getElementById('filterForm');
  if (filterForm) {
    // Already handled via onchange="this.form.submit()" in template
    // Additional: highlight active filters
    const selects = filterForm.querySelectorAll('select');
    selects.forEach(sel => {
      if (sel.value) sel.style.borderColor = 'var(--primary)';
      sel.addEventListener('change', () => {
        sel.style.borderColor = sel.value ? 'var(--primary)' : '';
      });
    });
  }

  // ---- Destination card entrance animation ----
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.destination-card, .why-card, .gem-card').forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = `opacity 0.4s ease ${i * 0.05}s, transform 0.4s ease ${i * 0.05}s, box-shadow 0.25s`;
    observer.observe(el);
  });

  // ---- Toast notifications helper ----
  window.showToast = (msg, type = 'success') => {
    const container = document.getElementById('alertContainer') || (() => {
      const c = document.createElement('div');
      c.id = 'alertContainer';
      c.className = 'container mt-3';
      document.querySelector('main').prepend(c);
      return c;
    })();
    const alert = document.createElement('div');
    alert.className = `alert alert-${type} alert-dismissible fade show rounded-3 shadow-sm`;
    alert.innerHTML = `${msg}<button type="button" class="btn-close" data-bs-dismiss="alert"></button>`;
    container.appendChild(alert);
    setTimeout(() => { alert.classList.remove('show'); }, 3500);
  };

});
