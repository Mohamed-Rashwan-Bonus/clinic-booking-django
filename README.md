# نظام حجوزات عيادة — Django

الفكرة جت من مشروع المتجر: كنت عامل تحقق الرقم المصري (+20) هناك، وقلت أطلع منه نظام حجوزات صغير ينفع لأي عيادة أو مركز.

## بيشتغل إزاي
- صفحة واحدة فيها Hero + فورم حجز (اسم/موبايل/تخصص/تاريخ/ملاحظات)
- بعد الحجز بيفتح صفحة تأكيد فيها رقم الحجز والتخصص واليوم
- الدكتور بيدير كل حاجة من `/admin/` (بحث بالاسم/الموبايل + فلترة بالتخصص والحالة + أكشن تأكيد/إلغاء)

## شوية تفاصيل
- الرقم المصري بيتحقق منه بـ regex يقبل `010/011/012/015` و `+20`، ورسالة الخطأ بالعربي
- التاريخ الماضي مرفوض، ونفس الرقم ميحجزش مرتين في نفس اليوم
- التخصصات بتتزرع من `seed_demo.py` (أسنان/جلدية/أطفال/عظام/باطنة)

## التشغيل
```powershell
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py shell --command="exec(open('seed_demo.py',encoding='utf-8').read())"
python manage.py runserver 8001
```
استخدمت بورت 8001 عشان لو مشغل المدونة على 8000 في نفس الوقت.

## الملفات المهمة
`booking/models.py` (التحقق + clean) — `booking/forms.py` — `booking/admin.py` (الأكشنز) — `templates/booking/home.html`

## مشاريعي التانية
- المتجر: https://github.com/Mohamed-Rashwan-Bonus/eshop-django
- المدونة: https://github.com/Mohamed-Rashwan-Bonus/blog-dashboard-django

محمد رشوان — Django Full-Stack (القاهرة)
