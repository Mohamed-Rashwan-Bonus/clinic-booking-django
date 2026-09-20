#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py shell --command="from booking.models import Specialty; [Specialty.objects.get_or_create(name=n) for n in ['أسنان','جلدية','أطفال','عظام','باطنة']]"
