from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from babies.models import Baby
from events.models import Event
from babies.serializers import BabySerializer
from events.serializers import EventSerializer

def evaluateUser(user, obj, request):
    return user.username == obj.parent.username

class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='BabyPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': False,
                },
                'instance': {
                    'retrieve': 'babies.view_baby',
                    'destroy': 'babies.delete_baby',
                    'update': 'babies.change_baby',
                    'partial_update': 'babies.change_baby',
                    'events':evaluateUser
                }
            }
        ),
    )

    def perform_create(self, serializer):
        baby = serializer.save()
        user = self.request.user
        assign_perm('babies.view_baby', user, baby)
        assign_perm('babies.change_baby', user, baby)
        assign_perm('babies.delete_baby', user, baby)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def events(self, request, pk=None):
        baby = self.get_object()
        babyEvents=[]
        for event in Event.objects.filter(baby=baby):
            babyEvents.append(EventSerializer(event).data)
        return Response(babyEvents)

