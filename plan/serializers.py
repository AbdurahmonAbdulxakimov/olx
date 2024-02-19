from rest_framework import serializers 

from plan.models import Plan, PlanDetail


class PlanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanDetail
        fields = (
            'id',
            'group',
            'code',
            'choice_text',
            "amount"
        )


class PlanSerializer(serializers.ModelSerializer):
    detail = PlanDetailSerializer()
    
    class Meta:
        model = Plan
        fields = (
            'id',
            'title',
            'detail',
        )