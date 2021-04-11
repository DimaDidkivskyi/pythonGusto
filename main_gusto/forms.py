from django import forms
from .models import UserMessages, Dishes, Category


class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'type': 'text', 'id': 'category_title', 'class': 'form-control', 'placeholder': 'Назва категорії', 'required': 'required'}))
    category_order = forms.IntegerField(max_value=50, widget=forms.NumberInput(
        attrs={'type': 'text', 'id': 'categoryNumber', 'class': 'form-control', 'placeholder': 'Номер категорії', 'required': 'required'}))
    is_visible = forms.BooleanField(initial=True, required=False, widget=forms.CheckboxInput(attrs={'id': 'category_visible'}))
    is_special = forms.BooleanField(initial=True, required=False, widget=forms.CheckboxInput(attrs={'id': 'category_special'}) ) 
    class Meta():
        model = Category
        fields = ('title', 'category_order', 'is_visible', 'is_special')


class DishesForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                            'type': 'text', 'id': 'title', 'class': 'form-control', 'placeholder': 'Назва страви', 'required': 'required'}))
    price = forms.DecimalField(max_digits=7, decimal_places=2, widget=forms.TextInput(
        attrs={'type': 'text', 'id': 'price', 'class': 'form-control', 'placeholder': 'Ціна', 'required': 'required'}))
    description = forms.CharField(max_length=300, widget=forms.Textarea(
        attrs={'type': 'text', 'id': 'description', 'class': 'form-control', 'rows': '4', 'placeholder': 'Опис страви', 'required': 'required'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'id':'photo_input'}))
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), initial=0)
    is_visible = forms.BooleanField(initial=True, required=False, widget=forms.CheckboxInput(attrs={'id':'dish_visible'}))

    class Meta():
        model = Dishes
        fields = ('title', 'price', 'description',
                  'photo', 'category', 'is_visible')


class UserMessageForm(forms.ModelForm):
    user_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'type': 'text', 'id': 'name', 'class': 'form-control', 'placeholder': 'Ім\'я', 'required': 'required'}))
    user_email = forms.EmailField(widget=forms.TextInput(
        attrs={'type': 'email', 'id': 'email', 'class': 'form-control', 'placeholder': 'Електрона пошта', 'required': 'required'}))
    message = forms.CharField(max_length=200, widget=forms.Textarea(
        attrs={'name': 'message', 'id': 'message', 'class': 'form-control', 'rows': '4', 'placeholder': 'Повідомлення', 'required': 'required'}))

    class Meta():
        model = UserMessages
        fields = ('user_name', 'user_email', 'message')
