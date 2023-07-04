from django.urls import path
from Meals import views
urlpatterns = [

    path('search',views.Search,name='search'),
    path('search_view',views.search_view,name='search_view'),

]