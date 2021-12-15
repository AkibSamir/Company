from django.db import models

# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='slider', blank=True, null=True)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=200, blank=False)
    short_intro = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True, null=True)
    key = models.CharField(max_length=200, blank=True)
    conclusion = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length=200, blank=False)
    designation = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to="team", blank=False, null=False)
    social_facebook = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_instagram = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    

    def __str__(self):
        return self.name

class Skill(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    percentage = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.title

class Client(models.Model):
    logo = models.ImageField(upload_to="clients", blank=False, null=False)
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Testomonial(models.Model):
    name = models.CharField(max_length=100, blank=False)
    designation = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="testimonial", blank=True)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    short_title = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="portfolio", blank=True)
    slider1 = models.ImageField(upload_to="portfolio", blank=True)
    slider2 = models.ImageField(upload_to="portfolio", blank=True)
    slider3 = models.ImageField(upload_to="portfolio", blank=True)
    category = models.CharField(max_length=100, blank=True)
    client = models.CharField(max_length=100, blank=True)
    project_url = models.CharField(max_length=100, blank=True)
    project_date = models.DateField(auto_now_add=False)


    def __str__(self):
        return self.short_title