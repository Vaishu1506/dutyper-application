from django.db import models
from django.conf import settings

class LeaveRequest(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('CL', 'Casual Leave'),
        ('ML', 'Medical Leave'),
        ('EL', 'Earned Leave'),
        ('COMP-OFF', 'Compensatory Off'),
        ('OD', 'On Duty'),
        ('LWP', 'Leave Without Pay'),
    ]

    STATUS_CHOICES = [
        ('Pending HR', 'Pending HR'),
        ('Pending Manager', 'Pending Manager'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='leave_requests')
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
    from_date = models.DateField()
    to_date = models.DateField()
    days = models.IntegerField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending HR')
    rejection_reason = models.TextField(blank=True, null=True)
    rejected_by = models.CharField(max_length=100, blank=True, null=True)
    approved_by_hr = models.CharField(max_length=100, blank=True, null=True)
    approved_by_manager = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leave_requests'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.emp_id} - {self.leave_type} - {self.status}"
