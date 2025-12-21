const imageInput = document.getElementById("imageInput");
const previewImg = document.getElementById("previewImg");
if (imageInput) {
    imageInput.addEventListener("input", () => {
        const url = imageInput.value.trim();
        if (url) {
            previewImg.src = url;
        }
    });
}
