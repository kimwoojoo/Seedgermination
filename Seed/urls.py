from django.urls import path
from . import views
from mysite.settings import MEDIA_ROOT
urlpatterns = [
    path('',views.ImageUpload, name='ImageUpload'),
    path('GetJsonData', views.GetJsonData, name='GetJsonData'),
    #path('', views.ImageView ,name='ImageView'),
]