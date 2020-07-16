from django.shortcuts import render,redirect
from .models import Task
from django.http import HttpResponse
import pdb

# Create your views here.
import datetime

def call_at_create(start,end):
    # pdb.set_trace()
    start=start.split(':')
    sh,sm,ss=int(start[0]),int(start[1]),int(start[2])
    end=end.split(':')
    eh,em,es=int(end[0]),int(end[1]),int(end[2])
    x = datetime.datetime.now()
    ch,cm,cs=int(x.strftime("%H")),int(x.strftime("%M")),int(x.strftime("%S"))
    status=''
    if ch < sh:
        status=("{}:{}:{}".format(sh,sm,ss))
    elif ch > eh:
        status=('False')
    elif ch > sh and ch < eh:
        status=('True')
    elif ch == sh:
        if ch == sh and cm < sm:
            status=("{}:{}:{}".format(sh, sm, ss))
        elif (ch == sh and cm == sm):
            if (cs < ss) :
                status=("{}:{}:{}".format(sh, sm, ss))
            else:
                status=('True')
        elif (ch == sh and cm > sm) and (ch < eh):
            status = ('True')

        elif (ch == sh and ch == eh):
            if cm > em:
                status=('False')
            elif cm < em:
                status=('True')
            elif cm == em:
                if cs < es:
                    status=('True')
                else:
                    status=('False')
    elif ch == eh:
        if ch == eh and cm < em:
            status=("{}:{}:{}".format(sh, sm, ss))
        elif (ch == eh and cm == em):
            if (cs < es) :
                status=("{}:{}:{}".format(sh, sm, ss))
            else:
                status=('False')
        else:
            status = ('False')

    return status


def enhanced_call_at_create(stime,etime,sday,eday):
    # pdb.set_trace()
    x = datetime.datetime.now()
    cwd = int(x.strftime("%w"))
    dict_day_to_digit = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5,
                         'Saturday': 6}
    day1 = sday.capitalize()
    day2 = eday.capitalize()
    swd = int(dict_day_to_digit[day1])
    ewd = int(dict_day_to_digit[day2])
    status=''
    if cwd < swd or cwd > ewd:
        status=day1+' '+str(stime)
    elif cwd > swd and cwd < ewd:
        status=day2+' '+str(stime)
    elif cwd == swd:
        output=call_at_create(str(stime),str(etime))
        if output != 'True' and output != 'False':
            status= status=day1+' '+str(stime)
        else:
            status=output
    elif cwd== ewd:
        output=call_at_create(str(stime),str(etime))
        if output != 'True' and output != 'False':
            status= status=day2+' '+str(stime)
        else:
            status=output

    return status


def home(request):
    return render(request,'home.html')


def Create_Task(request):
    if request.method == 'POST':
        # pdb.set_trace()
        task_type= request.POST.get("task_type", "")
        user = request.POST.get("user", "")
        country = request.POST.get("country", "")
        start_time = str(request.POST.get("start_time", ""))
        end_time = str(request.POST.get("end_time", ""))
        start_day= request.POST.get("start_day", "")
        end_day = request.POST.get("end_day", "")
        status=''
        if start_day and end_day:
            try:
                # pdb.set_trace()
                task=Task(task_type=task_type,user=user,country=country,start_time=start_time,end_time=end_time,start_day=start_day,end_day=end_day)
                task.save()
                status=enhanced_call_at_create(start_time,end_time,start_day,end_day)
                print(status)
            except:
                print('Please provide unique combination of Task, User and Country')
                return HttpResponse('<h1> Please provide unique combination of Task, User and Country</h1>')
            return render(request,'Output.html',{'status':status})
        else:
            try:
                task = Task(task_type=task_type, user=user, country=country, start_time=start_time, end_time=end_time)
                task.save()
                status = call_at_create((start_time), (end_time))
                print(status)
            except:
                print('Please provide unique combination of Task, User and Country')
                return HttpResponse('<h1> Please provide unique combination of Task, User and Country</h1>')
            return render(request,'Output.html', {'status':status})
            # return redirect()


    return render(request,'Create_task.html')
def Config_Task(request):
    task=Task.objects.all()
    return render(request,'data_list_conf.html',{'task':task})

def Update_task_Time(request,id):
    # pdb.set_trace()
    task=Task.objects.get(id=id)
    start_time=(task.start_time).strftime("%X")
    end_time=(task.end_time).strftime("%X")
    start_day=task.start_day
    end_day=task.end_day
    if request.method == 'POST':
        task.start_time = str(request.POST.get("start_time", ""))
        task.end_time = str(request.POST.get("end_time", ""))
        task.start_day = request.POST.get("start_day", "")
        task.end_day = request.POST.get("end_day", "")
        task.save()
        task=Task.objects.all()
        return render(request,'data_list_conf.html',{'task':task})
    return render(request,'config_time.html',{'start_time':start_time,'end_time':end_time,'start_day':start_day,'end_day':end_day})



