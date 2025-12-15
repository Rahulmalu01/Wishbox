// Scroll reveal
const reveals = document.querySelectorAll(".reveal");

const revealOnScroll = () => {
  reveals.forEach(el => {
    const top = el.getBoundingClientRect().top;
    if (top < window.innerHeight - 80) {
      el.classList.add("active");
    }
  });
};

window.addEventListener("scroll", revealOnScroll);
revealOnScroll();

// Counter animation
const counters = document.querySelectorAll(".stat h3");

counters.forEach(counter => {
  const update = () => {
    const target = +counter.getAttribute("data-count");
    const current = +counter.innerText;
    const increment = Math.ceil(target / 80);

    if (current < target) {
      counter.innerText = current + increment;
      setTimeout(update, 30);
    } else {
      counter.innerText = target + (target === 100 ? "%" : "+");
    }
  };
  update();
});
