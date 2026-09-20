"""Seed clinic: specialties. Run: python manage.py shell --command="exec(open('seed_demo.py',encoding='utf-8').read())" """
from booking.models import Specialty
for name in ['أسنان', 'جلدية', 'أطفال', 'عظام', 'باطنة']:
    Specialty.objects.get_or_create(name=name)
print('clinics seeded:', Specialty.objects.count())
