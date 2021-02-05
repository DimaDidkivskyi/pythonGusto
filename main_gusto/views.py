import datetime
from django.shortcuts import render, redirect
from .models import Category, Dishes, Event, Banners
from .forms import UserMessageForm


def main(request):
    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
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

    return render(request, 'index.html', context={'categories': categories, 'special_categories': special_categories, 'events': events, 'banners': banners, 'form': users_messages_form})
