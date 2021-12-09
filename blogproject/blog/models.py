from django.db import models

# Create your models here.
class post(models.Model):
    STATES = (
        (0 ,"Unpublished" ),
        (1 ,"published" ),
    )
    title = models.CharField(max_length=100 , unique=True )
    slug = models.SlugField(max_length=100 , unique=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    states = models.IntegerField(choices= STATES, default= 0)

    def __str__(self):
        return f"{self.title} : created at {self.created_at} "