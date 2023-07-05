from django.shortcuts import render
from Meals.models import Food
from django.http import JsonResponse
import urllib.parse 
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Meals.models import Food
from Meals.serializers import FoodSerializer
import requests
import json

def Search(request):
    query = request.GET.get('q', '')
    results = Food.objects.filter(Q(items__icontains=query) | Q(name__icontains=query)).values('items')
    all_dishes = []
    for result in results:
        items_data = json.loads(result['items'])
        for dish_name, dish_price in items_data.items():
            all_dishes.append((dish_name, dish_price))
    
    total_count = len(all_dishes)
    half_count = total_count // 2

    first_half = all_dishes[:half_count]
    second_half = all_dishes[half_count:]

    context = {
        'query': query,
        'first_half': first_half,
        'second_half': second_half,
    }
    return render(request, 'search.html', context)

def search_view(request):
    query = request.GET.get('q', '')

    results = Food.objects.filter(Q(items__icontains=query) | Q(name__icontains=query)).values('items')

    exact_results = {}
    related_results = []
    for result in results:
        items_data = json.loads(result['items'])
        for dish_name, dish_price in items_data.items():
            if query.lower() == dish_name.lower():
                exact_results[dish_name] = dish_price
            elif query.lower() in dish_name.lower():
                related_results.append((dish_name, dish_price))

    context = {
        'query': query,
        'exact_results': exact_results,
        'related_results': related_results,
    }

    return render(request, 'index.html', context)
