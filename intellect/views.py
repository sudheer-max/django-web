from django.shortcuts import render
from .models import Post, Profile, Hvac, Door, Equipment, Metal
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

def home(request):
    profile = Profile
    template = 'home.html'
    return render(request, template, { 'profile': Profile })

class metalView(ListView):
    model = Metal
    template_name = 'metal.html'

class metalDetailView(DetailView):
    model = Metal
    template_name = 'metalDetail.html'

def metalDetail(request):
    context = {}
    template = 'metalDetail.html'
    return render(request, template, context)

class equipmentView(ListView):
    model = Equipment
    template_name = 'equipment.html'

class equipmentDetailView(DetailView):
    model = Equipment
    template_name = 'equipmentDetail.html'

def equipmentDetail(request):
    context = {}
    template = 'equipmentDetail.html'
    return render(request, template, context)

class doorView(ListView):
    model = Door
    template_name = 'door.html'

class doorDetailView(DetailView):
    model = Door
    template_name = 'doorDetail.html'

def doorDetail(request):
    context = {}
    template = 'doorDetail.html'
    return render(request, template, context)

class hvacView(ListView):
    model = Hvac
    template_name = 'hvac.html'

class hvacDetailView(DetailView):
    model = Hvac
    template_name = 'hvacDetail.html'

def hvacDetail(request):
    context = {}
    template = 'hvacDetail.html'
    return render(request, template, context)

def product(request):
    context = {}
    template = 'product.html'
    return render(request, template, context)

class homeView(ListView):
    model = Post
    template_name = 'home.html'



class postDetailView(DetailView):
    model = Post
    template_name = 'product.html'




