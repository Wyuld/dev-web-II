from django.db.models import fields
from core.models import Empregador, VagaDeEmprego, Inscricao
from rest_framework.serializers import ModelSerializer

class EmpregadorSerializer(ModelSerializer):
    class Meta:
        model = Empregador
        fields = "__all__"

class VagaDeEmpregoSerializer(ModelSerializer):
    class Meta:
        model = VagaDeEmprego
        fields = "__all__"

class IncricaoSerializer(ModelSerializer):
    class Meta:
        model = Inscricao
        fields = "__all__"