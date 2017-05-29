from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.conf import settings
import pymssql
# Create your views here.
#def hello_world(request):
#    return HttpResponse("Hello World!")
 
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
    
