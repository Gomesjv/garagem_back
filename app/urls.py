from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import AcessorioViewSet,CategoriaViewSet,CorViewSet, UserViewSet, MarcaViewSet, ModeloViewSet, VeiculoViewSet

from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

router = DefaultRouter()

router.register(r"usuarios", UserViewSet, basename="usuarios")
router.register(r"acessorios", AcessorioViewSet, basename="acessorios")
router.register(r"categoria", CategoriaViewSet, basename="categorias")
router.register(r"cores", CorViewSet, basename="cores")
router.register(r"marcas", MarcaViewSet, basename="marcas")
router.register(r"modelos", ModeloViewSet, basename="modelos")
router.register(r"veiculos", VeiculoViewSet, basename="veiculos")

urlpatterns = [
    path("admin/", admin.site.urls),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # Simple JWT
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # API
    path("api/", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
