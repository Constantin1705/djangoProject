from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return HttpResponse('<h1>Hello, Iulian</h1>')


def show_details_students(request):
    details_students = {
        'all_students': [
            {
                'first_name': 'George',
                'last_name': 'Popescu',
                'age': 30,
                'is_olympic': False
            },
            {
                'first_name': 'Nicoleta',
                'last_name': 'Luchian',
                'age': 35,
                'is_olympic': True
            },
            {
                'first_name': 'Razvan',
                'last_name': 'Zamfir',
                'age': 34,
                'is_olympic': True
            }
        ]
    }

    return render(request, 'home/details_students.html', details_students)


def show_details_cars(requests):
    details_cars = {
        'all_cars': [
            {
                'brand_name': 'BMW',
                'model_name': 'M',
                'horse_power': 480,
                'year': 2022
            },
            {
                'brand_name': 'Tesla',
                'model_name': '3',
                'horse_power': 325,
                'year': 2021
            },
            {
                'brand_name': 'Ford',
                'model_name': 'Fusion',
                'horse_power': 197,
                'year': 2021
            }
        ]
    }

    return render(requests, 'home/details_cars.html', details_cars)


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'
