from django.shortcuts import render
from main_gusto.models import UserMessages
from django.core.paginator import Paginator

# Create your views here.


def messages_view(request):
    messages = UserMessages.objects.filter(
        is_processed=False).order_by('send_date')
    paginator = Paginator(messages, 5)
    page = request.GET.get('page')
    messages_page = paginator.get_page(page)
    return render(request, 'message_page.html', context={'items': messages_page})
