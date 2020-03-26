from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views
from django.contrib.auth import views as auth_views
from Login.views import LoginClass
from Login.views import LandingClass
from Login.views import DashboardClass

#VISTAS
# from Login.views import Index
# from Login.views import Landing
#URL QUE MANEJAN LOS PARAMETROS DASHBOARD
app_name = 'Login'
urlpatterns = [
    path('',LandingClass.as_view(), name='Landing'),
    path('login/', LoginClass.as_view(), name='login'),
    path('Dashboard',DashboardClass.as_view(), name='Dashboard'),
]