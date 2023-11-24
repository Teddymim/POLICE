"""
URL configuration for police project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from my_app.views import index_view, criminal_view, offence_view, add_criminal_view, add_crime_view, add_casuality_view, add_witness_view, add_offence_view, edit_criminal_view,edit_offence_view, edit_crime_view, edit_casuality_view, edit_witness_view, delete_criminal_view, delete_crime_view, delete_casuality_view, delete_witness_view, delete_offence_view, sign_up_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index_page'),
    path('sign_up/', sign_up_view, name='sign_up_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('criminal_details', criminal_view, name='criminal_page'),
    path('offence_details', offence_view, name='offence_page'),
    

#add
    path('add_criminal/', add_criminal_view, name= 'add_criminal_page'),
    path('add_crime/', add_crime_view, name='add_crime_page'),
    path('add_casuality/', add_casuality_view, name= 'add_casuality_page'),
    path('add_witness/', add_witness_view, name= 'add_witness_page'),
    path('add_offence/', add_offence_view, name='add_offence_page'),
    

#edit
    path('edit_criminal/<int:criminal_id>/', edit_criminal_view, name='edit_criminal_page'),
    path('edit_crime/<int:crime_id>/', edit_crime_view, name="edit_crime_page"),
    path('edit_casuality/<int:casuality_id>/', edit_casuality_view, name='edit_casuality_page'),
    path('edit_witness/<int:witness_id>/', edit_witness_view, name='edit_witness_page'),
    path('edit_offence/<int:offence_id>/', edit_offence_view, name="edit_offence_page"),

#delete urls
    path('delete_criminal/<int:criminal_id>/', delete_criminal_view, name = "delete_criminal_page"),
    path('delete_crime/<int:crime_id>/', delete_crime_view, name = "delete_crime_page"),
    path('delete_casuality/<int:casuality_id>/', delete_casuality_view, name = "delete_casuality_page"),
    path('delete_witness/<int:witness_id>/', delete_witness_view, name = "delete_witness_page"),
    path('delete_offence/<int:offence_id>/', delete_offence_view, name = "delete_offence_page")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
