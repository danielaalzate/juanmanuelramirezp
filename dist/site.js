(() => {
  const config = window.SITE_CONFIG;
  document.documentElement.dataset.theme = 'blue';
  document.addEventListener('DOMContentLoaded', () => {
    const menuButton = document.querySelector('.menu-toggle');
    const nav = document.querySelector('#primary-nav');
    const homeLink = nav?.querySelector('a[aria-current="page"][href="/"]');
    if (homeLink && document.querySelector('.hero')) {
      const updateHomeLink = () => { homeLink.hidden = window.scrollY < 80; };
      updateHomeLink();
      window.addEventListener('scroll', updateHomeLink, { passive: true });
      window.addEventListener('pageshow', updateHomeLink);
    }
    menuButton?.addEventListener('click', () => {
      const open = menuButton.getAttribute('aria-expanded') !== 'true';
      menuButton.setAttribute('aria-expanded', String(open));
      menuButton.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
      nav.classList.toggle('is-open', open);
    });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && menuButton?.getAttribute('aria-expanded') === 'true') {
        menuButton.click(); menuButton.focus();
      }
    });
    const video = document.querySelector('#hero-video');
    if (video) {
      const poster = document.querySelector('.hero-media img');
      if (config.heroPoster) { video.poster = config.heroPoster; poster.src = config.heroPoster; }
      if (!config.heroPosterIllustrative) {
        poster.alt = 'Juan Manuel en su estudio';
        document.querySelector('.hero-notice').textContent = 'Juan Manuel en su estudio';
      }
    }
    if (video && config.heroVideo) {
      video.src = config.heroVideo;
      const notice = document.querySelector('.hero-notice');
      const reduced = matchMedia('(prefers-reduced-motion: reduce)');
      video.addEventListener('playing', () => { video.hidden = false; notice.hidden = true; });
      video.addEventListener('error', () => {
        video.hidden = true; notice.hidden = false;
        notice.textContent = 'El video no está disponible. Se muestra la imagen de respaldo.';
      });
      reduced.addEventListener('change', () => { if (reduced.matches) video.pause(); });
      if (!reduced.matches) video.play().catch(() => {});
    }
    document.querySelectorAll('[data-load-interview]').forEach(button => button.addEventListener('click', () => {
      const frame = document.createElement('iframe');
      frame.src = 'https://www.youtube-nocookie.com/embed/DTZzfXQgzh8?autoplay=1';
      frame.title = 'Leyes, poesía y diplomacia — entrevista de Nerdopolitan';
      frame.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      frame.allowFullscreen = true;
      button.closest('.interview-player').replaceChildren(frame);
    }));
    const filters = document.querySelectorAll('[data-filter]');
    const entries = document.querySelectorAll('[data-category]');
    filters.forEach(button => button.addEventListener('click', () => {
      filters.forEach(other => other.setAttribute('aria-pressed', String(other === button)));
      let count = 0;
      entries.forEach(entry => {
        entry.hidden = button.dataset.filter !== 'all' && entry.dataset.category !== button.dataset.filter;
        if (!entry.hidden) count++;
      });
      document.querySelector('#catalog-status').textContent = `${count} ${count === 1 ? 'publicación' : 'publicaciones'}`;
    }));
  });
})();
