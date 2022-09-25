from django.forms.models import model_to_dict


from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer
from django.http import JsonResponse
from products.models import Product


@api_view(['POST'])
def api_home(request, *args, **kwargs):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)