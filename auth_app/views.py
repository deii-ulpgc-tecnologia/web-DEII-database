from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CheckGroupView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        group_name = request.query_params.get("group")

        if not group_name:
            return Response(
                {"error": "El parámetro 'group' es obligatorio"},
                status=400
            )

        belongs = request.user.groups.filter(name=group_name).exists()

        return Response({
            "group": group_name,
            "belongs": belongs
        })