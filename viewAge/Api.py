from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from datetime import datetime
from django.shortcuts import render
from django.conf import settings
import pymssql
# Create your views here.
#def hello_world(request):
#    return HttpResponse("Hello World!")
"""
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
"""
def getdata(request,data):
    
    conn = pymssql.connect(settings.APP_SETTING["serverconfig"], settings.APP_SETTING["userconfig"], settings.APP_SETTING["passwordconfig"], settings.APP_SETTING["dbconfig"])
    cursor = conn.cursor()
    cursor.execute("  select  *   FROM [Farmdata].[dbo].[patentFSecure] where patentNo ='%s'"  %data)
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

    
