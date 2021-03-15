from rest_framework import serializers

from home.models import Region, State, Lga, Center


class RegionSerliazer(serializers.ModelSerializer):
    class Meta:
        model=Region
        fields="__all__"


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model=State
        fields="__all__"

    # def to_representation(self, instance):
    #     response=super().to_representation(instance)
    #     response['company']=CompanySerliazer(instance.company_id).data
    #     return response


class LgaSerliazer(serializers.ModelSerializer):
    class Meta:
        model=Lga
        fields="__all__"



class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Center
        fields="__all__"

