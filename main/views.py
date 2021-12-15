from django.shortcuts import render
from .models import Slider, About, Team, Skill, Client, Testomonial, Portfolio

# Create your views here.
def index(request):
    sliders = Slider.objects.all()
    aboutus = About.objects.all()
    clients = Client.objects.all()
    context = {
        'sliders':sliders,
        'about':aboutus,
        'clients':clients,
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    aboutus = About.objects.all()
    teams = Team.objects.all()
    skills = Skill.objects.all()
    clients = Client.objects.all()
    context = {
        'about':aboutus,
        'teams':teams,
        'skills':skills,
        'clients':clients,
    }
    return render(request, 'main/about.html', context=context)

def team(request):
    teams = Team.objects.all()
    context = {
        'teams':teams,
    }
    return render(request, 'main/team.html', context=context)

def testimonials(request):
    testimonial = Testomonial.objects.all()
    context = {
        'testimonial':testimonial,
    }
    return render(request, 'main/testimonials.html', context=context)

def services(request):
    return render(request, 'main/services.html')

def portfolio(request):
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios':portfolios,
    }
    return render(request, 'main/portfolio.html', context=context)

def portfolio_detail(request, pk):
    portfolios_detail = Portfolio.objects.get(id=pk)
    context = {
       'portfolios':portfolios_detail,
    }
    return render(request, 'main/portfolio-details.html', context=context)


def pricing(request):
    return render(request, 'main/pricing.html')

def blog(request):
    return render(request, 'main/blog.html')

def blog_single(request):
    return render(request, 'main/blog-single.html')

def contact(request):
    return render(request, 'main/contact.html')