"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from adresboek.admin import adresboek_admin_site

urlpatterns = [
    # Beheer django
    path('systeem/', admin.site.urls),
    # Beheer adresboek
    path('adressen/beheer/', adresboek_admin_site.urls),
    url(r'^', include('adresboek.urls')),
    # Accounts
    url(r'^', include('accounts.urls')),
    # Static Pages
    url(r'^missie', TemplateView.as_view(template_name='pages/missie.html'), name='missie'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'Ambon-Diaspora Beheersysteem'
admin.site.site_title = 'Ambon-Diaspora Beheersysteem'
admin.site.index_title = 'Welkom Ambon-Diaspora in het Beheersysteem'
