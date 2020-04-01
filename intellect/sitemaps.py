from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Hvac, Door

class EquipmentSitemap(Sitemap):
    def items(self):
        return Equipment.objects.all()

class DoorSitemap(Sitemap):
    def items(self):
        return Door.objects.all()

class HvacSitemap(Sitemap):
    def items(self):
        return Hvac.objects.all()
