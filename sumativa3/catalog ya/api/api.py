from ninja import NinjaAPI, Redoc


api = NinjaAPI(docs=Redoc())

@api.get("/dummy")
def get_dummys(request):
    data={
        'exemple':'hola profe'
    }
    return data
