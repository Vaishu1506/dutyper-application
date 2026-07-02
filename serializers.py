from rest_framework import serializers
from .models import LeaveRequest

class LeaveRequestSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    emp_id = serializers.CharField(source='user.emp_id', read_only=True)
    department = serializers.CharField(source='user.department', read_only=True)

    class Meta:
        model = LeaveRequest
        fields = ['id', 'user', 'user_name', 'emp_id', 'department', 'leave_type',
                  'from_date', 'to_date', 'days', 'reason', 'status',
                  'rejection_reason', 'rejected_by', 'approved_by_hr',
                  'approved_by_manager', 'created_at']
        read_only_fields = ['id', 'created_at', 'user_name', 'emp_id', 
                           'department', 'status']

class ApplyLeaveSerializer(serializers.Serializer):
    leave_type = serializers.ChoiceField(choices=LeaveRequest.LEAVE_TYPE_CHOICES)
    from_date = serializers.DateField()
    to_date = serializers.DateField()
    reason = serializers.CharField(min_length=10)

    def validate(self, attrs):
        if attrs['to_date'] < attrs['from_date']:
            raise serializers.ValidationError("End date cannot be before start date")
        return attrs
