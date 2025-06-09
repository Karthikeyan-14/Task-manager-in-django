from django.shortcuts import render,redirect,get_object_or_404
from .models import reg,task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#function for redirect to registration page in start
@csrf_exempt
def start(request):
    return render(request,'reg.html')

#function for redirect to registration page
@csrf_exempt
def go_reg(request):
    return render(request,'reg.html')

#function for redirect to login page
@csrf_exempt
def go_log(request):
    return render(request,'login.html')

#function for redirect to dashboard page 
@csrf_exempt
def go_dash(request):
    # get the specific tasks of the user by filter by primary key of user and foreign key of task 
    task1=task.objects.filter(id_user_id=user_id)
    # redirect to dashboard by the user id and task
    return render(request,'dashboard.html',{'email':res_mail,'user':user_id,'tasks':task1})

# function used for register
@csrf_exempt
def register(request):
    # by using post method get data from the form
    if request.method=='POST':
        email=request.POST.get('regmail')
        password=request.POST.get('regpass')
        # check if the entered user is already registered or not if not registered save the details
        if not reg.objects.filter(reg_mail=email).exists():
            #save the rgistered details in table by the class name reg 
            user=reg(reg_mail=email,reg_pass=password)
            user.save()
            return render(request,'login.html')     
    return render(request,'reg.html')

# function used for login
@csrf_exempt
def login(request):
    #set the global variable 
    global user_id,res_mail,task1
     # by using post method get data from the form
    if request.method=='POST':
        email=request.POST.get('logmail')
        password=request.POST.get('logpass')
        # check if the user is already registered or not 
        if reg.objects.filter(reg_mail=email).exists():
            # take the name from the email before @
            res_mail=email.split('@')[0]
            print(res_mail)
            # take the user id by filter 
            temp_id=reg.objects.filter(reg_mail=email,reg_pass=password)
            for i in temp_id:
            # take the specific id and store it in variable
                user_id=i.id
                print(user_id)
                # filtering the user specific task by their user id
            task1=task.objects.filter(id_user_id=user_id)
            tasks_d = task.objects.all()
    
            context={
                "task_ud":task1,
                "email":res_mail

            }
         # redirect to dashboard by the user id and task
            return render(request,'dashboard.html',context)

    return render(request,'login.html')
@csrf_exempt
def task_save(request):
     # by using post method get data from the form
    if request.method=='POST':
        taskid=request.POST.get('task_id')
        tasks=request.POST.get('task_nid')
        des=request.POST.get('task_did')
        dates=request.POST.get('task_ddid')
        print(dates)
        print(taskid)
        print(user_id)

        # after getting the values from the form save the data in the table by the model(class) name
        #if condition is for create new task
        if taskid=="":
            use=task(task_data=tasks,description_data=des,date_data=dates,id_user_id=user_id)
            print(use)
        #else part is for updating the task
        else:
            """use=get_object_or_404(task,id=taskid)
            use.task_data
            use.description_data
            use.date_data"""
            print("good")
            use=task(id=taskid,task_data=tasks,description_data=des,date_data=dates,id_user_id=user_id)
            print(use)
            



        use.save()
        
        #send the updated tasks to the dashboard
        #task2=task.objects.filter(id_user_id=user_id)
        #print(task2)
        #task1=task.objects.values(id_user_id=user_id)
        
       # task_val=task.objects.values()
        #task_data=list(task1)

        #return the task data as list

        task_data = list(task.objects.filter(id_user_id=user_id).values())

        #return as jsonresponse

        return JsonResponse({"status":"Saved","task_data":task_data})
    else:
        return JsonResponse({"status":"Not Saved"})
         # redirect to dashboard by the user id and task
        #return render(request,'dashboard.html',{'email':res_mail,'user':user_id,'tasks':task2})
   # return render(request,'dashboard.html',{'email':res_mail,'user':user_id,'tasks':task1})

@csrf_exempt
def delete(request):
    # get the specific task of te user
    #task3=get_object_or_404(task,id=pk)
    if request.method=='POST':
        # delete the filtered specific task
        temp_id=request.POST.get("sid")
        id=temp_id.strip(",/'")
        print(id)
        print(temp_id)

        task_del=task.objects.get(pk=id)
        task_del.delete()

        #send the updated tasks as jsonresponse

        return JsonResponse({"status":"1"})
        #return render(request,'dashboard.html',{'email':res_mail,'user':user_id,'tasks':task5})
    else:
        return JsonResponse({"status":"0"})
        
@csrf_exempt
def update(request):
    print("Ajax")
    # get the task details
    #task6=get_object_or_404(task,id=pk)
    if request.method=="POST":
        print("hello")
        # get the value to be updated datas from forms
        id=request.POST.get("tid")

        task_d=task.objects.get(pk=id)

        datas={
            "id":task_d.pk,
            "task":task_d.task_data,
            "des":task_d.description_data,
            "date":task_d.date_data
        }
        print(datas)

        #task6=task.objects.get(pk=id)

        """task_name=request.POST.get('task_name')
        task_des=request.POST.get('task_desc')
        task_dates=request.POST.get('task_date')
        # rewrite the value of the tasks
        task6.task_data=task_name
        task6.description_data=task_des
        task6.date_data=task_dates
        # save the task of the data
        task6.save()       
        #send the updated tasks to the dashboard
        task5=task.objects.filter(id_user_id=user_id)"""

        return JsonResponse({"status":"success","task_datas":datas})
    else:
        return JsonResponse({"status":"fail"})
        #return render(request,'dashboard.html',{'email':res_mail,'user':user_id,'tasks':task5})
    #return render(request,'update.html',{'task':task6})
    