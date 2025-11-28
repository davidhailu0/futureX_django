from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()
    avatarUrl = serializers.CharField(allow_null=True, required=False)

class VideoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    userId = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField(allow_null=True, required=False)
    youtubeId = serializers.CharField()
    category = serializers.CharField(allow_null=True, required=False)
    duration = serializers.IntegerField(allow_null=True, required=False)

class SummaryReportSerializer(serializers.Serializer):
    totalUsers = serializers.IntegerField()
    totalVideos = serializers.IntegerField()
    topCategories = serializers.ListField(child=serializers.DictField())

class UserReportSerializer(serializers.Serializer):
    user = UserSerializer()
    totals = serializers.DictField()
    videos = VideoSerializer(many=True)