from django.contrib import admin


from .models import Worker,Client,Job,Service,Review,Applicant



admin.site.register(Worker)
admin.site.register(Client)
admin.site.register(Job)
admin.site.register(Service)
admin.site.register(Review)
admin.site.register(Applicant)
