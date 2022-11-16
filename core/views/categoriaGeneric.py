from core.models import Categoria
from core.serializers import CategoriaSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# post e get(listar todos)
class CategoriasListGeneric(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# patch,delete e get(listar um)
class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
