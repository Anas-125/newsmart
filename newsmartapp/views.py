from asyncio.windows_events import NULL

# import statistics
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from grpc import StatusCode
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .serializers import (
    WebSearchingSerializer,
    CosineSimilaritySerializer,
    UserSerializer,
)
from .models import WebSearching, CosineSimilarity, User
from .websearching import searchingwebinput
from .cosine import cosinesimilarity
from django.http import JsonResponse


class WebSearchingViewSet(viewsets.ModelViewSet):
    serializer_class = WebSearchingSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
        return WebSearching.objects.all()

    def create(self, request, *args, **kwargs):
        query = request.data
        print(query)
        input_string = query["query"]
        output = searchingwebinput(input_string)
        serializer = WebSearchingSerializer(output, many=True)
        return Response(serializer.data)

    # def get(self,request):
    #     input_string = str(input("Enter string"))
    #     output = tasks.cosinesimilarity(input_string)
    #     # for i in output:
    #     #     print(i['title'])
    #     # objects = websearching.objects.all()
    #     serializer = websearchingSerializer(output , many=True)
    #     return Response(serializer.data)

    # def post(self):
    #     pass


# def func(request):
#     if request.method == "POST":
#         input_string = request.POST.get('name')
#         tasks.cosinesimilarity(input_string)
#         obj = websearching.objects.all()
#         # print(obj)
#         objects = {
#             'obj' : obj
#         }

#         # return redirect('websearching')

#     return render(request , 'websearching/index.html')


class CosineSimilarityViewSet(viewsets.ModelViewSet):
    serializer_class = CosineSimilaritySerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
        return CosineSimilarity.objects.all()

    def create(self, request, *args, **kwargs):
        # query = request.data["query"]
        # print(query)
        output = cosinesimilarity(request.data["query"])
        serializer = CosineSimilaritySerializer(output, many=True)
        return Response(serializer.data)


class UserSignupViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        # print(data["email"])

        # if not User.objects.get(email = data["email"]) is NULL:
        #     print("BC")
        # else:
        #     print("MC")

        User.objects.create(
            firstname=data["firstname"],
            lastname=data["lastname"],
            DOB=data["DOB"],
            email=data["email"],
            password=data["password"],
        ).save()

        # print(data)
        # output = {
        #     "firstname": data["firstname"],
        #     "lastname": data["lastname"],
        #     "DOB": data["DOB"],
        #     "email": data["email"],
        #     "password": data["password"],
        # }

        # print(output)

        serializer = UserSerializer(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        # if serializer.is_valid():
        #     # serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # # return Response(serializer.data)
        # return JsonResponse({"data": serializer.data})


class UserLoginViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):

        try:
            password = User.objects.get(email=request.data["email"])

        except ValueError:
            return JsonResponse({"err": "Email or password invalid"})

        else:
            if password:

                if str(password) == str(request.data["password"]):
                    return Response({"ok"})
                else:
                    return JsonResponse({"err": "Email or password invalid"})

            else:
                return JsonResponse({"err": "Email or password invalid"})

        # print(x)
