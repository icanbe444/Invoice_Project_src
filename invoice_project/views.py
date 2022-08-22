from django.http import HttpResponse
from django.shortcuts import render
from invoices.models import Invoice

def main_page(request):
    obj = Invoice.objects.get(id=1)
    
    qs  = Invoice.objects.all()
    # print(obj.__dict__)
    # print("******************")
    # print(qs)
    # return HttpResponse('hello world')
    context = {
        'obj_': obj,
        'qs': qs

    }
    return render(request, 'home.html', context)