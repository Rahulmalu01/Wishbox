(() => {
  const API_UPDATE = "/api/cart/update-qty/";
  const API_REMOVE = "/api/cart/remove/";
  function getCSRF() {
    const cookie = document.cookie.split(';').map(c => c.trim()).find(c => c.startsWith('csrftoken='));
    return cookie ? cookie.split('=')[1] : '';
  }

  function recalc() {
    const rows = document.querySelectorAll('.cart-row');
    let total = 0, itemsCount = 0;
    rows.forEach(r => {
      const price = parseFloat(r.querySelector('.cart-price').textContent.replace('$','').trim());
      const qty = parseInt(r.querySelector('.qty').textContent);
      total += price * qty;
      itemsCount += qty;
    });
    document.getElementById('summaryTotal').textContent = total.toFixed(2);
    document.getElementById('summaryCount').textContent = itemsCount;
  }

  async function postJSON(url, data){
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type':'application/json', 'X-CSRFToken': getCSRF() },
      body: JSON.stringify(data)
    });
    return res.json();
  }

  document.addEventListener('click', async (e) => {
    if (e.target.matches('.qty-btn.inc')) {
      const id = e.target.getAttribute('data-id');
      const qtyEl = e.target.closest('.cart-row').querySelector('.qty');
      const newQty = parseInt(qtyEl.textContent) + 1;
      const r = await postJSON(API_UPDATE, {product_id: id, qty: newQty});
      if (r?.status === 'ok') { qtyEl.textContent = newQty; recalc(); }
    }

    if (e.target.matches('.qty-btn.dec')) {
      const id = e.target.getAttribute('data-id');
      const row = e.target.closest('.cart-row');
      const qtyEl = row.querySelector('.qty');
      const newQty = Math.max(1, parseInt(qtyEl.textContent) - 1);
      const r = await postJSON(API_UPDATE, {product_id: id, qty: newQty});
      if (r?.status === 'ok') { qtyEl.textContent = newQty; recalc(); }
    }

    if (e.target.matches('.remove-btn')) {
      const id = e.target.getAttribute('data-id');
      const r = await postJSON(API_REMOVE, {product_id: id});
      if (r?.status === 'ok') {
        const row = e.target.closest('.cart-row');
        row.parentNode.removeChild(row);
        recalc();
      }
    }
  });

  document.getElementById('checkoutBtn')?.addEventListener('click', () => {
    window.location.href = "/checkout/";
  });

  document.addEventListener('DOMContentLoaded', recalc);
})();
