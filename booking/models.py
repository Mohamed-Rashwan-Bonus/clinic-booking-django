import re
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

EG_PHONE = re.compile(r'^(\+20|0)?1[0125][0-9]{8}$')

def validate_eg_phone(v):
    if not EG_PHONE.match(v or ''):
        raise ValidationError('رقم مصري غير صحيح — مثال: 01001234567 أو +201001234567')

class Specialty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self): return self.name

class Appointment(models.Model):
    STATUS = [('pending','قيد المراجعة'),('confirmed','مؤكد'),('cancelled','ملغي')]
    name = models.CharField(max_length=120, verbose_name='الاسم')
    phone = models.CharField(max_length=15, validators=[validate_eg_phone], verbose_name='الموبايل')
    specialty = models.ForeignKey(Specialty, on_delete=models.PROTECT, verbose_name='التخصص')
    date = models.DateField(verbose_name='التاريخ')
    notes = models.TextField(blank=True, verbose_name='ملاحظات')
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: ordering = ['-created_at']
    def clean(self):
        super().clean()
        if self.date and self.date < timezone.localdate():
            raise ValidationError({'date': 'التاريخ لا يمكن أن يكون في الماضي'})
        if self.pk is None and Appointment.objects.filter(phone=self.phone, date=self.date).exists():
            raise ValidationError('يوجد حجز بنفس الرقم في نفس اليوم بالفعل')
    def __str__(self): return f"{self.name} — {self.specialty} — {self.date}"
