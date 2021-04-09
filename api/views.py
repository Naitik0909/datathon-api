from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .f1_score_evaluation import getF1
# Create your views here.

def handle_uploaded_file(f):
    with open('media/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def handleFile(request, filename):
    file = request.FILES["file"]
    destination = open(f'media/{filename}', 'wb')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()


@csrf_exempt
def my_api(request):
    if request.method == "POST":
        data = request.FILES
        filename = request.FILES["file"].name
        handleFile(request, filename)
        score = getF1(request.FILES["file"].name)

        return JsonResponse({'score': score})
    else:
        return HttpResponse('404')
