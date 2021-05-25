"""murekkepvekeci URL Configuration

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
from django.urls import path
from django.urls import include

from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LogoutView, LoginView

from keci import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_view, name="register"),
    path('keci/', include('keci.urls')),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name="logout"), #aslında burada herhangi bir template sağlamamıza gerek yok -hatta sağlamamalıyız ki bu url'e gidildiğinde herhangi bir sayfa açılmasın- çünkü 'logout' yapanları doğrudan 'keci_home'a yönlendiriyoruz.
    path('', include('django.contrib.auth.urls')),
    path('keci/', RedirectView.as_view(url='keci/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)