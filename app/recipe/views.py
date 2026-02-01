""" Views for the recipe APIs."""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentucation_classes = [TokenAuthentication]
    premission_classes = [IsAuthenticated]

    def get_quertset(self):
        """Retrieve recipes for authentucated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')
