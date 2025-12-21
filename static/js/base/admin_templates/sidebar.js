document.querySelectorAll(".sidebar-nav a").forEach(link => {
    if (link.href === window.location.href) {
        link.classList.add("active");
    }
});
