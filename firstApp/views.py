from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'templatesApp/index.html')

def peluche(request):
    data={"imag1":"https://cdn.shopify.com/s/files/1/2675/4376/products/N-2109-485276_1_512x512.jpg?v=1632379297","imag2":"https://cdn.shopify.com/s/files/1/0770/2163/products/mmwash1.jpg?v=1651271060","imag3":"https://cdn.shopify.com/s/files/1/0416/8083/0620/products/610020-Zoom.1_600x.jpg?v=1657303214","prod1":"Kuromi 15cm","prod2":"My Melody 20cm","prod3":"Hello Kitty"}
    return render(request,'templatesApp/productos.html',data)