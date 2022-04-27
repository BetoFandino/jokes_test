
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

import response_codes
from . import operations


class JokeViewSet(viewsets.ModelViewSet):

    @action(methods=['get'], url_path='get', detail=False)
    def get_jokes(self, *args, **kwargs):
        return_code, list_jokes = operations.chuknorris_get(15)
        if return_code == response_codes.SUCCESS:
            list_jokes = operations.organize_list(list_jokes)
        return Response({
            'RETURN_CODE': return_code,
            'RETURN_CONTENT': list_jokes
        }, status=200)
