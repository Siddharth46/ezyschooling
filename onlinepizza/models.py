from django.db import models

class Pizza(models.Model):
    p_id = models.TextField(primary_key=True)
    p_type = models.TextField()  # This field type is a guess.
    p_size = models.TextField()  # This field type is a guess.
    p_toppings = models.TextField(blank=True, null=True)