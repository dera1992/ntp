from rest_framework import viewsets, generics

from rest_framework.response import Response

from home.models import Region, State, Lga, Center
from home.serializers import RegionSerliazer, StateSerializer, LgaSerliazer, \
    CenterSerializer


class RegionViewSet(viewsets.ViewSet):

    def list(self,request):
        region=Region.objects.all()
        serializer=RegionSerliazer(region,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Region List Data","data":serializer.data}
        return Response(response_dict)


class StateViewset(viewsets.ViewSet):

    def list(self,request):
        state=State.objects.all()
        serializer=StateSerializer(state,many=True,context={"request":request})
        response_dict={"error":False,"message":"All State List Data","data":serializer.data}
        return Response(response_dict)


class LgaViewSet(viewsets.ViewSet):

    def list(self, request):
        lga = Lga.objects.all()
        serializer = LgaSerliazer(lga, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Lga List Data", "data": serializer.data}
        return Response(response_dict)


# Company Account Viewset
class CenterViewset(viewsets.ViewSet):

    def list(self, request):
        center = Center.objects.all()
        serializer = CenterSerializer(center, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Center List Data", "data": serializer.data}
        return Response(response_dict)


class StateNameByViewSet(generics.ListAPIView):
    serializer_class = StateSerializer
    def get_queryset(self):
        id=self.kwargs["id"]
        return State.objects.filter(region__id=id)

class  LgaByNameViewSet(generics.ListAPIView):
    serializer_class = LgaSerliazer
    def get_queryset(self):
        id = self.kwargs["id"]
        return Lga.objects.filter(state__id=id)

class  CenterByViewSet(generics.ListAPIView):
    serializer_class = CenterSerializer
    def get_queryset(self):
        id=self.kwargs["id"]
        return Center.objects.filter(lga__id=id)




