from django.shortcuts import render, redirect
from .models import Food
from .forms import FoodForm
from django.db.models import Min

import datetime

peremption_sort = False
# Create your views here.

def form_view(request):
    inv_before = Food.objects.values('gtin',).annotate(peremption=Min('peremption'),).order_by('peremption').filter(peremption__lt=datetime.date.today())
    inv_after = Food.objects.values('gtin',).annotate(peremption=Min('peremption'),).order_by('peremption').filter(peremption__gte=datetime.date.today())
    form = FoodForm()
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    if(request.GET.get('mybtn')):
        peremption_sort = True
    return render(request,'star/Home.html',{'form':form, 'inv_before': inv_before, 'inv_after': inv_after})