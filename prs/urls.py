from django.urls import path
from .views import *

app_name = 'prs'

urlpatterns = [
    path('prs', PullRequestAPIView.as_view()),
    path('prs/update-partial/<int:pk>/', PullRequestUpdatePartialAPIView.as_view()),
]