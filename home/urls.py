from django.urls import path

from home import views

urlpatterns = [
    path('first_page/', views.index, name='index'),
    path('details_students/', views.show_details_students, name='details'),
    path('details_cars/', views.show_details_cars, name="cars"),

    path('', views.HomeTemplateView.as_view(), name='home')
]
