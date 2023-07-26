from fastapi import APIRouter

router = APIRouter(
    prefix="/test1",
    tags=["test1"]
)



@router.get("/first_method")
def first_method():
    return {"message":"This is first method of test1"}


@router.get("/second_method")
def second_method():
    return {"message":"This is second method of test1"}
