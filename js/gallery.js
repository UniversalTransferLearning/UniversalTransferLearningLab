(() => {
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const canHover = window.matchMedia('(hover: hover)');

  document.querySelectorAll('.gallery-card').forEach(card => {
    const strip = card.querySelector('.gallery-strip');
    const photoCount = strip.querySelectorAll('.gallery-photo').length;
    if (photoCount < 2) return;

    window.setInterval(() => {
      if (reducedMotion.matches || document.hidden || (canHover.matches && card.matches(':hover'))) return;
      if (strip.matches(':active, :focus-visible')) return;
      const bounds = strip.getBoundingClientRect();
      if (bounds.bottom <= 0 || bounds.top >= window.innerHeight) return;

      const current = Math.round(strip.scrollLeft / strip.clientWidth);
      const next = (Math.max(0, Math.min(current, photoCount - 1)) + 1) % photoCount;
      strip.scrollTo({ left: next * strip.clientWidth, behavior: next === 0 ? 'auto' : 'smooth' });
    }, 5000);
  });
})();
