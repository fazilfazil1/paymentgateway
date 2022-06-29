from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def checkout(request):
    return render(request, 'checkout.html')


def product(request):
    return render(request, 'product.html')


def results(request):
    num1 = request.POST['num1']
    num2 = request.POST['num2']
    result = num1 + num2
    return render(request, 'result.html', {'add': result})


def sampleform(request):
    return render(request, 'sampleform.html')
