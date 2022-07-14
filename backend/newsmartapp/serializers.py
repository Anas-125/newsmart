from rest_framework import serializers
from .models import CosineSimilarity, WebSearching, User


class CosineSimilaritySerializer(serializers.ModelSerializer):
    class Meta:
        model = CosineSimilarity
        fields = "__all__"


class WebSearchingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebSearching
        # fields = ('link' , 'title' , 'score' , 'angle')
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    # id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # firstname = serializers.StringRelatedField(many=True, read_only=True)
    # lastname = serializers.StringRelatedField(many=True, read_only=True)
    # email = serializers.StringRelatedField(many=True, read_only=True)
    # password = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        # fields = ["id", "firstname", "lastname", "DOB", "email", "password"]
        fields = "__all__"


class WordListingField(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value
