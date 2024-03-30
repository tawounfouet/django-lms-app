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
    

class Level(models.Model):
    name = models.CharField(max_length=200, null=True)

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
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    price = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    slug = models.SlugField(max_length=500, null=True, blank=True, default="")
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.title




class What_you_will_learn(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    points = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.points
    

class Requirements(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    points = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.points


class Lesson(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,  null=True,)
    
    def __str__(self):
        return self.name + " - " + self.course.title
    

class Video(models.Model):
    serial_number = models.IntegerField(null=True)
    thumbnail = models.ImageField(upload_to="media/yt_thumbnail/", null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True)
    youtube_id = models.CharField(max_length=200, null=True)
    duration = models.CharField(max_length=200, null=True)
    preview = models.BooleanField(default=False)

    def __str__(self):
        return self.title
