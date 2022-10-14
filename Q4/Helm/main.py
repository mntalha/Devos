from fastapi import FastAPI, APIRouter


class HelmClass:

    def __init__(self, comment: str):
        self.comment = comment
        self.router = APIRouter()
        self.router.add_api_route("/initiate", self.called, methods=["GET"])

    def called(self):
        return {self.comment}

app = FastAPI()
hello = HelmClass("Microservice is successfully triggered")
app.include_router(hello.router)