from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='meals', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='meals/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.category:
            raise ValueError("Ҳар як хӯрок бояд ба категория тааллуқ дошта бошад.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Table(models.Model):
    STATUS_CHOICES = [
        ('free', 'Free'),
        ('reserved', 'Reserved'),
    ]
    table_number = models.IntegerField(unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='free')

    def __str__(self):
        return f"Table {self.table_number} - {self.status}"

class Bill(models.Model):
    table = models.ForeignKey(Table, related_name='bills', on_delete=models.CASCADE)
    customer = models.CharField(max_length=255, blank=True, null=True)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.table.status != 'reserved':
            self.table.status = 'reserved'
            self.table.save()
        super().save(*args, **kwargs)
    def save(self, *args, **kwargs):
        if not self.orders.exists():
            self.total_sum = 0
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Bill {self.id} - Total: {self.total_sum}"

class Order(models.Model):
    bill = models.ForeignKey(Bill, related_name='orders', on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, related_name='orders', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        bill = self.bill
        total = bill.total_sum + (self.meal.price * self.quantity)
        bill.total_sum = total
        bill.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} - {self.meal.name} x {self.quantity}"
    