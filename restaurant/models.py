from django.db import models


# Restaurant model
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    street = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# Menu model
class Menu(models.Model):
    day = models.CharField(max_length=10)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dishes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.day
