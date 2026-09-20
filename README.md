# Clinic Booking — نظام حجوزات عيادة Django MVT (Solo Build)

![Django](https://img.shields.io/badge/Django-5.x-green) ![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple) ![EG-Phone](https://img.shields.io/badge/EG--phone-validated-orange)

صفحة هبوط + فورم حجز ذكي + إدارة مواعيد — **Django MVT + Bootstrap 5 + SQLite**. نفس كود تحقق الرقم المصري المستخدم في مشروع E-Shop.

## Demo
- Home: `http://127.0.0.1:8001/` (استخدم بورت مختلف عن المدونة لو مشغل الاتنين)
- Admin: `/admin/` — إدارة تخصصات ومواعيد (تأكيد/إلغاء/بحث/فلترة)
- Success: `/done/<id>/` بعد الحجز

## Features
- تحقق تلقائي من الرقم المصري (`010/011/012/015` + `+20`) مع رسالة عربية واضحة
- منع التاريخ الماضي + منع الحجز المكرر (نفس الرقم/اليوم)
- `Specialty` + `Appointment(status: pending/confirmed/cancelled)` + Admin actions
- صفحة نجاح برقم الحجز + تصميم RTL متجاوب

## Run (Windows)
```powershell
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py shell --command="exec(open('seed_demo.py',encoding='utf-8').read())"
python manage.py runserver 8001
```

## Models
```python
Specialty(name)
Appointment(name, phone[EG-validated], specialty[PROTECT], date[>=today], notes, status, created_at)
```

## Author
Solo build by **Mohamed Rashwan** — portfolio:
- E-Shop: https://github.com/Mohamed-Rashwan-Bonus/eshop-django
- Blog: https://github.com/Mohamed-Rashwan-Bonus/blog-dashboard-django
