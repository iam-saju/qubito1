#threading
from django.conf import settings
import time
from django.contrib import messages
import threading
from django.shortcuts import render,redirect,HttpResponse
from .forms import UploadFileForm,ChatForm
from django.conf import settings
from .tl_utility import send_file_to_telegram,check_chat_id
import json
import time
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

threads = []
count=0

def login(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            phno = form.cleaned_data['phno']
            status = check_chat_id(phno)
            if status == True:
                messages.success(request, "Chat ID is valid!")
                return redirect('upload')
            else:
                messages.error(request, "❌ Invalid Chat ID or user hasn't started the bot.")
                # Missing return statement here - this causes the error
                return render(request, 'success.html', {'form': form})
    else:
        form = ChatForm()
    
    return render(request, 'success.html', {'form': form})


def login_page(request):
    print(settings.key)
    return render(request, 'tl.html')
    

def thread1(file,file_name):
    thread= threading.Thread(target=upload_file, args=(file, f"{file_name}"))
    thread.start()
    print(file_name+"is in thread1 ")
    return thread

def thread2(file,file_name):
    thread= threading.Thread(target=upload_file, args=(file, f"{file_name}"))
    thread.start()
    print(file_name+"is in thread2 ")
    return thread

def thread3(file,file_name):
    thread= threading.Thread(target=upload_file, args=(file, f"{file_name}"))
    thread.start()
    print(file_name+"is in thread3 ")
    return thread

# Create a thread pool for parallel uploads
def upload_file(file, message):
    response=send_file_to_telegram(file, file.name, message=message)
     # Debugging


def upload(request):
    message = None
    error = None
 
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_files = request.FILES.getlist('file_field') 
            length=len(uploaded_files)
            
            threads = []

            start=time.perf_counter()
            for f in range(0,length,3):
                t1=thread1(uploaded_files[f],uploaded_files[f].name)
                threads.append(t1)

                if f+1<length:
                    t2=thread2(uploaded_files[f+1],uploaded_files[f+1].name)
                    threads.append(t2)

                    if f+2<length:
                        t3=thread3(uploaded_files[f+1],uploaded_files[f+1].name)
                        threads.append(t3)

            for t in threads:
                t.join()
            end=time.perf_counter()

            duration = end - start
            total_size=sum(f.size for f in uploaded_files)
            total_size=(total_size/1024)/1000
            speed = (total_size / duration )
            
    
            
            message = "Files uploaded successfully!"
            print(f'{message} of size : {total_size:.2f} mb  completed in  {duration:.2f} seconds @ {speed:.2f} mbps')

        else:
            error = "Invalid form submission."

    else:
        form = UploadFileForm()

    return render(request, 'hi.html', {
        'form': form,
        'message': message,
        'error': error
    })



# Replace this with your bot's API token




@csrf_exempt
def telegram_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("✅ Telegram Login Data:", data)
            return JsonResponse({"message": "Login Success", "user": data})
        except Exception as e:
            return JsonResponse({"error": "Invalid data"}, status=400)
    return JsonResponse({"error": "Only POST allowed"}, status=405)
