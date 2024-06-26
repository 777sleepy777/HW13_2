
from django.urls import path
from  . import views

app_name = 'quotes'

urlpatterns = [
    path("", views.main, name='main'),
    path("<int:page>", views.main, name='root_paginate'),
    path('author/<str:author_id>', views.author, name='author'),
    path('tag/', views.add_tag, name='add_tag'),
    path('note/', views.add_quote, name='add_quote'),
    path('add_author/', views.add_author, name='add_author'),

]
