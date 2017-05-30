"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from viewAge.views import viewpage,hello_world,viewpageConfig,login,form,D3stockSource
from viewAge.Api import getdata,getdatas,getD3mbostocksourcedata

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello_world),
    url(r'^viewpage/$', viewpage),
    url(r'^viewpageConfig/$', viewpageConfig),
    url(r'^login/$', login),
    url(r'^form/$', form),
    url(r'^D3stockSource/(\w+)/$', D3stockSource),
    url(r'^api/getdata/(\w+)/$', getdata),
    url(r'^api/getdatas/$', getdatas),
    url(r'^api/getD3mbostocksourcedata/$', getD3mbostocksourcedata),


]
