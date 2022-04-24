from django.shortcuts import render, redirect
from .models import Food
from .forms import FoodForm
from django.db.models import Min

# Create your views here.

def form_view(request):
    inv = Food.objects.values('gtin',).annotate(peremption=Min('peremption'),).order_by()
    form = FoodForm()
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'star/Home.html',{'form':form, 'inv': inv})