from django.urls import path
from . import views
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('api/lote', views.LoteViewSet )
router.register('api/produto', views.ProdutoViewSet)
router.register('api/orgaoDonatario', views.OrgaoDonatarioViewSet)
router.register('api/orgaoFiscalizador', views.OrgaoFiscalizadorViewSet)


router.register(r'users', UserViewSet)
urlpatterns = [
    path('api/', include(router.urls)),

    path("", views.index, name="index"),
    path("visualizar/<classe>", views.visualizar, name="visualizar"),
    path("example/", views.json_example, name="json"),
    path("example2/", views.json_example2, name="json2"),

    path("lote/", views.lote),
    path("orgaoDonatario/", views.orgaoDonatario),
    path("orgaoDonatario/<id>", views.orgaoDonatario_id),

    path("orgaoFiscalizador/", views.orgaoFiscalizador),
    path("produto/", views.produto),
    path("site/", views.site),
    path("SemFraude/", views.semfraude),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]