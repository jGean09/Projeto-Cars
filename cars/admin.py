from django.contrib import admin
from cars.models import car, Brand


class BradAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand','factory_year','model_year','value')
    search_fields = ('model','brand')


admin.site.register(Brand,BradAdmin)
admin.site.register(car, CarAdmin)

