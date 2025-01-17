from django.urls import path
from .views import *


urlpatterns = [
    path('', ParserView.as_view(), name='parser_url'),
    path('body/<str:slug>', BodyView.as_view(), name='post_body_url'),
]