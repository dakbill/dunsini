from rest_framework.response import Response
from rest_framework.decorators import api_view
from diagnoser import doctor


@api_view(['GET'])
def pong(request):
	return Response({'message':'pong'})

@api_view(['POST'])
def consult(request):
	data = request.data
	case = data.get('case',None)
	
	if case:
		message = doctor.remedy(case.lower())
	else:
		message = [{'message':'Please state your [case]'}]
	return Response(message)
