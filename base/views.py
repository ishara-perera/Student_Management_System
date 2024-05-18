from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Subject
from base.serializers import SubjectSerializer


# Create
# @api_view(['POST'])
# def create_subject(request):
#     # Assuming 'name' is passed in the request body
#     name = request.data.get('name')
#     if name:
#         new_subject = Subject(name=name)
#         new_subject.save()
#         return Response({'id': new_subject.id, 'name': new_subject.name}, status=status.HTTP_201_CREATED)
#     return Response({'error': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_subject(request):
    # Create an instance of the serializer with the data received
    serializer = SubjectSerializer(data=request.data)

    # Check if the data is valid based on the serializer
    if serializer.is_valid():
        # Save the new subject to the database
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # If the data is not valid, return an error response
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Read (List)
@api_view(['GET'])
def get_subjects(request):
    subjects = Subject.objects.all().values('id', 'name')
    return Response(subjects)


# Read (Single)
@api_view(['GET'])
def get_subject(request, subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
        return Response({'id': subject.id, 'name': subject.name})
    except Subject.DoesNotExist:
        return Response({'error': 'Subject not found'}, status=status.HTTP_404_NOT_FOUND)


# Update
@api_view(['PUT', 'PATCH'])
def update_subject(request, subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
        name = request.data.get('name')
        if name:
            subject.name = name
            subject.save()
            return Response({'id': subject.id, 'name': subject.name})
        return Response({'error': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)
    except Subject.DoesNotExist:
        return Response({'error': 'Subject not found'}, status=status.HTTP_404_NOT_FOUND)


# Delete
@api_view(['DELETE'])
def delete_subject(request, subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Subject.DoesNotExist:
        return Response({'error': 'Subject not found'}, status=status.HTTP_404_NOT_FOUND)
