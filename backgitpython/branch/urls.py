from django.urls import path
from .views import *

app_name = 'branch'

urlpatterns = [
    path('/', Branches_APIView.as_view()),
]