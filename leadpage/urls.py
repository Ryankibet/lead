from django.urls import path
from . import views

app_name = 'leadpage'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('features/', views.features, name='features'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('testimonials/', views.testimonials, name='testimonials'),

    # CRUD routes
    path("messages/", views.contact_messages_list, name="messages_list"),
    path("messages/<int:pk>/edit/", views.contact_message_update, name="contact_message_update"),
    path("messages/<int:pk>/delete/", views.contact_message_delete, name="contact_message_delete"),
]
