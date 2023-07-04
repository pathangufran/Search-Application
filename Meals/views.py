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

    # Filter dishes based on query
    results = Food.objects.filter(Q(items__icontains=query) | Q(name__icontains=query)).values('items')
    all_results = []
    for result in results:
        items_data = json.loads(result['items'])
        for dish_name in items_data.keys(): 
            all_results.append(dish_name)

    context = {
        'query': query,
        'all_results': all_results,
    }

    return render(request, 'search.html', context)

def search_view(request):
    query = request.GET.get('q', '')

    # Filter dishes based on query
    results = Food.objects.filter(Q(items__icontains=query) | Q(name__icontains=query)).values('items')

    exact_results = set()
    related_results = []
    for result in results:
        items_data = json.loads(result['items'])
        for dish_name in items_data.keys(): 
            if query.lower() == dish_name.lower():
                exact_results.add(dish_name)
            elif query.lower() in dish_name.lower():
                related_results.append(dish_name)

    context = {
        'query': query,
        'exact_results': exact_results,
        'related_results': related_results,
    }

    return render(request, 'index.html', context)

















    # if 'q' in request.GET:
    #     query = request.GET['q']
    #     results = Food.objects.filter(name__icontains=query)
    #     best_match = results.first() if results.exists() else None
    # else:
    #     query = ''
    #     results = []
    #     best_match = None
    
    # context = {
    #     'query': query,
    #     'results': results,
    #     'best_match': best_match
    # }

    # return render(request, 'search.html', context)



    # query = request.GET.get('q')
    # if query:
    #     # Perform a case-insensitive search for dishes that contain the query string
    #     results = Food.objects.filter(name__icontains=query)
        
    #     # Retrieve recommendations using the recommendations API endpoint
    #     query_encoded = urllib.parse.quote_plus(query)
    #     response = requests.get(f'http://localhost:8000/dish/recommendations/{query_encoded}/')
    #     try:
    #         recommendations = response.json()
    #     except json.JSONDecodeError as e:
    #         print(f"Error decoding JSON: {str(e)}")
    #         recommendations = []
    
    # return render(request, 'search.html', {'results': results, 'query': query, 'recommendations': recommendations})