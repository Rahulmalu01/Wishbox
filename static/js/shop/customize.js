const prices = { mug:15, tshirt:25, canvas:40, pillow:30, blanket:50 };
const packagingPrices = { standard:0, premium:5, deluxe:10 };
const product = document.getElementById("productSelect");
const packaging = document.getElementById("packaging");
const wrap = document.getElementById("giftWrap");
const baseEl = document.getElementById("basePrice");
const packEl = document.getElementById("packagingPrice");
const wrapEl = document.getElementById("wrappingPrice");
const totalEl = document.getElementById("totalPrice");
const baseInput = document.getElementById("basePriceInput");
const packInput = document.getElementById("packagingPriceInput");
const wrapInput = document.getElementById("wrappingPriceInput");
const totalInput = document.getElementById("totalPriceInput");
function updatePrice() {
  const base = prices[product.value] || 0;
  const pack = packagingPrices[packaging.value] || 0;
  const w = wrap.checked ? 3 : 0;
  const total = base + pack + w;
  baseEl.textContent = base;
  packEl.textContent = pack;
  wrapEl.textContent = w;
  totalEl.textContent = total;
  baseInput.value = base;
  packInput.value = pack;
  wrapInput.value = w;
  totalInput.value = total;
}
product.onchange = packaging.onchange = wrap.onchange = updatePrice;
const text = document.getElementById("customText");
const previewText = document.getElementById("previewText");
const count = document.getElementById("charCount");
text.oninput = () => {
  previewText.textContent = text.value || "Your text here";
  count.textContent = text.value.length;
};
document.getElementById("textColor").onchange =
  e => previewText.style.color = e.target.value;
document.getElementById("textFont").onchange =
  e => previewText.style.fontFamily = e.target.value;
document.getElementById("imageUpload").onchange = e => {
  const file = e.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = ev => document.getElementById("previewImage").src = ev.target.result;
  reader.readAsDataURL(file);
};
