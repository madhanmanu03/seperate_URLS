from ind.views import *
from django.urls import path
app_name="ind"

urlpatterns=[
    path('virat/',virat,name='virat'),
    path('shresh/',shresh,name='shresh'),

]