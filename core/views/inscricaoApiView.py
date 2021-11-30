from core.models import Inscricao
from core.serializers import IncricaoSerializer

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

class InscricaoViewSet(APIView):
    def get(self, request):
        inscricao =  Inscricao.objects.all()
        serializer = IncricaoSerializer(inscricao, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = IncricaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class InscricaoDetail(APIView):
    def get(self, request, id):
        inscricao = get_object_or_404(Inscricao.objects.all(), id=id)
        serializer = IncricaoSerializer(inscricao)
        return Response(serializer.data)

    def put(self,request,id):
        inscricao = get_object_or_404(Inscricao.objects.all(), id=id)
        serializer = IncricaoSerializer(inscricao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        inscricao = get_object_or_404(Inscricao.objects.all(), id=id)
        inscricao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
