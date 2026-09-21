"""Seed physio version: run after migrate. python manage.py shell --command="exec(open('seed_physio.py',encoding='utf-8').read())" """
from booking.models import Specialty
for name in ['كشف إصابات', 'تأهيل ركبة', 'إصابات كتف', 'تأهيل بعد عملية', 'جلسة أونلاين']:
    Specialty.objects.get_or_create(name=name)
print('physio seeded:', Specialty.objects.count())
