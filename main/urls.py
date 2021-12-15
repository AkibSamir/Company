from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonials, name='testimonial'),
    path('service/', views.services, name='service'),
    path('portfolios/', views.portfolio, name='portfolios'),
    path('portfolio-detail/<str:pk>/', views.portfolio_detail, name='portfolio-detail'),
    path('pricing/', views.pricing, name='pricing'),
    path('blog/', views.blog, name='blog'),
    path('blog-single/', views.blog_single, name='blog-single'),
    path('contact/', views.contact, name='contact'),
]