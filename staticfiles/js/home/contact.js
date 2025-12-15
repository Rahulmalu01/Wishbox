document.getElementById("contactForm").addEventListener("submit", function(e) {
    e.preventDefault();

    fetch("", {
        method: "POST",
        body: new FormData(this),
        headers: {
            "X-Requested-With": "XMLHttpRequest"
        }
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            alert("✅ Message sent successfully!");
            this.reset();
        }
    });
});