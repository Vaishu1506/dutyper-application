"""
Check all users in database
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from accounts.models import User

users = User.objects.all()

print("=" * 60)
print("DATABASE USER COUNT")
print("=" * 60)
print(f"Total users: {users.count()}")
print()

print("Role breakdown:")
print(f"  Employees: {users.filter(role='employee').count()}")
print(f"  HR: {users.filter(role='hr').count()}")
print(f"  Managers: {users.filter(role='manager').count()}")
print()

print("=" * 60)
print("ALL USERS LIST")
print("=" * 60)
for u in users:
    print(f"{u.emp_id:15} - {u.first_name:15} {u.last_name:15} - Role: {u.role}")

print()
print("=" * 60)
print("MANAGER DASHBOARD CALCULATION")
print("=" * 60)
employees = users.filter(role='employee').count()
hr = users.filter(role='hr').count()
total_for_manager = employees + hr
print(f"Employees: {employees}")
print(f"HR: {hr}")
print(f"Total Staff (for Manager): {total_for_manager}")
print("=" * 60)
