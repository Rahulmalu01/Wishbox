document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.footer .social-links a').forEach(a => {
    a.setAttribute('rel', 'noopener noreferrer');
  });
});
