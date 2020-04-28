from django.contrib import admin
from .models import Worker,Client,Address,Job,Service,Review

admin.site.register(Worker)
admin.site.register(Client)
admin.site.register(Address)
admin.site.register(Job)
admin.site.register(Service)
admin.site.register(Review)
