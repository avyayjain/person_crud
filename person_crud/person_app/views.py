from .models import BaseUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .password_helper import get_password_hash
from .serializers import PersonSerializer


# Create your user here in post type request
@api_view(['POST'])
def add_user(request):
    serializers = PersonSerializer(data=request.data)
    if serializers.is_valid():
        # check if user with this email or id already exists
        if BaseUser.objects.filter(email=request.data["email"]).exists():
            return Response({"message": "User with this email already exists"},
                            status=status.HTTP_400_BAD_REQUEST)
        if BaseUser.objects.filter(id=request.data["id"]).exists():
            return Response({"message": "User with this id already exists"},
                            status=status.HTTP_400_BAD_REQUEST)
        user = BaseUser()
        # user password is hashed before saving
        user.password = get_password_hash(request.data["password"])
        user.save()

    return Response({"message": "Successfully created user"},
                    status=status.HTTP_201_CREATED)


#get all users
@api_view(['GET'])
def return_all_users(request):
    users = BaseUser.objects.all()
    count = BaseUser.objects.count()
    serializers = PersonSerializer(users, many=True)
    return Response({"users": serializers.data, "total count of users ": count, }, status=status.HTTP_200_OK)

# get user by id
@api_view(['GET'])
def return_user_by_id(request, pk):
    if BaseUser.objects.filter(id=pk).exists():
        user = BaseUser.objects.get(id=pk)
        serializers = PersonSerializer(user)
        return Response(serializers.data, status=status.HTTP_200_OK)
    else:
        return Response({"message": f"user id {pk} does not exist"},
                        status=status.HTTP_404_NOT_FOUND)

# delete user by id
@api_view(['DELETE', 'GET'])
def delete_user_by_id(request, pk):
    if not BaseUser.objects.filter(id=pk).exists():
        return Response({"message": f"user id {pk} does not exist"},
                        status=status.HTTP_404_NOT_FOUND)
    user = BaseUser.objects.get(pk=pk)
    user.delete()
    return Response({"message": f"user id {pk} deleted successfully"},
                    status=status.HTTP_204_NO_CONTENT)
