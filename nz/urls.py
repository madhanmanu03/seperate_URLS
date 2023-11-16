from nz.views import *
from django.urls import path
app_name="nz"

urlpatterns=[
    path('kane/',kane,name='kane'),
    path('convae/',convae,name='convae'),

]  