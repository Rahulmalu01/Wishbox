document.querySelectorAll(".stat-number").forEach(el => {
    el.style.opacity = 0;
    setTimeout(() => {
        el.style.transition = "opacity 0.6s ease";
        el.style.opacity = 1;
    }, 200);
});
