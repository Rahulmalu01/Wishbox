/*HERO SLIDER*/
const slider = document.getElementById("slider");
const slides = document.querySelectorAll(".slide");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const dotsContainer = document.getElementById("sliderDots");
let index = 0;
let interval;
if (slider && slides.length && dotsContainer) {
  slides.forEach((_, i) => {
    const dot = document.createElement("span");
    if (i === 0) dot.classList.add("active");
    dot.addEventListener("click", () => {
      goToSlide(i);
    });
    dotsContainer.appendChild(dot);
  });
  const dots = dotsContainer.querySelectorAll("span");
  function updateSlider() {
    slider.style.transform = `translateX(-${index * 100}%)`;
    dots.forEach(d => d.classList.remove("active"));
    if (dots[index]) dots[index].classList.add("active");
  }
  function goToSlide(i) {
    index = i;
    updateSlider();
    resetAutoSlide();
  }
  function nextSlide() {
    index = (index + 1) % slides.length;
    updateSlider();
  }
  function prevSlide() {
    index = (index - 1 + slides.length) % slides.length;
    updateSlider();
  }
  if (nextBtn) nextBtn.addEventListener("click", nextSlide);
  if (prevBtn) prevBtn.addEventListener("click", prevSlide);
  function startAutoSlide() {
    interval = setInterval(nextSlide, 5000);
  }
  function resetAutoSlide() {
    clearInterval(interval);
    startAutoSlide();
  }
  startAutoSlide();
  slider.addEventListener("mouseenter", () => clearInterval(interval));
  slider.addEventListener("mouseleave", startAutoSlide);
}
/*NEWSLETTER FORM*/
const newsletterForm = document.getElementById("newsletterForm");
if (newsletterForm) {
  newsletterForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch("/subscribe/", {
      method: "POST",
      body: formData,
      headers: {
        "X-Requested-With": "XMLHttpRequest"
      }
    })
      .then(res => res.json())
      .then(data => {
        if (data.status === "success") {
          alert("🎉 Subscribed successfully! Check your email.");
          this.reset();
        } else if (data.status === "exists") {
          alert("⚠️ You are already subscribed.");
        } else {
          alert("❌ Something went wrong. Try again.");
        }
      })
      .catch(() => {
        alert("⚠️ Network error. Please try later.");
      });
  });
}
