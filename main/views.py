from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from decimal import Decimal

# Create your views here.
sliderrange = ['product1.jpg', 'product2.jpg', 'product3.jpg', 'product4.jpg', 'product5.jpg', 'product6.jpg', 'product7.jpg', 'product8.jpg', 'product9.jpg']
normalrange = ['top11.jpg', 'top12.jpg', 'top13.jpg', 'top14.jpg']
allrange = ['product1.jpg', 'product2.jpg', 'product3.jpg', 'product4.jpg', 'product5.jpg', 'product6.jpg', 'product7.jpg', 'product8.jpg', 'product9.jpg', 'product10.jpg', 'product11.jpg', 'product12.jpg', 'product13.jpg', 'product14.jpg', 'product15.jpg', 'product16.jpg', 'product17.jpg', 'product18.jpg']

def about(response):
	return render(response, "main/about.html", {})


def home(response):
    return render(response, "main/home.html", {"sliderrange":sliderrange, "normalrange":normalrange})


def shop(response):
    return render(response, "main/shop.html", {"allrange":allrange})

shopping_cart = {}

def individual_product(request):
    if request.method == 'POST':
        product_key = 'KIZEK Tops 1543'.lower()
        amount = int(request.POST.get('amount', 0))
        color = request.POST.get('colour', '').lower()
        size = request.POST.get('size', '').lower()

        # Ensure data integrity in the shopping cart
        item_key = f"{product_key}_{color}_{size}"
        shopping_cart[item_key] = {
            'amount': amount,
            'color': color,
            'size': size,
            'unit_price': Decimal('139.00'),
            'total_price': Decimal(amount) * Decimal('139.00'),
        }

        return redirect('individual_product')  # Redirect to the same page after form submission

    return render(request, "main/individual_product.html", {"sliderrange": sliderrange})


def cart(request):
    print(shopping_cart)
    total = Decimal(0)
    if request.method == 'POST':
        remove_key = request.POST.get('remove', '').lower()
        if remove_key in shopping_cart:
            shopping_cart.pop(remove_key)

    for item_key, item_data in shopping_cart.items():
        total += item_data['total_price']

    return render(request, "main/cart.html", {"shopping_cart": shopping_cart, "total": total})


# for i in range(1, 19):
#     if i <= 4:
#         normalrange.append("top1"+str(i)+".jpg")
#         sliderrange.append("product"+str(i)+".jpg")
#         allrange.append("product"+str(i)+".jpg")
#     elif i <= 9:
#         sliderrange.append("product"+str(i)+".jpg")
#         allrange.append("product"+str(i)+".jpg")
#     else:
#         allrange.append("product"+str(i)+".jpg")