from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def my_api(request):
    if request.method == "POST":
        data = request.POST
        print(data.get('Data'))

        return JsonResponse({'foo': 'bar'})
    else:
        return HttpResponse('Works')
