from django.db import models


class Pizza(models.Model):
    type = models.CharField(max_length=20)
    size = models.CharField(max_length=10)

class Orders(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    pizza = models.ManyToManyField(Pizza, blank=True, related_name='orders', through="PizzaOrders")

    def set_pizza(self,*pizza):
        self.pizza.clear()
        PizzaOrders.objects.bulk_create([PizzaOrders(orders=self,pizza=pizza_) for pizza_ in pizza])

class PizzaOrders(models.Model):
    order_id =  models.ForeignKey(Orders,on_delete=models.CASCADE)
    pizza_id = models.ForeignKey(Pizza,on_delete=models.CASCADE)

    class Meta:
        db_table = 'pizza_orders'
        managed = False
    # quantity = models.IntegerField()
    # price = models.FloatField()

class Customer(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    order = models.ForeignKey(Orders, related_name="customer", on_delete=models.CASCADE)
