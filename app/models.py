from django.db import models

from django.contrib.auth.models import User
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

class Language(models.Model):
    language = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.language


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
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)
    deadline = models.CharField(max_length=200, null=True, default="Lifetime Access", blank=True)
    slug = models.SlugField(max_length=500, null=True, blank=True, default="")
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    certificate = models.BooleanField(default=False, null=True, blank=True)
    is_featured = models.BooleanField(default=False, null=True, blank=True)

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

class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + " - " + self.course.title


# Payment model    
class Payment(models.Model):
    order_id = models.CharField(max_length=200, null=True, blank=True)
    payment_id = models.CharField(max_length=200, null=True, blank=True)
    user_course = models.ForeignKey(UserCourse, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
    payment_status = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.username + " - " + self.course.title + " - " + str(self.amount) + " - " + str(self.date)