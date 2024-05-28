from django.db import models

class Hobby(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    hobby = models.ForeignKey(Hobby,on_delete=models.CASCADE,related_name='hoby')
    phone = models.IntegerField()
    image = models.ImageField(upload_to='student_images')

    def __str__(self):
        return f"{self.name}"


