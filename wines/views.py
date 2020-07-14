from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import WineForm
from .models import Wine
from .serializers import WineSerializer
import json


def wine_list(request):
    wines = Wine.objects.all()
    serialized_wines = WineSerializer(wines).all_wines
    return JsonResponse(data=serialized_wines, status=200)


def wine_detail(request, wine_id):
    wine = Wine.objects.get(id=wine_id)
    serialized_wine = WineSerializer(wine).wine_detail
    return JsonResponse(data=serialized_wine, status=200)


@csrf_exempt
def new_wine(request):
    data = json.load(request)
    if request.method == "POST":
        form = WineForm(data)
        if form.is_valid():
            wine = form.save(commit=True)
            serialized_wine = WineSerializer(wine).wine_detail
            return JsonResponse(data=serialized_wine, status=201)
        else:
            return JsonResponse(data={'error': 'Wine not created'}, status=400)


@csrf_exempt
def edit_wine(request, wine_id):
    wine = Wine.objects.get(id=wine_id)
    if request.method == "PUT":
        data = json.load(request)
        form = WineForm(data, instance=wine)
        if form.is_valid():
            wine = form.save(commit=True)
            serialized_wine = WineSerializer(wine).wine_detail
            return JsonResponse(data=serialized_wine, status=200)
        else:
            return JsonResponse(data={'error': 'Wine not updated'}, status=400)


@csrf_exempt
def delete_wine(request, wine_id):
    if request.method == "DELETE":
        wine = Wine.objects.get(id=wine_id)
        wine.delete()
        return JsonResponse(data={
            'status': 'Successfully deleted wine.'}, status=200)
    else:
        return JsonResponse(data={'status': 'Not deleted'}, status=405)
