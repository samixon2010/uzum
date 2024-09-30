from django.shortcuts import render, redirect   
from .models import Phone, PhoneForm

# Create your views here.

def Form(request):
    form = PhoneForm()
    if request.POST:
        form = PhoneForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'form.html', {"form": form})

def detail(request,id):

    d = Phone.objects.get(id=id)

    return render(request, 'detail.html', {'i': d})

    
def nmadur(request, id):
    a = {
        # "phones" : Phone.objects.filter(name='macbook', narxi__gte=1200)
        # "phones" : Phone.objects.filter(name='iphone 13 pro max', narxi__lte=900)
        'i' : Phone.objects.get(id=id)
    }
    return render(request, 'nmadur.html', a)
def home(request):
    d = {
        'phones': Phone.objects.all()
    }
    print(Phone.objects.all())
    return render(request, 'home.html', d)


def index(request):
    # print(dir(request))
    if request.POST:
        Phone.objects.create( 
            name=request.POST['name'],
            narxi = request.POST['narxi'],
            rangi = request.POST['rangi'],
            holati = request.POST['holati'],
            xotira = request.POST['xotira'],
            rasm = request.FILES['rasm']
        )
        return redirect('home')
    return render(request, 'index.html')