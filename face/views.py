from django.shortcuts import render
from .models import Question, Unknown
# Create your views here.
from django.http import HttpResponse
import face_recognition
import os


def index(request):
    return render(request,"face/missing.html")

def updated(request):
    if request.method== 'POST':
        your_name=request.POST.get('name')
        your_age=request.POST.get('age')
        your_address=request.POST.get('address')
        your_contact=request.POST.get('contact_no')
        your_img=request.POST.get('img')
        var_img = Question(name=your_name, age=your_age, address=your_address, Contact_no=your_contact, image=your_img)
        var_img.save()

    return render(request,"face/updated.html")    

def result(request):
    if request.method== 'POST':
        img=request.POST.get('img')
        var_img = Unknown(image=img)
        var_img.save()

        unknown_image_list = []
        basepath = './missing_faces/Unknown'
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                unknown_image_list.append(entry)

        image_of_bill = face_recognition.load_image_file('./missing_faces/Unknown/'+unknown_image_list[-1])  
        bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

        known_image_list = []
        basepath = './missing_faces/Known'
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                known_image_list.append(entry)
                   

        #lst=Question.objects.all()
        for image in range(len(known_image_list)):
            unknown_image = face_recognition.load_image_file('./missing_faces/Known/'+known_image_list[0]) 
            unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
            results = face_recognition.compare_faces([bill_face_encoding], unknown_face_encoding)
            matched_name=known_image_list[0]
            
            if results[0]:
                #stri=Question.objects.filter(name=matched_name)
                return render(request, 'face/matched_person.html', {'names': known_image_list[0]})
                break
            else:
                known_image_list.remove(known_image_list[0])
        return render(request,'face/result.html')    