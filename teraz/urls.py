from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'teraz'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('login', views.login, name='login'),
    path('przed', views.przed, name='przed'),
    path('teraz', views.teraz, name='teraz'),
    path('po', views.po, name='po'),
    path('form', views.get_info, name='get_info')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)