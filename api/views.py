from rest_framework.decorators import api_view
from rest_framework.response import Response
from .backend import AgroX_Intelligence

@api_view(['POST'])
def predict_hybrid(request):
    # 1. Get data from React
    plant_a = request.data.get('plant_a')
    plant_b = request.data.get('plant_b')
    model = AgroX_Intelligence()
    result = model.analyze_pair(plant_a, plant_b)
    return Response(result)
@api_view(['POST'])
def predict_single(request):
    # 1. Get data from React
    plant = request.data.get('plant')
    model = AgroX_Intelligence()
    result = model.find_best_match(plant)
    return Response(result)
@api_view(['GET'])
def ranks(request):
    model =AgroX_Intelligence()
    result = model.get_top_hybrids()
    return Response(result)
    