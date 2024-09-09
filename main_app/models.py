from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Comments(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    sec_title = models.CharField(max_length=100)
    sec_description = models.TextField()
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Category)
    authors = models.ManyToManyField(Author)
    comments = models.ManyToManyField(Comments)


class About(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Resume(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
    date = models.DateField()
    profession = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Services(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
    image = models.ImageField(upload_to='services/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Skills(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
    skill_name = models.CharField(max_length=100)
    persentage = models.IntegerField()

    def __str__(self):
        return self.title

class Projects(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
    image = models.ImageField(upload_to='projects/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class MyBlog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
    image = models.ImageField(upload_to='blog/')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
    image = models.ImageField(upload_to='contact/')
    name = models.CharField(max_length=100)
    sub_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Home(models.Model):
#     title = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.title