from django.contrib import admin
from .models import Specialty, Appointment

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name','phone','specialty','date','status','created_at')
    list_filter = ('status','specialty','date')
    search_fields = ('name','phone')
    actions = ('make_confirmed','make_cancelled')
    @admin.action(description='تأكيد المواعيد المحددة')
    def make_confirmed(self, request, qs): qs.update(status='confirmed')
    @admin.action(description='إلغاء المواعيد المحددة')
    def make_cancelled(self, request, qs): qs.update(status='cancelled')
