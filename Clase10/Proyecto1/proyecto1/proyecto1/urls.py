from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('probandoTemplates/', views.probando_templates, name='probando_templates'),
]
