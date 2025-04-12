from fastapi import HTTPException, status
from fastapi.logger import logger as fastapi_logger
from pydantic import ValidationError

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

    user.password = get_password_hash(user.password)
    db_user = UserModel.create(**user.model_dump())
    db_user.save()
    return user_schema.User.model_validate(db_user, from_attributes=True)

def get_users():
    db_users = UserModel.select()
    return map(lambda x : user_schema.User.model_validate(x, from_attributes=True), db_users)

def get_user(id: id):

    fastapi_logger.info(f"Get user with id {id}")
    try:
        db_user = UserModel.get(UserModel.user_id==id)
        return user_schema.User.model_validate(db_user, from_attributes=True)
    except UserModel.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    except ValidationError as exc:
        print(repr(exc.errors()[0]['type']))



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

    return user_schema.User.model_validate(db_user, from_attributes=True)

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
        
