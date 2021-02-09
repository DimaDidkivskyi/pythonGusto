import datetime
from django.shortcuts import render, redirect
from .models import Category, Dishes, Event, Banners
from .forms import UserMessageForm, CategoryForm, DishesForm


def main(request):
    if request.method == 'POST':
        if 'sendMessage' in request.POST:
            form = UserMessageForm(request.POST)
            if form.is_valid():
                form.save()

        if 'createCategory' in request.POST:
            form2 = CategoryForm(request.POST)
            if form2.is_valid():
                form2.save()

        if 'createDish' in request.POST:
            form3 = DishesForm(request.POST, request.FILES)
            if form3.is_valid():
                form3.save()
        return redirect('/')

    banners = Banners.objects.filter(is_visible=True)

    special_categories = Category.objects.filter(
        is_visible=True).filter(is_special=True).order_by('category_order')
    for item in special_categories:
        item.dishes = Dishes.objects.filter(category=item.pk)

    categories = Category.objects.filter(
        is_visible=True).filter(is_special=False).order_by('category_order')
    for item in categories:
        item.dishes = Dishes.objects.filter(category=item.pk)

    events = Event.objects.filter(event_date__gte=datetime.date.today())

    users_messages_form = UserMessageForm()
    category_form = CategoryForm()
    dishes_form = DishesForm()

    return render(request, 'index.html', context={'categories': categories, 'special_categories': special_categories, 'events': events, 'banners': banners, 'form1': users_messages_form, 'form2': category_form, 'form3': dishes_form, })
