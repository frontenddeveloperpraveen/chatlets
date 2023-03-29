from django.shortcuts import render,redirect
from django.http.response import JsonResponse, HttpResponse
from .models import Room,Message
import csv,os
from django.conf import settings
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def Home(request):
    return render(request,"index.html")

def Chat(request):
    return render(request,"chat.html")

def Check_room(request):
    if 'create' in request.GET:
        #Room Creation
        room_id = request.GET['room_id']
        username = request.GET["username"]
        if Room.objects.filter(name=room_id).exists():
            return render(request, 'chat.html', {'message': "Room Already Exist", 'message2':""})
        else:
            creation = Room.objects.create(name=room_id, creater=username)
            creation.save()
            return redirect("/"+room_id+"/?username="+username) 
    elif "join" in request.GET:
        room_id = request.GET['room_id']
        username = request.GET["username"]
        if Room.objects.filter(name=room_id).exists():
            return redirect("/"+room_id+"/?username="+username)
        else:    
            return render(request, 'chat.html', {'message':"",'message2': "No Room Found"})

def Room_join(request,room):
    print(request.GET)
    username = request.GET.get('username')
    print("username 54654654654 : ",username)
    print(username,room)
    return render(request,"message.html",{
        "user":username,
        "room":room,
    })

def Send(request):
    print("Recieveing")
    print(request)
    username = request.POST['username']
    room = request.POST["room_id"]
    message = request.POST['message']
    entry = Message.objects.create(msg=message,room=room,sender=username)
    entry.save()
    return HttpResponse('Message sent successfully')
def message(request,room):
    print("Message Recieving")
    print(room)
    msg_list = Message.objects.filter(room=room)
    return JsonResponse({"messages":list(msg_list.values())})

def Download2(request):
    room = request.GET["roomname"]
    info = Message.objects.filter(room=room)
    method = list(info.values())
    file_name = room+".csv"
    path= BASE_DIR+"\\static\\files\\"+file_name
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{path}"'   
    f = open(path,"w",newline="")
    fwriter = csv.writer(f)
    final = []
    for i in method:
        msg = i["msg"]
        sender = i["sender"]
        time = str(i['date'])
        time = time[:time.index(".")]
        final.append([msg,sender,time])
    fwriter.writerows(final)
    f.close()
    return response



def Download(request):
    room = request.GET["roomname"]
    info = Message.objects.filter(room=room)
    method = list(info.values())
    file_name = room + ".csv"
    path = os.path.join(settings.STATICFILES_DIRS[0], 'files', file_name)
    
    with open(path, "w", newline="") as f:
        fwriter = csv.writer(f)
        final = []
        fwriter.writerow(["Chatlets","Created by","Praveen"])
        fwriter.writerow(["Message","Sender","Time&Date"])
        for i in method:
            msg = i["msg"]
            sender = i["sender"]
            time = str(i['date'])
            time = time[:time.index(".")]
            final.append([msg, sender, time])
        fwriter.writerows(final)

    with open(path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{path}"'
        response['Content-Length'] = os.path.getsize(path)

    return response


def Page(request):
    return redirect("/home")
