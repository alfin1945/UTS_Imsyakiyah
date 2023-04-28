from UtsApp.models import jadwalModels
from rest_framework import serializers

class jadwalSerializer(serializers.ModelSerializer):
    class Meta:
        model =  jadwalModels
        fields = ['Tanggal','Imsyak','Subuh','Terbit','Dhuha','Dzuhur','Asar','Magrib','Isya']