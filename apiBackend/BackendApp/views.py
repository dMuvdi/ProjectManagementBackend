from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from BackendApp.models import Roles, User, Models, Operations, Rol_operacion, FieldsOfStudy, States, Project
from BackendApp.serializers import RolesSerilizer, UserSerilizer, ModelsSerilizer, OperationsSerilizer, Rol_operacionSerilizer, FieldsOfStudySerilizer, StatesSerilizer, ProjectSerilizer
from django.core.files.storage import default_storage
# Create your views here.

@csrf_exempt
def projectApi(request, id=0):
    if request.method == 'GET':
        project = Project.objects.all()
        project_serilizer = ProjectSerilizer(project, many = True)
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
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        project = Project.objects.get(id = id)
        project.delete()
        return JsonResponse("Deleted Successfully", safe = False)

@csrf_exempt
def userApi(request, id=0):
    if request.method == 'GET':
        user = User.objects.all()
        user_serilizer = UserSerilizer(user, many = True)
        return JsonResponse(user_serilizer.data, safe = False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serilizer = UserSerilizer(data = user_data)
        if user_serilizer.is_valid():
            user_serilizer.save()
            return JsonResponse("Added Succesfully", safe = False)
        return JsonResponse("Failed to Add", safe = False)
    elif request.method == 'PUT' :
        user_data=JSONParser().parse(request)
        user=User.objects.get(id=user_data['id'])
        user_serilizer=UserSerilizer(user, data=user_data)
        if user_serilizer.is_valid():
            user_serilizer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        user = User.objects.get(id = id)
        user.delete()
        return JsonResponse("Deleted Successfully", safe = False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name, safe = False)