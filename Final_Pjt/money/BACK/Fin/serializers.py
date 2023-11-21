
from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import DepositProducts, DepositOptions, GeneralDepositOptions, GeneralDepositProducts



class DepositOptionsSerializer(ModelSerializer):
    product = ReadOnlyField(source='DepositOptions.product')
    
    class Meta:
        model = DepositOptions
        fields = '__all__'
        # read_only_fields = ('product', )


class DepositProductsSerializer(ModelSerializer):
    options = DepositOptionsSerializer(many=True, read_only=True)
    class Meta:
        model = DepositProducts
        fields = '__all__'
        read_only_fields = ('options',)


class NestedSerialzer(ModelSerializer):
    product = DepositProductsSerializer(read_only=True)
    
    class Meta:
        model = DepositOptions
        fields = '__all__'






class GeneralDepositOptionsSerializer(ModelSerializer):
    product = ReadOnlyField(source='GeneralDepositOptions.product')
    
    class Meta:
        model = GeneralDepositOptions
        fields = '__all__'
        # read_only_fields = ('product', )


class GeneralDepositProductsSerializer(ModelSerializer):
    options = GeneralDepositOptionsSerializer(many=True, read_only=True)
    class Meta:
        model = GeneralDepositProducts
        fields = '__all__'
        read_only_fields = ('options',)



class GeneralNestedSerialzer(ModelSerializer):
    product = GeneralDepositProductsSerializer(read_only=True)
    
    class Meta:
        model = GeneralDepositOptions
        fields = '__all__'