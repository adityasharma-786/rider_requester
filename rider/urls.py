from django.conf.urls import url, include
from rider.views import RequesterClass, create_rider, get_matching_rider, rider_applied

urlpatterns = [
    url(r"^create-requester/$", RequesterClass.as_view(), name="create-requester"),
    url(r"^requester-listing/$", RequesterClass.as_view(), name="requester-listing"),
    url(r"^create-rider/$", create_rider, name="create-rider"),
    url(r"^matching-listing/$", get_matching_rider, name="matching-listing"),
    url(r"^applied-rider/$", rider_applied, name="applied-rider"),
]
