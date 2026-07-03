from django.urls import path
from .views import (
    UsersAPIView,
    EmployeeAPIView,
    ProductAPIView,
    TodosAPIView,
    SalesAPIView,
    login,
    me,
)

urlpatterns = [
    # auth
    path("auth/login/", login),
    path("auth/me/", me),

    # users
    path("users/", UsersAPIView.as_view()),
    path("users/<int:pk>/", UsersAPIView.as_view()),

    # employees
    path("employees/", EmployeeAPIView.as_view()),
    path("employees/<int:pk>/", EmployeeAPIView.as_view()),

    # products
    path("products/", ProductAPIView.as_view()),
    path("products/<int:pk>/", ProductAPIView.as_view()),

    # todos
    path("todos/", TodosAPIView.as_view()),
    path("todos/<int:pk>/", TodosAPIView.as_view()),

    # toggle
    path("todos/<int:pk>/toggle/", TodosAPIView.as_view()),

    # sales
    path("sales/", SalesAPIView.as_view()),
    path("sales/<int:pk>/", SalesAPIView.as_view()),
]