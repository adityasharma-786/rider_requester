from django.conf.urls import url, include
from rider.views import RequesterClass

urlpatterns = [
    url(r"^requester-create/$", RequesterClass.as_view(), name="requester-create/"),
    url(r"^requester-listing/$", RequesterClass.as_view(), name="requester-listing/"),


]
