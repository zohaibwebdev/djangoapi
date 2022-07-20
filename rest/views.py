from django.shortcuts import render
from .serializers import stuSerializer
from .models import student

# Create your views here.

def student_detail(request):
    stu = student.objects.get(id=2)
    
