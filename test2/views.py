from django.shortcuts import render
from .models import Person
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers


@api_view(['GET'])
def person_all(requets):
    vse_ludi = Person.objects.all()
    serializer = serializers.PersonSerializer(vse_ludi,many=True)
    return Response(serializer.data, status=200)

@api_view(['Get'])
def person_id(requests,pk):
    try:
        queryset = Person.objects.get(id=pk)
        serializer = serializers.PersonSerializer(queryset)
        print(serializer.data)
        return Response(serializer.data, status=404)
    except Person.DoesNotExist:
        return Response('человека по id {pk} нет',status=404)

@api_view(['POST'])
def person_create(request):
    serializer = serializers.PersonSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=201)

@api_view(['PUT', 'PATCH'])
def person_update(request,pk):
    try:
        person = Person.objects.get(id=pk)
        if request.method == 'PUT':
            serializer = serializers.PersonSerializer(instance=person, data=request.data)
        else:
            serializer= serializers.PersonSerializer(instance=person, data=request.data, partial = True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data,status=206)
    except Person.DoesNotExist:
        return Response('Does not exict',status=404)

@api_view(['DELETE'])
def person_delete(request,pk):
    try:
        person = Person.objects.get(id=pk)
        person.delete()
        return Response('deleted Ssuccessfulyy', status=204)
    except Person.DoesNotExist:
        return Response(f'This person with {pk} id does not exict!',status=404)
    
    





