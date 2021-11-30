from core.views.inscricaoApiView import InscricaoDetail, InscricaoViewSet
from core.models import VagaDeEmprego
from core.views.vagaDeEmpregoApiView import VagaDeEmpregoViewSet, VagasDeEmpregoDetail
from core.views.empregadorApiView import EmpregadorDetail, EmpregadorViewSet
from django.contrib import admin
from django.urls import path, include
from core import views
from rest_framework import routers

## TODO URLS on router
router = routers.DefaultRouter()
# router.register(r"vagas-apiviews", views.VagaDeEmpregoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empregadores-apiview/', EmpregadorViewSet.as_view()),
    path('empregadores-apiview/<int:id>/', EmpregadorDetail.as_view()),
    path('vagas-apiview/', VagaDeEmpregoViewSet.as_view()),
    path('vagas-apiview/<int:id>/', VagasDeEmpregoDetail.as_view()),
    path('inscricoes-apiview/', InscricaoViewSet.as_view()),
    path('inscricoes-apiview/<int:id>/', InscricaoDetail.as_view()),
    # path('api/', include(routers.urls))
]
