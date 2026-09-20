# Clinic Booking — نظام حجوزات عيادة Django MVT (Portfolio Project 3)

Solo build — Django + Bootstrap 5. أسهل مشروع يبيع على مستقل وخمسات (كل عيادة/مركز عايزه).

## الفكرة
صفحة هبوط + فورم حجز (اسم + رقم مصري + تخصص + معاد) + لوحة Admin للمواعيد + تحقق من الرقم المصري (عندك الكود جاهز من E-Shop).

## هتبنيه في يوم واحد — Checklist
- [ ] نفس setup مشروع المدونة
- [ ] Models:
```python
# booking/models.py
from django.db import models
import re

class Specialty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self): return self.name

class Appointment(models.Model):
    STATUS = [('pending','قيد المراجعة'),('confirmed','مؤكد'),('cancelled','ملغي')]
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)  # +20 validation
    specialty = models.ForeignKey(Specialty, on_delete=models.PROTECT)
    date = models.DateField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        # انسخ نفس regex تحقق الرقم المصري من مشروع E-Shop (accounts/validators)
        if not re.match(r'^(\+20|0)?1[0125][0-9]{8}$', self.phone):
            raise ValidationError('رقم مصري غير صحيح')
```
- [ ] Form بـ `ModelForm` + رسالة نجاح بعد الحجز + منع حجز مكرر لنفس الرقم/اليوم
- [ ] Admin: list_display (name, phone, specialty, date, status) + filter + search + action "تأكيد"
- [ ] Templates: Hero + مميزات + فورم حجز + صفحة "تم استلام طلبك" (انسخ ستايل E-Shop)
- [ ] سكرينين: الهبوط + جدول المواعيد في Admin

## Run
```powershell
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## للرفع على GitHub
repo جديد `clinic-booking-django` وادفع الكود + سكرينات.

## وصف جاهز لمستقل (انسخه)
> **نظام حجوزات عيادة - Django + Bootstrap**
> صفحة هبوط متجاوبة مع فورم حجز ذكي: تحقق تلقائي من الرقم المصري (+20)، منع التكرار، حفظ الموعد، وإدارة كاملة من Django Admin (تأكيد/إلغاء/بحث/فلترة بالتخصص). بناء فردي بالكامل.
