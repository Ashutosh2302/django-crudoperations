from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from django.urls import path
from crudApp import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('file/', views.files, name="files"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('add/',views.add, name="add"),
    path('edit/<int:id>',views.edit, name="edit"),
    url(r'^download/(?P<path>.*)$' , serve,{'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
