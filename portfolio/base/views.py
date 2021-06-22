from django.shortcuts import render
from .models import Card
from django.views import generic
# Create your views here.

def home(request):
    cards = Card.objects.all()
    return render(request, 'base/home.html', {'cards':cards})

class CardView(generic.ListView):
    model = Card
    template_name = 'base/card.html'
