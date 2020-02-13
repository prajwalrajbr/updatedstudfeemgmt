from django.contrib import admin
from django.conf.urls import url,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^accounts/',include('accounts.urls')),
    url(r'^entry/',include('entry.urls')),
    url(r'^details/',include('details.urls')),
    url(r'^$',views.home,name="index"),
]

urlpatterns += staticfiles_urlpatterns()