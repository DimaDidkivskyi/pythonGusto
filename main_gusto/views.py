from django.shortcuts import render
from .models import Category, Dishes


def main(request):
    categories = Category.objects.filter(
        is_visible=True).order_by('category_order')
    for item in categories:
        item.dishes = Dishes.objects.filter(category=item.pk)
    return render(request, 'index.html', context={'categories': categories})
