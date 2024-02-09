from django.urls import path
from . import views

app_name = "heatmap"


urlpatterns= [
 path("home/",views.home ,name = 'home'),
]