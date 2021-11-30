from core.models import VagaDeEmprego
from core.serializers import VagaDeEmpregoSerializer

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

class VagaDeEmpregoViewSet(APIView):
    def get(self, request):
        VagasDeEmprego = VagaDeEmprego.objects.all()
        serializer = VagaDeEmpregoSerializer(VagasDeEmprego, many= True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = VagaDeEmpregoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class VagasDeEmpregoDetail(APIView):
    def get(self,request, id):
        vagas = get_object_or_404(VagaDeEmprego.objects.all(), id=id)
        serializer = VagaDeEmpregoSerializer(vagas)
        return Response(serializer.data)

    def put(self,request,id):
        vagas = get_object_or_404(VagaDeEmprego.objects.all(), id=id)
        serializer = VagaDeEmpregoSerializer(vagas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        vagas = get_object_or_404(VagaDeEmprego.objects.all(), id=id)
        vagas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)