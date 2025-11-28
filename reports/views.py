from collections import Counter
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import SummaryReportSerializer, UserReportSerializer, UserSerializer, VideoSerializer
from .services import fetch_users, fetch_videos, fetch_user_by_id, fetch_user_videos

class ReportViewSet(ViewSet):
    # GET /report/summary
    def summary(self, request):
        try:
            users = fetch_users()
            videos = fetch_videos()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)

        total_users = users["pagination"]["total"] if "pagination" in users else 0
        total_videos = videos["pagination"]["total"] if "pagination" in videos else 0
        categories = [v.get("category") for v in videos['videos'] if v.get("category")]
        counts = Counter(categories)
        top = [{"category": k, "count": v} for k, v in counts.most_common(5)]

        payload = {
            "totalUsers": total_users,
            "totalVideos": total_videos,
            "topCategories": top,
        }
        serializer = SummaryReportSerializer(payload)
        return Response(serializer.data)

    # GET /report/user/<id>
    def user(self, request, pk=None):
        try:
            user = fetch_user_by_id(int(pk))
            if not user:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            videos = fetch_user_videos(int(pk))
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)

        totals = {
            "videoCount": len(videos),
            "categories": Counter([v.get("category") for v in videos if v.get("category")]),
        }

        payload = {
            "user": user,
            "totals": {k: (dict(v) if not isinstance(v, int) else v) for k, v in totals.items()},
            "videos": videos,
        }

        serializer = UserReportSerializer(payload)
        return Response(serializer.data)