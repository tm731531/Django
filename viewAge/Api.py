from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from datetime import datetime
from django.shortcuts import render
from django.conf import settings
import pymssql
import json
# Create your views here.
#def hello_world(request):
#    return HttpResponse("Hello World!")
"""
def hello_world(request):
    conn = pymssql.connect(settings.APP_SETTING["serverconfig"], settings.APP_SETTING["userconfig"], settings.APP_SETTING["passwordconfig"], settings.APP_SETTING["dbconfig"])
    cursor = conn.cursor()
    cursor.execute("  select  *   FROM [patentFSecure] " )

    row=cursor.fetchall()
    data=[]
    for x in row:
        data.append({'title':x[1]})
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
        'rowdata': data,
    })
"""
def getdata(request,data):
    
    conn = pymssql.connect(settings.APP_SETTING["serverconfig"], settings.APP_SETTING["userconfig"], settings.APP_SETTING["passwordconfig"], settings.APP_SETTING["dbconfig"])
    cursor = conn.cursor()
    cursor.execute("  select  *   FROM [patentFSecure] where patentNo ='%s'"  %data)
    row=cursor.fetchall()
    data=[]

    for cols in row:
        arrays={}
        for i in range(len(cursor.description)):
            desc = cursor.description[i][0]
            arrays[desc] = cols[i]
        data.append(arrays)
    print(data)
    return JsonResponse( {
        'returnData': data,
    })

def getD3mbostocksourcedata(request):
    
    conn = pymssql.connect(settings.APP_SETTING["serverconfig"], settings.APP_SETTING["userconfig"], settings.APP_SETTING["passwordconfig"], settings.APP_SETTING["dbconfig"])
    cursor = conn.cursor()
    cursor.execute("  select  *   FROM [D3mbostocksource]")
    row=cursor.fetchall()
    data=[]

    for cols in row:
        arrays={}
        for i in range(len(cursor.description)):
            desc = cursor.description[i][0]
            arrays[desc] = cols[i]
        data.append(arrays)
    print(data)
    return JsonResponse(data , safe=False)
def getdatas(request):
    returndata={}
    
    
    returndata['REMOTE_ADDR']= request.META.get('REMOTE_ADDR')
    returndata['CONTENT_LENGTH']= request.META.get('CONTENT_LENGTH')
    returndata['CONTENT_TYPE']= request.META.get('CONTENT_TYPE')
    returndata['HTTP_ACCEPT_ENCODING']= request.META.get('HTTP_ACCEPT_ENCODING')
    returndata['HTTP_ACCEPT_LANGUAGE']= request.META.get('HTTP_ACCEPT_LANGUAGE')
    returndata['HTTP_HOST']= request.META.get('HTTP_HOST')
    returndata['HTTP_REFERER']= request.META.get('HTTP_REFERER')
    returndata['HTTP_USER_AGENT']= request.META.get('HTTP_USER_AGENT')
    returndata['QUERY_STRING']= request.META.get('QUERY_STRING')
    returndata['REMOTE_HOST']= request.META.get('REMOTE_HOST')
    returndata['REMOTE_USER']= request.META.get('REMOTE_USER')
    returndata['REQUEST_METHOD']= request.META.get('REQUEST_METHOD')
    returndata['SERVER_NAME']= request.META.get('SERVER_NAME')
    returndata['SERVER_PORT']= request.META.get('SERVER_PORT')
    request.session['color'] = 'blue'
    returndata['session_color']= str(request.session['color'] )
    request.session['food'] = 'beef'
    returndata['session_food']= str(request.session['food'] )
    #returndata['resolver_match']= request.resolver_match
    #returndata['current_app']= request.current_app
    #returndata['urlconf']= request.urlconf
    #returndata['session']= request.session
    #returndata['site']= request.site
    #returndata['user']= request.user
    
    
    returndata['get_host']= request.get_host()
    returndata['get_full_path']= request.get_full_path()
    returndata['get_port']= request.get_port()
    returndata['is_secure']= request.is_secure()
    returndata['is_ajax']= request.is_ajax()
    
    #post
    if(request.method=="POST"):
        returndata['scheme']= request.scheme
        returndata['body']= json.loads(request.body.decode('utf-8'))
        returndata['path']= request.path
        returndata['path_info']= request.path_info
        returndata['method']= request.method
        returndata['encoding']= request.encoding
        returndata['content_type']= request.content_type
        returndata['content_params']= request.content_params
        returndata['COOKIES']= request.COOKIES
        returndata['FILES']= request.FILES
    elif(request.method=="GET"):
        #get
        returndata['scheme']= request.scheme
        #returndata['body']= request.body
        returndata['path']= request.path
        returndata['path_info']= request.path_info
        returndata['method']= request.method
        returndata['encoding']= request.encoding
        returndata['content_type']= request.content_type
        returndata['content_params']= request.content_params
        returndata['COOKIES']= request.COOKIES
        returndata['FILES']= request.FILES
        
 

    print (returndata )
    return JsonResponse( {
        'returnData': returndata,
        
    })
