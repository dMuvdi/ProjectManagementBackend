from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from BackendApp.models import Roles, User, Models, Operations, Rol_operacion, FieldsOfStudy, States, Project
from BackendApp.serializers import RolesSerilizer, UserSerilizer, ModelsSerilizer, OperationsSerilizer, Rol_operacionSerilizer, FieldsOfStudySerilizer, StatesSerilizer, ProjectSerilizer
from django.core.files.storage import default_storage
from rest_framework import generics
from BackendApp import urls
from django.urls import reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def projectApi(request, id=0):
    if request.method == 'GET':
        if id:
            projects = Project.objects.filter(id = id)
            project_serilizer = ProjectSerilizer(projects, many=True)
            return JsonResponse(project_serilizer.data[0], safe = False)
        else:
            projects = Project.objects.all()
            project_serilizer = ProjectSerilizer(projects, many=True)
            return JsonResponse(project_serilizer.data, safe = False)
    elif request.method == 'POST':
        project_data = JSONParser().parse(request)
        project_serilizer = ProjectSerilizer(data = project_data)
        if project_serilizer.is_valid():
            project_serilizer.save()
            return JsonResponse("Added Succesfully", safe = False)
        return JsonResponse("Failed to Add", safe = False)
    elif request.method == 'PUT' :
        project_data=JSONParser().parse(request)
        project=Project.objects.get(id=project_data['id'])
        project_serilizer=ProjectSerilizer(project, data=project_data)
        if project_serilizer.is_valid():
            project_serilizer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe = False)
    elif request.method == 'DELETE':
        project = Project.objects.get(id = id)
        project.delete()
        return JsonResponse("Deleted Successfully", safe = False)

@csrf_exempt
def userApi(request, id=0):
    if request.method == 'GET':
        if id:
            user = User.objects.filter(id = id)
            user_serilizer = UserSerilizer(user, many=True)
            return JsonResponse(user_serilizer.data[0], safe = False)
        elif(request.path == '/user/active'):
            user = User.objects.filter(Active = True)
            user_serilizer = UserSerilizer(user, many=True)
            if user:
                return JsonResponse(user_serilizer.data[0], safe = False)
            else:
                return JsonResponse("No active users", safe = False)
        else:
            user = User.objects.all()
            user_serilizer = UserSerilizer(user, many=True)
            return JsonResponse(user_serilizer.data, safe = False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serilizer = UserSerilizer(data = user_data)
        if user_serilizer.is_valid():
            user_serilizer.save()
            return JsonResponse({"success":True}, safe = False)
        return JsonResponse({"success":False}, safe = False)
    elif request.method == 'PUT':
        user_data=JSONParser().parse(request)
        user=User.objects.get(id=user_data['id'])
        user_serilizer=UserSerilizer(user, data=user_data)
        if user_serilizer.is_valid():
            user_serilizer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe = False)
    elif request.method == 'DELETE':
        user = User.objects.get(id = id)
        user.delete()
        return JsonResponse("Deleted Successfully", safe = False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name,file)
    return HttpResponse(file_name)

class StatesView(generics.RetrieveAPIView):
    queryset = States.objects.all()
    serializer_class = StatesSerilizer

@csrf_exempt
def userLogIn(request, email, password):
    if request.method == 'PUT':
        user = User.objects.filter(Email = email, Password = password).update(Active=True)
        user_serilizer=UserSerilizer(user, data=user)
        if user:
            return JsonResponse({"success":True}, safe = False)
        else:
            return JsonResponse({"success":False}, safe = False)
            

@csrf_exempt
def userLogOff(request, email):
    if request.method == 'PUT':
        user = User.objects.filter(Email = email).update(Active=False)
        user_serilizer=UserSerilizer(user, data=user)
        if user:
            return JsonResponse({"success":True}, safe = False)
        else:
            return JsonResponse({"success":False}, safe = False)


@csrf_exempt
def projectSearch(request, searchTitle):
    if request.method == 'GET':
        project = Project.objects.filter(Title__contains=searchTitle)
        project_serilizer=ProjectSerilizer(project, many=True)
        if project:
            return JsonResponse(project_serilizer.data[0], safe = False)
        else:
            return JsonResponse("No projects found", safe = False)

@csrf_exempt
def userMyProject(request, id):
    if request.method == 'GET':
        project = Project.objects.filter(Author_id__in = [id])
        project_serilizer=ProjectSerilizer(project, many=True)
        if project:
            return JsonResponse(project_serilizer.data[0], safe = False)
        else:
            return JsonResponse("No projects found", safe = False)
