from rest_framework import generics, mixins, permissions, authentication

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import Http404

# from api.permissions import IsStaffEditorPermission

from api.mixins import StaffEditorPermissionMixin

from .models import Product
from .serializers import ProductSerializer


from api.authentication import TokenAuthentication


class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     TokenAuthentication]

    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)




###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????


class ProductMixinView(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        generics.GenericAPIView,
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response()

        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)



    if method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title
            serializer.save(content=content)
        return Response(serializer.data)
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????



class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????



class ProductUpdataAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????
###########<<<<<<&&&&&&&$$$$$$$@@@@>>>>???????????


class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
