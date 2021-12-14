
from django.urls import path 
from .views import pub_post_list , unpub_post_list
urlpatterns = [
    path('published/' , pub_post_list),
    path('unpublished/' , unpub_post_list),
]
