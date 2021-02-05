from django.shortcuts import render
from main_gusto.models import Dishes

# Create your views here.


def dish_info(request, pk):
    dish = Dishes.objects.get(pk=pk)
    return render(request, 'dish.html', context={'dish': dish})
