from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if "count" not in request.session:
        request.session["count"] = 0
        request.session["price"] = 0
    if "sums" not in request.session:
        request.session["sums"] = 0
    return render(request, "shop/index.html")

def checkout(request):

    return render(request, "shop/checkout.html")

def buy(request):
    quantity = request.POST["quantity"]
    request.session["price"] = float(request.POST["product_id"] * int(quantity))
    request.session["sums"] += request.session["price"]
    request.session["count"] += 1
    
    return redirect("/amadon/checkout")