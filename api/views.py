from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Projects, WorkExperiences
from .serializers import ProjectSerializer, WorkSerializer


@api_view(['GET'])
def get_projects(request):
    projects = Projects.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_work(request):
    work = WorkExperiences.objects.all()
    serializer = WorkSerializer(work, many=True)
    return Response(serializer.data)