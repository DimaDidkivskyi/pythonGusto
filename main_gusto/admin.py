from django.contrib import admin
from.models import Category, Dishes, Event, Banners, UserMessages

# Register your models here.


@admin.register(UserMessages)
class UserMessagesAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email')
    readonly_fields = ('user_name', 'user_email', 'message')
    list_filter = ('user_name',)
    search_fields = ('user_name', 'user_name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_order')
    list_filter = ('title',)
    search_fields = ('title', 'title')


@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'category')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'event_date', 'price')
    list_filter = ('title',)
    search_fields = ('title', 'event_date')


@admin.register(Banners)
class BannersAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
