from app import views as app_wiews
from django.urls import path

urlpatterns = [
    path('view_b/', app_wiews.view_b, name='view b'),
    path('view_c/', app_wiews.view_c, name='view c'),
]
