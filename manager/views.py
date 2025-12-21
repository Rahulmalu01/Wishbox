from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from bson import ObjectId
from db_connection import get_collection

@staff_member_required
def home(request):
    products_col = get_collection("carts")
    orders_col = get_collection("orders")
    product_count = products_col.count_documents({})
    active_orders = orders_col.count_documents({"status": {"$ne": "completed"}})
    completed_orders = orders_col.count_documents({"status": "completed"})
    revenue_cursor = orders_col.find(
        {"status": "completed"},
        {"amount": 1}
    )
    total_revenue = sum(float(o.get("amount", 0)) for o in revenue_cursor)
    recent_orders = list(
        orders_col.find({})
        .sort("created_at", -1)
        .limit(5)
    )
    context = {
        "product_count": product_count,
        "active_orders": active_orders,
        "completed_orders": completed_orders,
        "total_revenue": round(total_revenue, 2),
        "recent_orders": recent_orders,
    }
    return render(request, "home.html", context)

@staff_member_required
def addproduct(request):
    if request.method == "POST":
        try:
            product_id = int(request.POST.get("id"))
            name = request.POST.get("name").strip()
            price = float(request.POST.get("price"))
            category = request.POST.get("category", "").strip()
            image = request.POST.get("image", "").strip()
            description = request.POST.get("description", "").strip()
            stock = int(request.POST.get("stock", 0))
        except (TypeError, ValueError):
            messages.error(request, "Invalid input values.")
            return redirect("manager:addproduct")
        if not name:
            messages.error(request, "Product name is required.")
            return redirect("manager:addproduct")
        products_col = get_collection("carts")
        if products_col.find_one({"id": product_id}):
            messages.error(request, "Product with this ID already exists.")
            return redirect("manager:addproduct")
        product_doc = {
            "id": product_id,
            "name": name,
            "price": price,
            "category": category,
            "image": image,
            "description": description,
            "stock": stock,
            "created_at": None,
            "updated_at": None,
        }
        products_col.insert_one(product_doc)
        messages.success(request, "✅ Product added successfully!")
        return redirect("manager:addproduct")
    return render(request, "add.html")

@staff_member_required
def alterproduct(request):
    products = list(get_collection("carts").find({}))
    return render(request, "alter.html", {"products": products})

@staff_member_required
def updateproduct(request):
    if request.method == "POST":
        product_id = int(request.POST.get("id"))
        get_collection("carts").update_one(
            {"id": product_id},
            {"$set": {
                "name": request.POST.get("name"),
                "price": float(request.POST.get("price")),
                "category": request.POST.get("category"),
                "stock": int(request.POST.get("stock", 0)),
            }}
        )
        messages.success(request, "Product updated successfully")
    return redirect("manager:alterproduct")

@staff_member_required
def deleteproduct(request, product_id):
    get_collection("carts").delete_one({"id": int(product_id)})
    messages.success(request, "Product deleted")
    return redirect("manager:alterproduct")

@staff_member_required
def vieworder(request):
    orders = list(
        get_collection("orders").find(
            {"status": {"$ne": "completed"}}
        ).sort("created_at", -1)
    )
    return render(request, "order.html", {"orders": orders})

@staff_member_required
def markcompleted(request, order_id):
    if request.method == "POST":
        get_collection("orders").update_one(
            {"_id": ObjectId(order_id)},
            {"$set": {"status": "completed"}}
        )
    return redirect("manager:vieworder")

@staff_member_required
def completedorder(request):
    orders = list(get_collection("orders").find({"status": "completed"}))
    return render(request, "completed.html", {"orders": orders})
