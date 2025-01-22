from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DIVISION_CHOICES = (
    ('Dhaka','Dhaka'),
    ('Chittagong','Chittagong'),
    ('Sylhet','Sylhet'),
    ('Rangpur','Rangpur'),
    ('Rajshahi','Rajshahi'),
    ('Mymensingh','Mymensingh'),
    ('Khulna','Khulna'),
    ('Barisal','Barisal'),
)

CATEGORY_CHOICES = (
    ('C','Cat'),
    ('D','Dog'),
    ('B','Bird'),
    ('O','Other'),
)


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Confirmed', 'Confirmed'),
    ('On The Way' , 'On The Way'),
    ('Delivered' , 'Delivered'),
    ('Cancel' , 'Cancel'),
    ('Pending' , 'Pending')

)

class Product(models.Model):
    title = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, default='')
    adoption_fee = models.FloatField()
    description = models.TextField()
    origin = models.TextField(default='')
    health_issue = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    division = models.CharField(choices=DIVISION_CHOICES, max_length=200)
    address = models.CharField(max_length=500, default='N/A')

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)

    @property
    def total_cost(self):
        return self.quantity * self.product.adoption_fee

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default= "")
    @property
    def total_cost(self):
        return self.quantity * self.product.adoption_fee
    
class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
