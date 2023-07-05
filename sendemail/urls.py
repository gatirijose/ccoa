from django.urls import path
from .views import contact_view


app_name = 'send_to'
urlpatterns = [
    path('contact/', contact_view, name='contact'),
]
