from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import Poll, Option, Vote
from .serializers import PollSerializer, OptionSerializer

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        poll = self.get_object()
        option_id = request.data.get('option_id')
        user = request.user

        try:
            option = poll.options.get(id=option_id)
        except Option.DoesNotExist:
            return Response({"error": "Option not found."}, status=status.HTTP_404_NOT_FOUND)

        if Vote.objects.filter(user=user, option__poll=poll).exists():
            return Response({"error": "You have already voted in this poll."}, status=status.HTTP_400_BAD_REQUEST)

        Vote.objects.create(user=user, option=option)
        return Response({"success": "Vote cast successfully."})

    @action(detail=True, methods=['get'])
    def results(self, request, pk=None):
        poll = self.get_object()
        serializer = OptionSerializer(poll.options.all(), many=True)
        return Response(serializer.data)
