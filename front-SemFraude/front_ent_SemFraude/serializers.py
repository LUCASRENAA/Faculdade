from rest_framework import serializers
from front_ent_SemFraude.models import Lote,Produto,OrgaoDonatario,OrgaoFiscalizador


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class OrgaoDonatarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgaoDonatario
        fields = '__all__'

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'

class OrgaoFiscalizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgaoFiscalizador
        fields = '__all__'



class LoteSerializerCategory(serializers.ModelSerializer):
    orgaoDonatario = OrgaoDonatarioSerializer
    orgaoFiscalizador = OrgaoFiscalizadorSerializer
    class Meta:
        model = OrgaoFiscalizador
        fields = '__all__'

        depth = 1

class ProdutoSerializerCategory(serializers.ModelSerializer):
            orgaoDonatario = OrgaoDonatarioSerializer
            orgaoFiscalizador = OrgaoFiscalizadorSerializer

            class Meta:
                model = OrgaoFiscalizador
                fields = '__all__'

                depth = 1
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
