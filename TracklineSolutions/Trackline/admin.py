from django.contrib import admin
from Trackline.models import Users,Rides,Articles
import Trackline

# Register your models here.
admin.site.register(Users)
admin.site.register(Rides)
admin.site.register(Articles)
