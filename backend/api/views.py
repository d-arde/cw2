from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import CarBrand

@csrf_exempt
def requestHandler(request, brand_id=None):
    if request.method =='GET':
        if brand_id is not None:
            return displayBrand(request,brand_id)
        else:
            return displayData()
    if request.method =='POST':
        details = json.loads(request.body)
        brand = CarBrand(brand_name=details['name'],date_founded=details['date'],email=details['email'],revenue=details['revenue'])
        print(details)
        brand.save()
        return displayData()
    if request.method == 'PUT':
        updateBrand(request, brand_id)
        return displayData()
    if request.method == 'DELETE':
        deleteBrand(request, brand_id)
        return displayData()


def displayData():
    brands = CarBrand.objects.all().values()
    brand_dict = {brand['id']: brand for brand in brands}
    
    return JsonResponse(brand_dict)

def displayBrand(request, brand_id):
    try:
        brand = get_object_or_404(CarBrand, pk=brand_id)
        brand_details = {
            "id": brand.id,
            "brand_name": brand.brand_name,
            "date_founded": brand.date_founded,
            "email": brand.email,
            "revenue": brand.revenue,
        }
        return JsonResponse(brand_details)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=404)  # Return a 404 response for not found



@csrf_exempt
def updateBrand(request, brand_id):
    try:
        put = json.loads(request.body)
        brand_to_change = CarBrand.objects.get(id=brand_id)

        brand_to_change.brand_name = put.get("brand_name", brand_to_change.brand_name)
        brand_to_change.date_founded = put.get("date_founded", brand_to_change.date_founded)
        brand_to_change.email = put.get("email", brand_to_change.email)
        brand_to_change.revenue = put.get("revenue", brand_to_change.revenue)
        
        brand_to_change.save()
        return JsonResponse({"message": "Brand updated successfully"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)



@csrf_exempt
def deleteBrand(request, brand_id):
    try:
        # Attempt to get the brand by its ID, or return a 404 if it doesn't exist
        brand = CarBrand.objects.get(id=brand_id)
        brand.delete()
        return HttpResponse(statu=204)
    except CarBrand.DoesNotExist:
        return HttpResponse("Brand not found", status=404) 
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

