from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
def about(response):
	return render(response, "main/about.html", {})


sliderrange = []
normalrange = []
allrange = []
for i in range(1, 19):
    if i <= 4:
        normalrange.append("top1"+str(i)+".JPG")
        sliderrange.append("product"+str(i)+".JPG")
        allrange.append("product"+str(i)+".JPG")
    elif i <= 9:
        sliderrange.append("product"+str(i)+".JPG")
        allrange.append("product"+str(i)+".JPG")
    else:
        allrange.append("product"+str(i)+".JPG")

def home(response):
	return render(response, "main/home.html", {"sliderrange":sliderrange, "normalrange":normalrange})


def shop(response):
	return render(response, "main/shop.html", {"allrange":allrange})


shopping_cart = {}

def individual_product(request):
    print(shopping_cart)

    if request.method == 'POST':
        amount = request.POST.get('amount', '').lower()
        color = request.POST.get('colour', '').lower()
        size = request.POST.get('size', '').lower()
        shopping_cart['KIZEK Tops 1543'.lower()] = [amount, color, size, 139, int(amount)*139]

    return render(request, "main/individual_product.html", {"sliderrange": sliderrange})


def cart(request):
    total = 0
    for items, values in shopping_cart.items():
        total += (int(values[0])*int(values[3])) 
    if request.method == 'POST':
        remove = request.POST.get('remove', '').lower()
        print(remove)
        shopping_cart.pop(remove)
        return redirect('/cart')
    return render(request, "main/cart.html", {"shopping_cart": shopping_cart, "total":total, })


