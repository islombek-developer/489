from django.urls import path
from .views import LoginView,RegisterView,prfil,read,delete,student_create,student_update,reg
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login-page/', LoginView.as_view(),name='login'),
    path('register/', RegisterView.as_view(),name='register'),
    path('profil/',prfil,name='profil'),
    path('reg/',reg,name='reg'),
    path('read/<int:id>',read,name='read'),
    path('delete/<int:id>/', delete, name='delete'), 
     path('students/create/', student_create, name='student_create'),
    path('students/<int:id>/edit/', student_update, name='student_update'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)