
from django.urls import path
from weatherapp.views import index


urlpatterns = [

    path('sunny/', view=index,name='index'),
]