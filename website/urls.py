
from django.urls import path
from website.views import home, about

urlpatterns = [

    path('', home),
    path('about/' , about)
]
