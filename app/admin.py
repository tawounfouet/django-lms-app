from django.contrib import admin
from .models import Categories, Author, Level, Course, What_you_will_learn, Requirements, Lesson, Video

class what_you_learn_TabularInline(admin.TabularInline):
    model = What_you_will_learn
    extra = 2

class video_TabularInline(admin.TabularInline):
    model = Video
    extra = 2

class requirements_TabularInline(admin.TabularInline):
    model = Requirements
    extra = 2

class course_admin(admin.ModelAdmin):
    inlines = (what_you_learn_TabularInline, requirements_TabularInline, video_TabularInline)

# Register your models here.
admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Level)
admin.site.register(Course, course_admin)
# admin.site.register(What_you_will_learn)
admin.site.register(Requirements)
admin.site.register(Lesson)
admin.site.register(Video)
