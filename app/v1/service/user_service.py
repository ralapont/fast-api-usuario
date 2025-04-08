from fastapi import HTTPException, status
from fastapi.logger import logger as fastapi_logger

from passlib.context import CryptContext

from app.v1.model.user_model import User as UserModel
from app.v1.schema import user_schema
from app.v1.service.auth_service import get_password_hash

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user: user_schema.UserRegister):

    get_user = UserModel.filter((UserModel.email == user.email) | (UserModel.username == user.username)).first()
    if get_user:
        msg = "Email already registered"
        if get_user.username == user.username:
            msg = "Username already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_user = UserModel(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password)
    )

    db_user.save()

    return convery_entity_to_schema(db_user)

def get_users():
    db_users = UserModel.select()
    return map(lambda x : convery_entity_to_schema(x), db_users)

def get_user(id: id):

    fastapi_logger.info(f"Get user with id {id}")
    try:
        db_user = UserModel.get(UserModel.user_id==id)
    except UserModel.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return convery_entity_to_schema(db_user)

def modify_user(id: int, user: user_schema.UserRegister):
    fastapi_logger.info(f"Get user with id {id}")
    try:
        db_user = UserModel.get(UserModel.user_id==id)
    except UserModel.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    db_user.username = user.username
    db_user.email = user.email
    db_user.password = get_password_hash(user.password)

    db_user.save()

    return convery_entity_to_schema(db_user)

def delete_user(id: int):
    fastapi_logger.info(f"Get user with id {id}")
    try:
        db_user = UserModel.get(UserModel.user_id==id)
    except UserModel.DoesNotExist: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    db_user.delete_instance()
        
def convery_entity_to_schema(user: UserModel):
    return user_schema.User(
        id = user.user_id,
        email = user.email,
        username = user.username
    )