const modal = document.getElementById("editModal");
function openEditModal(id, name, price, category, stock) {
    modal.style.display = "flex";
    document.getElementById("editId").value = id;
    document.getElementById("editName").value = name;
    document.getElementById("editPrice").value = price;
    document.getElementById("editCategory").value = category;
    document.getElementById("editStock").value = stock;
}
function closeEditModal() {
    modal.style.display = "none";
}
window.onclick = function(e) {
    if (e.target === modal) closeEditModal();
}
