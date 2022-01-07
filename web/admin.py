from django.contrib import admin
from .models import Appoinment ,Banner,Service,Award,Book,Gallery,Update,doctorAvailable

# Register your models here.


admin.site.register(Appoinment)
admin.site.register(Banner)
admin.site.register(Service)
admin.site.register(Award)
admin.site.register(Book)
admin.site.register(Gallery) 


@admin.register(doctorAvailable)
class doctorAvailableAdmin(admin.ModelAdmin):
    list_display = ('day','fromTime','toTime')
    

@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('name',)}