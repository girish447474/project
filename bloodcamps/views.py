from django.shortcuts import render
from django.http import HttpResponse
from bloodcamps.models import bloodcamp,bloodcampdonor
from bloodcamps.forms import newcamp
# Create your views here.
def index(request):
    return render(request,'bloodcamps/index.html')
def camphome(request):
    return render(request,'bloodcamps/camphome.html')
def history(request):
    camps=bloodcamp.objects.order_by('date')
    print('camps:',camps)
    content = {
        'camps' : camps
    }

    return render(request,'bloodcamps/history.html',context=content)
def upcoming(request):
    return render(request,'bloodcamps/upcoming.html')
def newcamppage(request):
    form=newcamp()
    if request.method=='POST':
        form=newcamp(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return camphome(request)
        else:
            print('form invalid')
    return render(request,'bloodcamps/newcamp.html',{'form':form})
