import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from db_connection import get_collection, save_custom_order


# ===============================
# PAGES
# ===============================
def products_page(request):
    return render(request, "products.html")


@ensure_csrf_cookie
def cart_page(request):
    return render(request, "cart.html")


@login_required
def customize_page(request):
    return render(request, "customize.html")


# ===============================
# PRODUCTS API (FIXED)
# ===============================
@require_GET
def api_list_products(request):
    col = get_collection("carts")  # ← matches MongoDB screenshot

    cursor = col.find({})
    items = []

    for doc in cursor:
        items.append({
            "product_id": doc.get("id"),
            "name": doc.get("name"),
            "price": float(doc.get("price", 0)),
            "img": doc.get("image", "/static/assets/placeholder.png"),
            "tags": [doc.get("category")],
            "short_desc": doc.get("description", ""),
            "stock": 10
        })

    return JsonResponse({
        "items": items,
        "total": len(items),
        "page": 1,
        "pages": 1,
        "limit": len(items)
    })


# ===============================
# CART APIs
# ===============================
@require_GET
def api_get_cart(request):
    if not request.session.session_key:
        request.session.save()

    cart = get_collection("user_carts").find_one(
        {"session": request.session.session_key}
    ) or {"items": []}

    return JsonResponse(cart, safe=False)


@require_POST
def api_add_to_cart(request):
    try:
        data = json.loads(request.body)
    except Exception:
        return HttpResponseBadRequest("Invalid JSON")

    required = ("product_id", "name", "price")
    if not all(k in data for k in required):
        return HttpResponseBadRequest("Missing fields")

    col = get_collection("user_carts")

    if not request.session.session_key:
        request.session.save()

    cart = col.find_one({"session": request.session.session_key})
    if not cart:
        cart = {
            "session": request.session.session_key,
            "items": [],
            "updated_at": timezone.now()
        }

    cart["items"].append({
        "product_id": data["product_id"],
        "name": data["name"],
        "price": float(data["price"]),
        "qty": int(data.get("qty", 1)),
        "img": data.get("img", "")
    })

    col.update_one(
        {"session": request.session.session_key},
        {"$set": cart},
        upsert=True
    )

    return JsonResponse({"status": "ok"})


# ===============================
# CUSTOMIZE ORDER
# ===============================
@login_required
@require_POST
def api_save_custom_order(request):
    try:
        data = json.loads(request.body)
    except Exception:
        return HttpResponseBadRequest("Invalid JSON")

    save_custom_order({
        "user_id": request.user.id,
        "product": data.get("product"),
        "custom_text": data.get("custom_text"),
        "text_color": data.get("text_color"),
        "text_font": data.get("text_font"),
        "packaging": data.get("packaging"),
        "gift_wrap": data.get("gift_wrap", False),
        "pricing": data.get("pricing", {})
    })

    return JsonResponse({"success": True})
