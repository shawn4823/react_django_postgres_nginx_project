from rest_framework import serializers
from .models import Users, Employee, Product, Todos, Sales


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        return Users.objects.create(**validated_data)

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"

    def validate_pay(self, value):
        if value < 0:
            raise serializers.ValidationError("급여는 0 이상이어야 합니다.")
        return value


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("price는 0 이상이어야 합니다.")
        return value

    def validate_sale_price(self, value):
        if value < 0:
            raise serializers.ValidationError("sale_price는 0 이상이어야 합니다.")
        return value



class TodosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todos
        fields = "__all__"

    def validate_subject(self, value):
        if not value.strip():
            raise serializers.ValidationError("subject는 비어있을 수 없습니다.")
        return value


class SalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = "__all__"

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("quantity는 1 이상이어야 합니다.")
        return value

    def validate_discount_rate(self, value):
        if value < 0 or value > 1:
            raise serializers.ValidationError("discount_rate는 0~1 사이여야 합니다.")
        return value

    def validate_total_price(self, value):
        if value < 0:
            raise serializers.ValidationError("total_price는 0 이상이어야 합니다.")
        return value