from django.shortcuts import render
from .models import Category


def main(request):
    categories = Category.objects.all()
    return render(request, 'index.html', context={'categories': categories})
