from django.shortcuts import render,HttpResponseRedirect
from . forms import UserRegister
from.models import User
# Create your views here.

def homep(request):
    if request.method == 'POST':
        fm = UserRegister(request.POST)
        if fm.is_valid():
            fm.save()
            print(request.FILES)
            return HttpResponseRedirect('/')
    else:
        fm = UserRegister()
        myusers = User.objects.all()
        return render(request,'home.html',{'form':fm,'myusers':myusers})

def updatedata(request,id):
    if request.method == 'POST':
        myid = User.objects.get(id=id)
        fm = UserRegister(request.POST,instance=myid)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        myid = User.objects.get(id=id)
        fm = UserRegister(instance=myid)
        return render(request,'update.html',{'fm':fm,'myid':myid})

def deletedata(request,id):
    deleteid = User.objects.get(id = id)
    deleteid.delete()
    return HttpResponseRedirect('/')
