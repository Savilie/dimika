from rest_framework import status, filters
from elasticsearch import Elasticsearch

from .models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
# Create your views here.


class ProductAPIView(APIView):
    """APIView модели Product"""
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Product.objects.all()  # Установите queryset вашей модели Product



    def get(self, request):
        p = Product.objects.all()
        category_id = self.request.query_params.get('category_id')

        if category_id:
            p = p.filter(category_id=category_id)

        return Response({'products': ProductSerializer(p, many=True).data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Put method is not allowed"})
        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"product": serializer.data})

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Patch method is not allowed"})
        try:
            instance = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Object does not exist"})

        serializer = ProductSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"product": serializer.data})

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CategoryAPIView(APIView):
    """APIView модели Category"""
    permission_classes = [IsAuthenticatedOrReadOnly, ] # Проверка аутентификации, если нет => только чтение
    queryset = Category.objects.all()  # Установите queryset вашей модели Product


    def get(self, request):
        c = Category.objects.all()
        parent_id = self.request.query_params.get('parent_id')
        tree_id = self.request.query_params.get('tree_id')

        if tree_id:
            c = c.filter(tree_id=tree_id)
            return Response({'categories': CategorySerializer(c, many=True).data})

        if parent_id:
            c = c.filter(parent_id=parent_id)
        elif not parent_id:
            c = c.filter(parent_id=None)


        return Response({'categories': CategorySerializer(c, many=True).data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Put method is not allowed"})
        try:
            instance = Category.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = CategorySerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"category": serializer.data})

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Patch method is not allowed"})
        try:
            instance = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Object does not exist"})

        serializer = CategorySerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"category": serializer.data})

    def delete(self, request, pk):
        try:
            product = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


