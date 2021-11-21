"""tutorial_pt1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

# from django.http import HttpResponse

# def home(request):                      #Tworzymy stronę home
#     return HttpResponse('Home page')

# def contact(request):
#     return HttpResponse('Contant page')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')) #kiedy uzywamy tej sciezki url, zamimast szukac konkretnej funkcji, odsyla nas do pliku accounts -> urls i pozwol tamtym funkcjonalnosciom to obsluzyc, one wyszukuja odpowiednia sciezke i uderzaja w konkretne funkcje w "views"



    # path('', home), #we need to tell what view is connected to this path. W tym przypadku home jest na "base url" więc jest pusty cudzysłów
    # path('about/', contact), #w tym przypadku gdy wejdziemy na stronę "about" to pojawi się odpowiedź z funkcji contact.
                              

]
