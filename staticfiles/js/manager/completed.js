document.querySelectorAll(".order-table tbody tr").forEach((row, index) => {
    row.style.opacity = 0;
    row.style.transform = "translateY(10px)";
    setTimeout(() => {
        row.style.transition = "all 0.4s ease";
        row.style.opacity = 1;
        row.style.transform = "translateY(0)";
    }, index * 60);
});
