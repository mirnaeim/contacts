from django.shortcuts import render, HttpResponse
from .models import Contact
# Create your views here.


def contact_list(request):
    context = {
        "contacts": Contact.objects.all(),
    }
    return render(
        request=request,
        context=context,
        template_name='index.html'
    )
