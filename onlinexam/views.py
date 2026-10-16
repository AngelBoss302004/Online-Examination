from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from onlinexam.models import QuestionDb
from onlinexam.serializer import OnlineExaminationSystemSerializer


# Create your views here.
class OnlineExaminationSystemView(APIView):
    def get(self,request):
        qs=QuestionDb.objects.all()
        Serializer_instance=OnlineExaminationSystemSerializer(qs,many=True)
        return Response(data=Serializer_instance.data)

    def post(self,request):
        form_data=request.data
        Serializer_instance=OnlineExaminationSystemSerializer(data=form_data)
        if Serializer_instance.is_valid():
            Serializer_instance.save()
        
            return Response(data={"message":"question added successfully"})
        else:
            return Response(Serializer_instance.errors,status=400)

class OnlineExamRetriveUpdateDeleteView(APIView):
    def get(self,request,pk):
        qs=QuestionDb.objects.get(id=pk)
        Serializer_instance=OnlineExaminationSystemSerializer(qs)
        return Response(data=Serializer_instance.data)

    def put(self,request,pk):
        form_data=request.data
        serializer_instance=OnlineExaminationSystemSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionDb.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
    def delete(self,request,pk):
        QuestionDb.objects.filter(id=pk).delete()

        return Response(
            {"message":"question deleted successfuly"}
        )