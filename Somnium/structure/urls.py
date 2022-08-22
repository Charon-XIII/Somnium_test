from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from structure import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'structure'

urlpatterns = [
    path('', views.DocsView.as_view()),
    path('organizations/', views.OrganizationList.as_view()),
    path('organizations/<int:pk>/', views.OrganizationDetail.as_view()),
    path('collegial_bodies/', views.CollegialBodyList.as_view()),
    path('collegial_bodies/<int:pk>/', views.CollegialBodyDetail.as_view(),),
    path('administrative_bodies/', views.AdministrativeBodyList.as_view()),
    path('administrative_bodies/<int:pk>/', views.AdministrativeBodyDetail.as_view()),
    path('positions/', views.PositionList.as_view()),
    path('positions/<int:pk>/', views.PositionDetail.as_view()),
    path('persons/', views.PersonList.as_view()),
    path('persons/<int:pk>/', views.PersonDetail.as_view(), name="person-detail"),
    path('directors/', views.DirectorList.as_view()),
    path('directors/<int:pk>/', views.DirectorDetail.as_view()),
    path('subdivisions/', views.SubdivisionList.as_view()),
    path('subdivisions/<int:pk>/', views.SubdivisionDetail.as_view()),
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)



