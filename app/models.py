from django.db import models

# Create your models here.

# Category model
class Categories(models.Model):
    icon = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


# Author model 
class Author(models.Model):
    author_profile = models.ImageField(upload_to="author/", null=True)
    name = models.CharField(max_length=200, null=True)
    about_author = models.TextField(null=True)

    def __str__(self):
        return self.name
    

# Course model
class Course(models.Model):
    STATUS = (
        ("Published", "Published"),
        ("Pending", "Pending"),
        ("Rejected", "Rejected"),
    )
    
    featured_image = models.ImageField(upload_to="featured_image/", null=True)
    featured_video = models.CharField(max_length=300, null=True)  
    title = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, null=True, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    price = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    slug = models.SlugField(max_length=500, null=True, blank=True, default="")
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.title
