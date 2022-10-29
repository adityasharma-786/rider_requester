# from django.shortcuts import render
from datetime import datetime
import pytz
from validations import response_structure, requester_dict_validator, requester_get_dict_validator, rider_dict_validator, matching_rider_validator, applied_rider_validator
from rider.models import Requester, Rider
from serializers import RequesterDataSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class RequesterClass(APIView):
    def post(self, request):
        try:
            input_data = request.data
            if not input_data:
                response = response_structure(code=300, message='Failed', details='Please Enter Valid Data')
                return Response(response)
            data = requester_dict_validator(input_data)
            create_requester(data)
            response = response_structure()
            return Response(response) 
        except Exception as e:
            return Response(response_structure(code=300, message='Failed', details=str(e)))

    def get(self, request):
        try:
            status = request.GET.get("status")
            asset_type = request.GET.get("asset_type")
            requester_get_dict_validator(status,asset_type)
            Requester.objects.filter(date_time__lt=datetime.now(tz=pytz.timezone("Asia/Calcutta"))).update(status="EXPIRED")
            requester_obj = Requester.objects.all()
            if status:
                requester_obj.filter(status=status)
            if asset_type:
                requester_obj.filter(asset_type=asset_type)
            paginator = PageNumberPagination()
            paginator.page_size = 25
            details = paginator.paginate_queryset(requester_obj, request)
            return paginator.get_paginated_response(
                {
                    "code": 200,
                    "data": RequesterDataSerializer(details, many=True).data
                }
            )
        except Exception as e:
            return Response(response_structure(code=300, message='Failed', details=str(e)))



def create_requester(data):
    Requester.objects.create(
        from_location = data["from_location"],
        to_location = data["to_location"],
        date_time = data["date_time"],
        is_flexible = True if str(data["is_flexible"]).upper() == "TRUE" else False,
        no_of_assets = data["no_of_assets"],
        asset_type = data["asset_type"],
        asset_sensitivity = data["asset_sensitivity"],
        whom_to_deliver = data["whom_to_deliver"],
        status = 'PENDING'
    )

@api_view(["POST"])
def create_rider(request):
    try:
        input_data = request.data
        if not input_data:
                response = response_structure(code=300, message='Failed', details='Please Enter Valid Data')
                return Response(response)
        data = rider_dict_validator(input_data)
        create_rider_entry(data)
        response = response_structure()
        return Response(response) 
    except Exception as e:
        return Response(response_structure(code=300, message='Failed', details=str(e)))

def create_rider_entry(data):
    Rider.objects.create(
        from_location = data["from_location"],
        to_location = data["to_location"],
        date_time = data["date_time"],
        is_flexible = True if str(data["is_flexible"]).upper() == "TRUE" else False,
        no_of_assets = data["no_of_assets"],
        travel_medium = data["travel_medium"]
    )

@api_view(["GET"])
def get_matching_rider(request): #write this code
    try:
        input_data = request.data
        if not input_data:
                response = response_structure(code=300, message='Failed', details='Please Enter Valid Data')
                return Response(response)
        data = matching_rider_validator(input_data)
        create_rider(data)
        response = response_structure()
        return Response(response) 
    except Exception as e:
        return Response(response_structure(code=300, message='Failed', details=str(e)))

@api_view(["PUT"])
def rider_applied(request): #write this code
    try:
        input_data = request.data
        if not input_data:
                response = response_structure(code=300, message='Failed', details='Please Enter Valid Data')
                return Response(response)
        applied_rider_validator(input_data)
        r_obj = Rider.objects.filter(id=input_data['id']).update(is_applied=True, status='APPLIED')
        if not r_obj:
            raise Exception(F"No Valid Data Found WITH this ID - {input_data['id']}")
        response = response_structure()
        return Response(response) 
    except Exception as e:
        return Response(response_structure(code=300, message='Failed', details=str(e)))


    

        
