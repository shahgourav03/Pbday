from django.contrib import admin
from .models import Friends, Family, Lovelies

# Register your models here.
admin.site.register(Friends)
admin.site.register(Family)
admin.site.register(Lovelies)