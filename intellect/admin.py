from django.contrib import admin

# Register your models here.
from .models import Post, Profile, Hvac, Door, Equipment, Metal

admin.site.site_header = "INTELLECT INNOVATION"
admin.site.site_title = "Admin Area of Intellect Innovation"
admin.site.index_title = "Intellect Innovation Platform"

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Hvac)
admin.site.register(Door)
admin.site.register(Equipment)
admin.site.register(Metal)
