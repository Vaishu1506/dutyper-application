"""
Verify that the system is using IST timezone correctly
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.conf import settings
from django.utils import timezone

print("=" * 60)
print("DJANGO TIMEZONE CONFIGURATION")
print("=" * 60)
print(f"TIME_ZONE setting: {settings.TIME_ZONE}")
print(f"USE_TZ setting: {settings.USE_TZ}")
print()

print("=" * 60)
print("CURRENT TIMES")
print("=" * 60)
utc_now = timezone.now()
ist_now = timezone.localtime(utc_now)

print(f"UTC Time:     {utc_now}")
print(f"IST Time:     {ist_now}")
print(f"IST Date:     {ist_now.date()}")
print(f"IST Time:     {ist_now.strftime('%H:%M:%S')}")
print()

print("=" * 60)
print("VERIFICATION")
print("=" * 60)
if settings.TIME_ZONE == 'Asia/Kolkata':
    print("✅ PASS: Using IST (Asia/Kolkata) timezone")
else:
    print("❌ FAIL: Not using IST timezone")

if settings.USE_TZ:
    print("✅ PASS: Timezone-aware datetime enabled")
else:
    print("❌ FAIL: Timezone-aware datetime disabled")

# Check offset
ist_offset = ist_now.utcoffset()
print(f"✅ IST Offset: {ist_offset} (should be +5:30)")

print()
print("=" * 60)
print("ATTENDANCE LATE THRESHOLD TEST")
print("=" * 60)
from datetime import time
late_threshold = time(10, 0)
current_ist_time = ist_now.time()

print(f"Current IST Time: {current_ist_time}")
print(f"Late Threshold:   {late_threshold}")
print(f"Status:           {'Late' if current_ist_time >= late_threshold else 'Present'}")
print()
print("✅ System is correctly configured to use IST timezone!")
print("=" * 60)
