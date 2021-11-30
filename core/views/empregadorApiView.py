
from core.models import Empregador
from core.serializers import EmpregadorSerializer

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404


class EmpregadorViewSet(APIView):
    def get(self, request):
        empregadores = Empregador.objects.all()
        serializer = EmpregadorSerializer(empregadores, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = EmpregadorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpregadorDetail(APIView):
    def get(self, request, id):
        empregador = get_object_or_404(Empregador.objects.all(), id=id)
        serializer = EmpregadorSerializer(empregador)
        return Response(serializer.data)

    def put(self,request, id):
        empregador = get_object_or_404(Empregador.objects.all(), id=id)
        serializer = EmpregadorSerializer(empregador, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        empregador = get_object_or_404(Empregador.objects.all(), id=id)
        empregador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)