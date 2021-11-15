from rest_framework import serializers

import products
from .models import Product,ProductAttribute
from rest_framework import exceptions


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'
        # read_only_fields = []


class ProductAttributeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductAttribute
        fields = '__all__'
        # read_only_fields = []

    # validation for laptop/mobile attribute
    def validate(self, data):
        # import pdb ;pdb.set_trace()
        product_type = data["product"].type

        screen_size = data.get('screen_size')
        colour = data.get('colour')
        hd_capacity = data.get('hd_capacity')

        if product_type == "Lap":
            if not hd_capacity:
                raise serializers.ValidationError({
                'hd_capacity': 'This field is required.'
            })
        if product_type == "Mob":
            if not screen_size :
                raise serializers.ValidationError({
                'screen_size': 'This field is required.'
            })
            if not colour :
                raise serializers.ValidationError({
                'colour': 'This field is required.'
            })

        return data

class MobileData(serializers.ModelSerializer):
    
    class Meta:
        model = ProductAttribute
        fields = ["processor","ram","screen_size","colour"]
        # read_only_fields = ["processor","ram","screen_size","colour"]
class MobileSerializer(serializers.ModelSerializer):

    product_attribute = MobileData(many=True)
    
    class Meta:
        model = Product
        # fields = '__all__'
        # read_only_fields = []

        fields = [

            "id",
            "name",
            "description",
            "type",
            'product_attribute'
        ]


class LaptopData(serializers.ModelSerializer):
    
    class Meta:
        model = ProductAttribute
        fields = ["processor","ram","hd_capacity"]
        # read_only_fields = ["processor","ram","screen_size","colour"]
class MobileSerializer(serializers.ModelSerializer):

    product_attribute = LaptopData(many=True) 
    class Meta:
        model = Product
        # fields = '__all__'
        # read_only_fields = []

        fields = [

            "id",
            "name",
            "description",
            "type",
            'product_attribute'
        ]