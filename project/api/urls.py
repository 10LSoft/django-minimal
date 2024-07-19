from django.urls import path
from ninja import NinjaAPI, Router

router = Router()
api = NinjaAPI()


@router.get("/")
def health_check(request):
    _ = request
    return {"message": "🚀 I am here! Quick and alive!"}


api.add_router("health-check/", router)

urlpatterns = [path("api/", api.urls)]
