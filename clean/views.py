from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework.views import *
from rest_framework.generics import *
from rest_framework.permissions import *
# Create your views here.
from clean.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ListProductApi(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    permission_classes = (IsAuthenticated,)

class MyProductsApi(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    permission_classes = (IsAuthenticated,)

class AllProductApi(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    permission_classes = (AllowAny,)
class GetUserProduct(ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        user_id = self.kwargs.get('id')
        return Product.objects.filter(user_id=user_id)

class EditMyProduct(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        return Product.objects.filter(pk=post_id,user=self.request.user)

    permission_classes = (IsAuthenticated,)

class EditProductPrice(APIView):
    permission_classes = (AllowAny,)

    def get(self,request):
        return Response({"test":"working get"})
    def post(self,request):

        post_id = request.data['post_id']
        price = request.data['price']
        if 'post_id' not in request.data:
            raise ValidationError({"error":"Поле поста не должно быть пустым"})
        elif 'price' not in request.data:
            raise ValidationError({"error": "Поле цены не должно быть пустым"})

        product = Product.objects.get(pk=post_id)
        product.price = float(price)
        product.save()
        return Response({
            'product':model_to_dict(product)
        })

