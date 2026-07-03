from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False



class Employee(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField(unique=True)
        job = models.CharField(max_length=100)
        pay = models.IntegerField()

        class Meta:
            db_table = "employees"

        def __str__(self):
            return self.name

class Product(models.Model):
            product_name = models.CharField(max_length=100)
            color = models.CharField(max_length=30)
            price = models.IntegerField()
            sale_price = models.IntegerField()
            product_category_code = models.CharField(max_length=20)

            class Meta:
                db_table = "products"

            def __str__(self):
                return self.product_name


class Todos(models.Model):
    subject = models.CharField(max_length=200)
    checked = models.BooleanField(default=False)

    class Meta:
        db_table = "todos"

    def __str__(self):
        return self.subject



class Sales(models.Model):
    user_id = models.BigIntegerField()
    product_id = models.BigIntegerField()
    quantity = models.IntegerField()
    discount_rate = models.FloatField()
    total_price = models.IntegerField()
    created_at = models.DateField()

    class Meta:
        db_table = "sales"

    def __str__(self):
        return str(self.id)