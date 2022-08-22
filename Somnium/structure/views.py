from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import send_notice

class DocsView(APIView):
    def get(self, request, *args, **kwargs):
        apidocs = {
            'organizations': request.build_absolute_uri('organizations/'),
            'collegial_bodies': request.build_absolute_uri('collegial_bodies/'),
            'administrative_bodies': request.build_absolute_uri('administrative_bodies/'),
            'directors': request.build_absolute_uri('directors/'),
            'subdivisions': request.build_absolute_uri('subdivisions/'),
            'positions': request.build_absolute_uri('positions/'),
            'persons': request.build_absolute_uri('persons/'),
            'tasks': request.build_absolute_uri('tasks/'),
         }
        return Response(apidocs)


class OrganizationList(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    
    
class CollegialBodyList(generics.ListCreateAPIView):
    queryset = CollegialBody.objects.all()
    serializer_class = CollegialBodySerializer

class CollegialBodyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CollegialBody.objects.all()
    serializer_class = CollegialBodySerializer


class AdministrativeBodyList(generics.ListCreateAPIView):
    queryset = AdministrativeBody.objects.all()
    serializer_class = AdministrativeBodySerializer

class AdministrativeBodyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdministrativeBody.objects.all()
    serializer_class = AdministrativeBodySerializer


class PositionList(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class PositionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
    
class DirectorList(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    
    
class SubdivisionList(generics.ListCreateAPIView):
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer

class SubdivisionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer
    
    
class TaskList(APIView):
    serializer_class = TaskSerializer
    
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_notice.apply_async(kwargs={'task_info': serializer.data}, eta=serializer.data['date_start'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    
    
    
    
    
    
    
    
    
