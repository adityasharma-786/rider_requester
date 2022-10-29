from datetime import datetime
from rider.constants import allowed_flags, allowed_asset_type, allowed_asset_sensitivity, allowed_requester_status, allowed_travel_mediums


def requester_dict_validator(data):
    if not data.get("from_location"):
        raise Exception("From location is mandatory.")
    if not data.get("to_location"):
        raise Exception("To location is mandatory.")
    if not data.get("asset_type"):
        raise Exception("Asset Type is mandatory.")
    if not data.get("asset_sensitivity"):
        raise Exception("Asset Sensitivity is mandatory.")
    if not data.get("whom_to_deliver"):
        raise Exception("Whom To Deliver is mandatory.")
    if not data.get("no_of_assets"):
        raise Exception("Number of assets is mandatory.")
    if not data.get("date_time"):
        raise Exception("Date Time is mandatory.")
    if str(data.get("is_flexible")).upper() not in allowed_flags:
        raise Exception(f"Allowed Flexible Flag are - {allowed_flags}")
    if data["asset_type"].upper() not in allowed_asset_type:
        raise Exception(f"Allowed Asset Types are - {allowed_asset_type}")
    if data.get("asset_sensitivity").upper() not in allowed_asset_sensitivity:
        raise Exception(f"Allowed Asset Sensitivities are - {allowed_asset_sensitivity}")
    try:
        data["date_time"] = datetime.strptime(data["date_time"], "%Y-%m-%d %H:%M:%S")
    except:
        raise Exception("Please enter valid date time format")
    try:
        data["no_of_assets"] = int(data["no_of_assets"])
        if data["no_of_assets"] < 1:
            raise Exception("Number of assets cannot be zero or negative")
    except:
        raise Exception("Please enter valid Integer for number of assets")  
    return data

def rider_dict_validator(data):
    if not data.get("from_location"):
        raise Exception("From location is mandatory.")
    if not data.get("to_location"):
        raise Exception("To location is mandatory.")
    if not data.get("no_of_assets"):
        raise Exception("Number of assets is mandatory.")
    if not data.get("date_time"):
        raise Exception("Date Time is mandatory.")
    if not data.get("travel_medium"):
        raise Exception("Travel Medium is mandatory.")
    if data["travel_medium"].upper() not in allowed_travel_mediums:
        raise Exception(f"Allowed Travel Medium are - {allowed_travel_mediums}")
    if str(data.get("is_flexible")).upper() not in allowed_flags:
        raise Exception(f"Allowed Flexible Flag are - {allowed_flags}")
    try:
        data["date_time"] = datetime.strptime(data["date_time"], "%Y-%m-%d %H:%M:%S")
    except:
        raise Exception("Please enter valid date format")
    try:
        data["no_of_assets"] = int(data["no_of_assets"])
        if data["no_of_assets"] < 1:
            raise Exception("Number of assets cannot be zero or negative")
    except:
        raise Exception("Please enter valid integer for number of assets")  
    return data


def requester_get_dict_validator(status, asset_type):
    if status and status.upper() not in allowed_requester_status:
        raise Exception(f"Valid Status are - {allowed_requester_status}")
    if asset_type and asset_type.upper() not in allowed_asset_type:
        raise Exception(f"Allowed Asset Types are - {allowed_asset_type}")

def matching_rider_validator(data):
    if not data.get("from_location"):
        raise Exception("From location is mandatory.")
    if not data.get("to_location"):
        raise Exception("To location is mandatory.")
    if not data.get("date"):
        raise Exception("Date is mandatory.")
    try:
        date_time = datetime.strptime(data["date"], "%Y-%m-%d %H:%M:%S")
        data['date'] = date_time.date()
    except:
        raise Exception("Please enter valid date format")
    return data
    
def applied_rider_validator(data):
    if not data.get("rider_id"):
        raise Exception(f"Rider ID is mandatory.")
    if not data.get("requester_id"):
        raise Exception(f"Requester ID is mandatory.")

def response_structure(code=200, message="Success", details=""):
    return {"code": code, "message": message, "details": details}

# def create_requester_dict(data):
#     request_dict = dict()
#     request_dict["from_location"] = data["from_location"]
#     request_dict["to_location"] = data["to_location"]
#     request_dict["date_time"] = data["date_time"]
#     request_dict["is_flexible"] = True if str(data["is_flexible"]).upper() == "TRUE" else False
#     request_dict["no_of_assets"] = data["no_of_assets"]
#     request_dict["asset_type"] = data["asset_type"]
#     request_dict["asset_sensitivity"] = data["asset_sensitivity"]
#     request_dict["whom_to_deliver"] = data["whom_to_deliver"]
#     request_dict["status"] = 'Pending'
#     return request_dict
    
    