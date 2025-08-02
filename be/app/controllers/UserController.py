from app.models import User
from app.schemas import User as UserSchema
from app.db import session


def create(user: UserSchema):
    if(user.password != user.password_confirmation):
        raise Exception("password dan konfirmasi password tidak sama")

    session.add(User(
        username=user.username, 
        email=user.email,
        password=user.password
    ))
    session.commit()

    return "Akun berhasil dibuat"

def destroy(id: int):
    try:

        user = session.query(User).filter(user.id == id).first()
        session.delete(user)

        return {
            "status": True,
            "message": "Your account deleted succesfully!"
        }

    except:
        return {
            "status": False,
            "message": "There is an error while deleting your eccount."
        }
    
def login():
    pass

def logout():
    pass