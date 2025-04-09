from django.shortcuts import render
from .models import Usuario, Worker
from .serializers import UsuarioSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


def worker(req, token):

    user = Usuario.objects.get(token=token)

    return render(req, 'worker.html', context={
        'user': user,
        'token': token
    })

@csrf_exempt
@api_view(['POST'])
def get_user_confirmation(req, token):
    is_worker = req.data.get('is_worker')
    user = Usuario.objects.get(token=token)
    try: 
        if is_worker:
            user.token = None
            user.save()
            return Response(data={'usuario é um funcionario'}, status=status.HTTP_200_OK)
        else:
            Worker.objects.get(user=user).delete()
            user.token = None
            user.save()
            return Response(data={'usuario não é um funcionario'}, status=status.HTTP_204_NO_CONTENT)
    except ValueError as e:
        return Response(data={'error:' f"{str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        



