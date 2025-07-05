from django.shortcuts import render, HttpResponse
from .models import student
import datetime
def wish(request):
    time=datetime.datetime.now()
    hours=int(time.strftime("%H"))
    msg="hello user a very"
    if hours<12:
        msg+="good morning"
    elif hours<16:
        msg+="good afternoon"
    elif hours<22:
        msg+="good evening"
    else:
        msg+="good night"
    

    send={"msg1":msg, "time":time}
    return render(request,'index.html',context=send)
def std_data(request):
    students=student.objects.all()
    data={"students":students}
    return render(request, 'data.html',context=data)


# Create your views here.
