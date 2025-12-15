const grid = document.getElementById("productsGrid");

fetch("/shop/api/products/")
  .then(res => res.json())
  .then(data => {
    data.items.forEach(p => {
      grid.innerHTML += `
        <div class="product-card">
          <img src="${p.img}" alt="${p.name}">
          <h3>${p.name}</h3>
          <p>${p.short_desc}</p>
          <strong>₹${p.price}</strong>
          <button onclick="addToCart('${p.product_id}','${p.name}',${p.price},'${p.img}')">
            Add to Cart
          </button>
        </div>
      `;
    });
  });

function addToCart(id, name, price, img) {
  fetch("/shop/api/cart/add/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken")
    },
    body: JSON.stringify({
      product_id: id,
      name,
      price,
      img,
      qty: 1
    })
  }).then(() => alert("Added to cart 🛒"));
}

function getCookie(name) {
  let cookieValue = null;
  document.cookie.split(";").forEach(c => {
    const cookie = c.trim();
    if (cookie.startsWith(name + "=")) {
      cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
    }
  });
  return cookieValue;
}
