from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.shortcuts import reverse


class Profile(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='images', help_text='image should be Height = 480px, Width = 480px')
    description = RichTextField(default='about profile details')

    def __str__(self):
        return self.title

class Hvac(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='images', help_text='image should be Height = 560px, Width = 480px')
    post_short_description = models.TextField(default='This area write image short description')
    post_long_description = RichTextUploadingField(default='This area write image in brief text description')
    slug = models.SlugField(blank=True, null=True)

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("intellect:hvacDetail", kwargs={
            'slug' : self.slug
        })

class Door(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='images', help_text='image should be Height = 480px, Width = 480px')
    post_short_description = models.TextField(default='This area write image short description')
    post_long_description = RichTextUploadingField(default='This area write image in brief text description')
    slug = models.SlugField(blank=True, null=True)


    def __str__(self):
        return self.title

    def get_absolutel_url(self):
        return reverse("intellect:doorDetail", kwargs={
            'slug' : self.slug
        })

class Equipment(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='images', help_text='image should be Height = 480px, Width = 480px')
    post_short_description = models.TextField(default='This area write image short description')
    post_long_description = RichTextUploadingField(default='This area write image in brief text description')
    slug = models.SlugField(blank = True, null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("intellect:equipmentDetail", kwargs = {
            'slug' : self.slug
        })

class Metal(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='images', help_text='image should be Height = 480px, Width = 480px')
    post_short_description = models.TextField(default='This area write image short description')
    post_long_description = RichTextUploadingField(default='This area write image in brief text description')
    slug = models.SlugField(blank = True, null = True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("intellect:metalDetail", kwargs = {
            'slug' : self.slug
        })


class Post(models.Model):
    title = models.CharField(max_length=200)
    post_image = models.FileField(upload_to='images', help_text='image should be Height = 480px, Width = 560px')
    post_short_description = models.TextField(default='This area write image short description')
    post_long_description = RichTextUploadingField(default='This area write image in brief text description')
    slug = models.SlugField(blank=True, null=True)
    
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("intellect:product", kwargs={
            'slug' : self.slug
        })

