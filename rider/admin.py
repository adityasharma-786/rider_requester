from django.contrib import admin

# Register your models here.
from rider.models import Requester, Rider, RequesterRiderMapper

admin.site.register(Requester)
admin.site.register(Rider)
admin.site.register(RequesterRiderMapper)

