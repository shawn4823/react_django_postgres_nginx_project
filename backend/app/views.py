from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Users, Employee, Product, Todos, Sales
from .serializer import (
    UsersSerializer,
    EmployeeSerializer,
    ProductSerializer,
    TodosSerializer,
    SalesSerializer
)
from .jwt import create_access_token



# ===========================
# JWT
# ===========================



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):
    user = request.user

    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "age": user.age,
        "city": user.city,
    })

@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    try:
        user = Users.objects.filter(username=username).first()

        if user.password != password:
            return Response({"message": "wrong password"}, status=401)

        token = create_access_token(user.id)

        return Response({
            "token": token,
            "user": {
                "id": user.id,
                "username": user.username
            }
        })

    except Users.DoesNotExist:
        return Response({"message": "user not found"}, status=404)


# ===========================
# USERS
# ===========================

class UsersAPIView(APIView):

    def get(self, request, pk=None):

        if pk:
            try:
                user = Users.objects.get(pk=pk)
            except Users.DoesNotExist:
                return Response({"message": "user not found"}, status=404)

            serializer = UsersSerializer(user)
            return Response(serializer.data)

        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = UsersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=400)

    def put(self, request, pk):

        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response({"message": "user not found"}, status=404)

        serializer = UsersSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk):

        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response({"message": "user not found"}, status=404)

        user.delete()
        return Response(status=204)


# ===========================
# EMPLOYEE
# ===========================

class EmployeeAPIView(APIView):

    def get(self, request, pk=None):

        if pk:
            try:
                employee = Employee.objects.get(pk=pk)
            except Employee.DoesNotExist:
                return Response({"message": "Employee not found"}, status=404)

            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)

        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

    def put(self, request, pk):

        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"message": "Employee not found"}, status=404)

        serializer = EmployeeSerializer(employee, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk):

        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"message": "Employee not found"}, status=404)

        employee.delete()
        return Response(status=204)


# ===========================
# PRODUCT
# ===========================

class ProductAPIView(APIView):

    def get(self, request, pk=None):

        if pk:
            try:
                product = Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                return Response({"message": "Product not found"}, status=404)

            serializer = ProductSerializer(product)
            return Response(serializer.data)

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

    def put(self, request, pk):

        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=404)

        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk):

        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=404)

        product.delete()
        return Response(status=204)


class TodosAPIView(APIView):

    # GET ALL / GET ONE
    def get(self, request, pk=None):

        if pk:
            try:
                todo = Todos.objects.get(pk=pk)
            except Todos.DoesNotExist:
                return Response(
                    {"message": "Todo not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = TodosSerializer(todo)
            return Response(serializer.data)

        todos = Todos.objects.all()
        serializer = TodosSerializer(todos, many=True)

        return Response(serializer.data)


    # CREATE
    def post(self, request):

        serializer = TodosSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    # UPDATE
    def put(self, request, pk):

        try:
            todo = Todos.objects.get(pk=pk)
        except Todos.DoesNotExist:
            return Response(
                {"message": "Todo not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TodosSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    # PATCH (toggle)
    def patch(self, request, pk):

        try:
            todo = Todos.objects.get(pk=pk)
        except Todos.DoesNotExist:
            return Response(
                {"message": "Todo not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        todo.checked = not todo.checked
        todo.save()

        serializer = TodosSerializer(todo)

        return Response(serializer.data)


    # DELETE
    def delete(self, request, pk):

        try:
            todo = Todos.objects.get(pk=pk)
        except Todos.DoesNotExist:
            return Response(
                {"message": "Todo not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        todo.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class SalesAPIView(APIView):

    # GET ALL / GET ONE
    def get(self, request, pk=None):

        if pk:
            try:
                sale = Sales.objects.get(pk=pk)
            except Sales.DoesNotExist:
                return Response(
                    {"message": "Sale not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = SalesSerializer(sale)
            data = serializer.data

            try:
                user = Users.objects.get(pk=data["user_id"])
                data["username"] = user.username
            except Users.DoesNotExist:
                data["username"] = "알수없음"

            return Response(data)

        sales = Sales.objects.all()
        serializer = SalesSerializer(sales, many=True)
        data = serializer.data

        user_map = {u.id: u.username for u in Users.objects.all()}
        for item in data:
            item["username"] = user_map.get(item["user_id"], "알수없음")

        return Response(data)