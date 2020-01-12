from django.shortcuts import render

# Create your views here.
def manal(request):
    context = {
        "msg": "Hello World!",
        "hello":1
    }
    return render(request, 'manal.html', context)