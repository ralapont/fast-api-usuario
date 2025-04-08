from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm

from fastapi.logger import logger as fastapi_logger

from app.v1.schema import user_schema
from app.v1.service import user_service
from app.v1.service import auth_service
from app.v1.schema.token_schema import Token

from app.v1.utils.db import get_db


router = APIRouter(
    prefix="/api/v1",
    tags=["users"]
)

@router.post(
    "/user",
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Create a new user"
)
def create_user(user: user_schema.UserRegister = Body(...)):
    """
    ## Create a new user in the app

    ### Args
    The app can receive next fields into a JSON
    - email: A valid email
    - username: Unique username
    - password: Strong password for authentication

    ### Returns
    - user: User info
    """
    return user_service.create_user(user)

@router.get(
    "/user",
    status_code=status.HTTP_200_OK,
    response_model=list[user_schema.User],
    dependencies=[Depends(get_db)],
    summary="get all users"
)
def get_users():
    """
    ## Get the users in the app

    ### Returns
    - users: List of Users with the info
    """
    return user_service.get_users()

@router.get(
    "/user/{id}",
    tags=["user"],
    status_code=status.HTTP_200_OK,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)]
)
def get_user(id: int):
    """
    ## Get user by Id

    ### Args
    The app can receive next fields into path variable
    - id: id of the user

    ### Returns
    - user: User info
    """
    fastapi_logger.info(f"Get user with id {id}")
    return user_service.get_user(id)

@router.put(
    "/user/{id}",
    tags=["user"],
    status_code=status.HTTP_200_OK,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)]
)
def modify_user(id: int, user: user_schema.UserRegister = Body(...)):
    """
    ## Modify user by Id

    ### Args
    The app can receive next fields
    - id: id of the user
    - user: The app can receive next fields into a JSON
        - email: A valid email
        - username: Unique username
        - password: Strong password for authentication

    ### Returns
    - user: User info
    """
    fastapi_logger.info(f"Modify user with id {id}")
    return user_service.modify_user(id, user)

@router.delete(
    "/user/{id}",
    tags=["user"],
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(get_db)]
)
def delete_user(id: int):
    """
    ## Delete user by Id

    ### Args
    The app can receive next fields
    - id: id of the user

    """
    fastapi_logger.info(f"Delete user with id {id}")
    user_service.delete_user(id)


@router.post(
    "/login",
    response_model=Token
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    ## Login for access token

    ### Args
    The app can receive next fields by form data
    - username: Your username or email
    - password: Your password

    ### Returns
    - access token and token type
    """
    access_token = auth_service.generate_token(form_data.username, form_data.password)
    return Token(access_token=access_token, token_type="bearer")