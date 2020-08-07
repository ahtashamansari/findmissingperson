from django.shortcuts import render
from .models import Missing_Person
from django.conf import settings
from django.conf.urls.static import static
from .forms import OrderCreateForm
from django.http import HttpResponse
import face_recognition
import os
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request,"face/missing.html")

def updated(request):
    if request.method== 'POST':
        your_name=request.POST.get('name')
        your_age=request.POST.get('age')
        your_address=request.POST.get('address')
        your_contact=request.POST.get('contact_no')
        your_img=request.POST.get('img')
        your_image_name=request.POST.get('image_name')
        var_img = Missing_Person(name=your_name, age=your_age, address=your_address,
             Contact_no=your_contact, image=your_img,image_name=your_image_name)
        var_img.save()
        uploaded_file = request.FILES['img']
        fs = FileSystemStorage()
        name=fs.save(uploaded_file.name, uploaded_file)

    return render(request,"face/updated.html")    

def result(request):
    if request.method== 'POST':
        uploaded_file = request.FILES['img']
        uname=uploaded_file.name
        fs = FileSystemStorage()
        name=fs.save(uploaded_file.name, uploaded_file)
        url=fs.url(name)

        unknown_image = face_recognition.load_image_file('./media/'+uname) 
        unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]        
    
        known_image_list = []
        basepath = './media'
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                known_image_list.append(entry)       
        
        for image in known_image_list:
            if(image==uname):
                continue
            known_image = face_recognition.load_image_file('./media/'+image)  
            known_face_encoding = face_recognition.face_encodings(known_image)[0]
            results = face_recognition.compare_faces([known_face_encoding], unknown_face_encoding)
            if results[0]:
                fs.delete(uploaded_file.name)
                return render(request, 'face/matched_person.html', {'names': image})
                break
        fs.delete(uploaded_file.name)    
        return render(request,'face/result.html') 
