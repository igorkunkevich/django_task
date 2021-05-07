from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serialaizers import EmployeeListSerializer


class EmployeeListView(APIView):
    """Вывод списка работников"""
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeListSerializer(employee, many=True)
        return Response(serializer.data)
