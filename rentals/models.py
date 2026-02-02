from django.db import models
from django.contrib.auth.models import User

# 1. Model Kategorii
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

# 2. Model Sprzętu
class Equipment(models.Model):
    category = models.ForeignKey(Category, related_name='equipment', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    serial_number = models.CharField(max_length=100, unique=True)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)  # Cena za dzień
    is_available = models.BooleanField(default=True)  # Czy sprzęt jest dostępny
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"

# 3. Model Wypożyczenia
class Rental(models.Model):
    user = models.ForeignKey(User, related_name='rentals', on_delete=models.CASCADE)  # Kto wypożycza
    equipment = models.ForeignKey(Equipment, related_name='rentals', on_delete=models.CASCADE)  # Co wypożycza
    start_date = models.DateField()
    end_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)  # Data faktycznego zwrotu
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f"Rental: {self.equipment.name} by {self.user.username}"

# 4. Model Serwisu/Napraw
class Maintenance(models.Model):
    equipment = models.ForeignKey(Equipment, related_name='maintenance_logs', on_delete=models.CASCADE)
    issue_description = models.TextField()  # Opis usterki
    date_reported = models.DateField(auto_now_add=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_fixed = models.BooleanField(default=False)

    def __str__(self):
        return f"Fix: {self.equipment.name} - {self.date_reported}"