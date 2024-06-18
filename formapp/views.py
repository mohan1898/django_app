from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import StudenInfo
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

class Formlist(APIView):
    renderer_classes=[TemplateHTMLRenderer]
    template_name='form.html'

    def get(self,request):
        pro=StudenInfo.objects.all()
        return Response({'profile':pro})
