# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from .models import Cat
# from .serializers import CatSerializer


# @api_view(['GET', 'POST'])
# def cat_list(request):
#     if request.method == 'POST':
#         serializer = CatSerializer(data=request.data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     cats = Cat.objects.all()
#     serializer = CatSerializer(cats, many=True)
#     print(f'1                {cats}')
#     print(f'2  {serializer}')
#     print(f'3  {serializer.data}')
#     return Response(serializer.data)


####################### 1 Обновлённый views.py ##################################
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView

# from .models import Cat
# from .serializers import CatSerializer


# class APICat(APIView):
#     def get(self, request):
#         cats = Cat.objects.all()
#         serializer = CatSerializer(cats, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


######################### 2 Обновлённый еще раз views.py ########################
# from rest_framework import generics

# from .models import Cat
# from .serializers import CatSerializer


# class CatList(generics.ListCreateAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


# class CatDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer

################### 3 обновленный в третий раз views.py #########################
from rest_framework import viewsets

from .models import Cat
from .serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
