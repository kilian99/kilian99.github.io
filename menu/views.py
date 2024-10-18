from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .modelo import Plato, Reserva

class MenuView(ListView):
    model = Plato
    template_name = 'menu/menu.html'

class ReservaCreateView(CreateView):
    model = Reserva
    fields = ['nombre', 'fecha', 'personas']
    template_name = 'menu/reserva.html'
    success_url = reverse_lazy('menu')
