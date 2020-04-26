from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from babies.models import Baby
from events.models import Event
from babies.serializers import BabySerializer
from events.serializers import EventSerializer

def evaluateParent(user, request):
    babyPk = (request.POST).get('baby', 0)
    baby = Baby.objects.filter(pk=babyPk)[0]
    return user.username == baby.parent.username

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='BabyPermission',
            permission_configuration={
                'base': {
                    'create': evaluateParent,
                    'list': False,
                },
                'instance': {
                    'retrieve': 'events.view_event',
                    'destroy': 'events.delete_event',
                    'update': 'events.change_event',
                    'partial_update': 'events.change_event'
                }
            }
        ),
    )

    def perform_create(self, serializer):
        event = serializer.save()
        user = self.request.user
        assign_perm('events.view_event', user, event)
        assign_perm('events.change_event', user, event)
        assign_perm('events.delete_event', user, event)
        return Response(serializer.data)
