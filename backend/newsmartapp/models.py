from django.db import models


# Create your models here.


class CosineSimilarity(models.Model):
    title = models.TextField()
    link = models.CharField(max_length=120)
    score = models.TextField()
    angle = models.TextField()

    def __str__(self):
        return self.link


class WebSearching(models.Model):
    title = models.TextField()
    link = models.CharField(max_length=120)
    text = models.TextField(default="")
    # angle = models.TextField()

    def __str__(self):
        return self.link


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstname = models.CharField(default="", max_length=100, blank=True)
    lastname = models.CharField(default="", max_length=100, blank=True)
    DOB = models.DateField(blank=True)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return "{}".format(self.password)
        # return self.password
