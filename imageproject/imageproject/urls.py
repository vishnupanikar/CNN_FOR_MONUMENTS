"""imageproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#------------------------------FLOW CONTROL-----------------

from django.contrib import admin
from django.urls import path

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views

#This gives the flow of the server side
#admin -> image -> uploads(urls of image app)
#admin -> currentpage(for the home page)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.output , name = "output"),
    url(r'^image/', include('image_app.urls')),
	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)