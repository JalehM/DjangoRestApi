from django.conf.urls import url, include
from . import views
from django.urls import path
urlpatterns = [
    path('api/tutorials', views.tutorial_list),
    path('api/tutorials/published', views.tutorial_detail),
    path('Post /tutorials', views.tutorial_detail),

    #path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),

]
