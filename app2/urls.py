from django.urls import path
from app2.views import *
app_name='anything'
urlpatterns=[
    path('app2_uday/',app2_uday,name='app2_uday')
]