from django.contrib import admin


from .models import Worker,Client,Address,WorkerJob,Job,Service,Review,WorkerReview

class WorkerJobInline(admin.TabularInline):
    model=WorkerJob
class JobAdmin(admin.ModelAdmin):
    inlines=(WorkerJobInline,)

class WorkerReviewInline(admin.TabularInline):
    model=WorkerReview
class WorkerAdmin(admin.ModelAdmin):
    inlines=(WorkerReviewInline,)

admin.site.register(Worker,WorkerAdmin)
admin.site.register(Client)
admin.site.register(Address)
admin.site.register(Job,JobAdmin)
admin.site.register(Service)
admin.site.register(Review)
