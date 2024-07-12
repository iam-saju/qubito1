from django.shortcuts import render,redirect
from .forms import userform
# Create your views here.



def login(req):
    frm=userform()
    if req.method=='POST':
        print(req.POST.get('data'))


        return redirect('auth')
       
    return render(req,'login.html',{'frm':frm})

# telegram_auth/views.py


def home(request):
    if request.method == 'POST':
        print(request.POST.get('email'))


    # If the request method is not POST, render the form
    return render(request,'home.html')

def auth(req):
    if req.method=='POST':
        u=req.POST.get('input1')
        p=req.POST.get('input2')
        n=req.POST.get('input3')
        i=req.POST.get('input4')
        print(i,n,p,u)

    return render(req,'auth.html')





