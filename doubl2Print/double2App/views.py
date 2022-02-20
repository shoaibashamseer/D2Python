from django.shortcuts import render
from . models import Canvas
from . models import Product

# Create your views here.
def modifications(request):
    canva_obj=Canvas.objects.all()
    pro_obj = Product.objects.all()
    return render(request,'index.html',{'canva_result':canva_obj,'pro_result':pro_obj})