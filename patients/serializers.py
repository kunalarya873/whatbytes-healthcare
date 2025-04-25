from rest_framework import serializers
from patients.models import Patient
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['created_by']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().update(instance, validated_data)
    
    