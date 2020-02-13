from django.conf.urls import url
from . import views
from .forms import LoginForm

app_name='accounts'

urlpatterns = [   
    url(r'^login/$',views.login_view,name="login"),
    url(r'^logout/$',views.logout_view,name="logout"),
]