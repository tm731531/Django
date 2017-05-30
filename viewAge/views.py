from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.http import HttpResponse,JsonResponse
from datetime import datetime
from django.shortcuts import render
from django.conf import settings
from django import forms 
from django.core.mail import send_mail
from django.contrib import auth

#from django.utils import simplejson
import pymssql
import json
# Create your views here.
#def hello_world(request):
#    return HttpResponse("Hello World!")
class UserForm(forms.Form):
    name=forms.CharField(label='Your name', max_length=100) 
    password=forms.CharField(label='Your password', max_length=100) 
    Email=forms.EmailField(label='Your Email', max_length=100) 
    Url=forms.URLField(label='Your Url', max_length=100) 
    Integer=forms.IntegerField(label='Your Integer') 
    Float=forms.FloatField (label='Your Float') 
    Boolean=forms.BooleanField (label='Your Boolean') 
   
    #password2=forms.EmailField(label='Your password3', max_length=100) 

def hello_world(request):
    conn = pymssql.connect(settings.APP_SETTING["serverconfig"], settings.APP_SETTING["userconfig"], settings.APP_SETTING["passwordconfig"], settings.APP_SETTING["dbconfig"])
    cursor = conn.cursor()
    cursor.execute("  select  *   FROM [Farmdata].[dbo].[patentFSecure] " )

    row=cursor.fetchall()
    data=[]
    for x in row:
        data.append({'title':x[1]})
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
        'rowdata': data,
    })

def viewpage(request):
    
    conn = pymssql.connect(settings.APP_SETTING["serverconfig"], settings.APP_SETTING["userconfig"], settings.APP_SETTING["passwordconfig"], settings.APP_SETTING["dbconfig"])
    cursor = conn.cursor()
    cursor.execute("  select  *   FROM [Farmdata].[dbo].[patentFSecure] " )
    row=cursor.fetchall()
    data=[]
    for x in row:
        data.append({'title':x[1],'pub_date': datetime.now(),'body':x[3]})
    return render(request, 'index.html', {
        'now': str(datetime.now()),
        'posts': data,
    })

def viewpageConfig(request):
    #server = getattr(settings, "serverconfig", None)
    #user = getattr(settings, "userconfig", None)
    #password = getattr(settings, "passwordconfig", None)
    #data = getattr(settings, "dbconfig", None)
    server= settings.APP_SETTING["serverconfig"]
    user= settings.APP_SETTING["userconfig"]
    password= settings.APP_SETTING["passwordconfig"]
    data= settings.APP_SETTING["dbconfig"]
    return render(request, 'viewpageConfig.html', {
        'server': server,
        'user': user,
        'password': password,
        'data': data,
    })
    
def login(request):
    
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    
    if username is not None and username=='1':
        #auth.login(request, user)
        return HttpResponseRedirect('/hello/')
    else:
        return render_to_response('login.html') 
    """
    conn = pymssql.connect(settings.APP_SETTING["serverconfig"], settings.APP_SETTING["userconfig"], settings.APP_SETTING["passwordconfig"], settings.APP_SETTING["dbconfig"])
    cursor = conn.cursor()
    cursor.execute("  select  *   FROM [Farmdata].[dbo].[patentFSecure] " )
    row=cursor.fetchall()
    data=[]
    for x in row:
        data.append({'title':x[1],'pub_date': datetime.now(),'body':x[3]})
    return render(request, 'index.html', {
        'now': str(datetime.now()),
        'posts': data,
    })
    """

def form(request):
    if request.method == "POST":
        form = UserForm(request.POST)                     
        if form.is_valid():
             
            user = auth.authenticate(username=form.cleaned_data['name'], password=form.cleaned_data['password'])

            if user is not None and user.is_active:
                auth.login(request, user)
                subject = form.cleaned_data['name']
                message = form.cleaned_data['password']
                sender = form.cleaned_data['Email']
                cc_myself = form.cleaned_data['Email']

                recipients = ['tom_ting@trend.com.tw']
            #if cc_myself:
            #    recipients.append(sender)

                send_mail(subject, message, sender, recipients)
            print (form.cleaned_data)
            return HttpResponse('ok')
    else:
        if request.user is not None and str(request.user)=="AnonymousUser":
            form = UserForm()
        else :
            return HttpResponse(str(request.user)) 
    return render_to_response('form.html',{'form':form,})



def D3stockSource(request,data):
    print(data)
    conn = pymssql.connect(settings.APP_SETTING["serverconfig"], settings.APP_SETTING["userconfig"], settings.APP_SETTING["passwordconfig"], settings.APP_SETTING["dbconfig"])
    cursor = conn.cursor()
    if data.lower().upper()=="ALL":
        cursor.execute("  select  *   FROM [D3mbostocksource] ")
    else :
        cursor.execute("  select  *   FROM [D3mbostocksource] where type ='%s'"  %data)
    row=cursor.fetchall()
    sourcedata=[]

    for cols in row:
        arrays={}
        for i in range(len(cursor.description)):
            desc = cursor.description[i][0]
            arrays[desc] = cols[i]
        sourcedata.append(arrays)
    #print(sourcedata)
    return render(request, 'D3//stockSource.html',{'sourcedata':sourcedata})

    
