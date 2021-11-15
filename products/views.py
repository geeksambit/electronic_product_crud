from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.permissions import IsAuthenticated

from .models import Product,ProductAttribute
from .serializers import ProductSerializer,ProductAttributeSerializer,MobileSerializer


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset,many= True)
        # serializer = self.serializer_class
        return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "All Product record",
            },
            status.HTTP_200_OK
        )
    
    def retrieve(self, request, pk=None):
            queryset = Product.objects.all()
            product = get_object_or_404(queryset, pk=pk)
            serializer = ProductSerializer(product)
            return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "Got single Product record",
            },
            status.HTTP_200_OK
        )

    def create(self, request):
        serializer_class = self.serializer_class
        serializer = serializer_class(data=request.data, context={'request' : request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 201,
                "message" : "Successfully created Product record",
            },
            status.HTTP_200_OK
        )

    def update(self, request, pk=None):
        serializer_class = self.serializer_class
        serializer = serializer_class(data=request.data, instance=self.get_object())
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        data.save()

        return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "Successfully updated Product record",
            },
            status.HTTP_200_OK
        )

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(
             {
                "data": [],
                "status" : "ok",
                "code" : 200,
                "message" : "Successfully Deleted Product record",
            },
            status.HTTP_204_OK
        )


# anthor way of writting views for same functionality

class SecondProductViewSet(APIView):
    def get_object(self,id= None):
         try:
            return Product.objects.get(id=id)
            
         except Product.DoesNotExist as e:
            raise Http404
            # return Response({"error": "Given product not found."}, status=404)   
    
    def get(self, request, id=None):
        
        instance = self.get_object(id)
        serializer = ProductSerializer(instance)
        return Response(

            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "Got single Product record",
            },
            status.HTTP_200_OK
        )

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = ProductSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "Successfully updated Product record",
            },
            status.HTTP_200_OK
        )
        return Response({"data":serializer.errors,"status":"01","message":"success"}, status=400)

    def delete(self, request, id=None):
        instance = self.get_object(id)
        instance.delete()
        return Response(
             {
                "data": [],
                "status" : "ok",
                "code" : 200,
                "message" : "Successfully Deleted Product record",
            },
            status.HTTP_200_OK
        )
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):
    def get(self, request, format=None):
        query = Product.objects.all()
        serializer = ProductSerializer(query, many=True)
        return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "All Product record",
            },
            status.HTTP_200_OK
        )

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 201,
                "message" : "Successfully created Product record",
            },
            status.HTTP_200_OK
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductAttributeView(APIView):
    
    def get(self, request, format=None):
        query = ProductAttribute.objects.all()
        serializer = ProductAttributeSerializer(query, many=True)
        return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "All Product record",
            },
            status.HTTP_200_OK
        )

    def post(self, request, format=None):
        serializer = ProductAttributeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 201,
                "message" : "Successfully created Product record",
            },
            status.HTTP_201_CREATED
        )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductAttributeDetails(APIView):
    def get_object(self,id= None):
         try:
            return ProductAttribute.objects.get(id=id)
            
         except ProductAttribute.DoesNotExist as e:
            raise Http404
            # return Response({"error": "Given product not found."}, status=404)   
    
    def get(self, request, id=None):
        
        instance = self.get_object(id)
        serializer = ProductAttributeSerializer(instance)
        return Response(

            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "Got single Product record",
            },
            status.HTTP_200_OK
        )

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = ProductAttributeSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "Successfully updated Product record",
            },
            status.HTTP_200_OK
        )
        return Response({"data":serializer.errors,"status":"01","message":"success"}, status=400)

    def delete(self, request, id=None):
        instance = self.get_object(id)
        instance.delete()
        return Response(
             {
                "data": [],
                "status" : "ok",
                "code" : 200,
                "message" : "Successfully Deleted Product record",
            },
            status.HTTP_200_OK
        )
    def post(self, request, format=None):
        serializer = ProductAttributeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MobilesView(APIView):
    
    def get(self, request, format=None):
        query = Product.objects.filter(type ="Mob")
        serializer = MobileSerializer(query, many=True)
        return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "All Mobile record",
            },
            status.HTTP_200_OK
        )


class LaptopsView(APIView):
    
    def get(self, request, format=None):
        query = Product.objects.filter(type ="Mob")
        serializer = MobileSerializer(query, many=True)
        return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "All Mobile record",
            },
            status.HTTP_200_OK
        )