from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.exc import IntegrityError


# create database
engine = create_engine("sqlite:///tasks.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    tasks = relationship('Task', back_populates='user', cascade="all, delete-orphan")


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='tasks')


Base.metadata.create_all(engine)


# ability functions
def get_user_by_email(email):
    user = session.query(User).filter_by(email=email).first()
    if user:
        print(user.name)
    return user

def confirm_action(prompt:str) -> bool:
    return input(f"{prompt} yes/no: ").strip().lower() == 'yes'



def add_user():
    name, email = input("Enter user name: "), input("Enter the email: ")
    if get_user_by_email(email=email):
        print(f"User already exists: {email}")
        return

    try:
        session.add(User(name=name, email=email))
        session.commit()
        print(f"User: {name} added")
    
    except:
        session.rollback()
        print(f"Error")


def add_task():
    email = input("Enter the email of the use to add tasks:")
    user = get_user_by_email(email=email)
    
    if not user:
        print("There is no such user")
        return
    
    try:
        title, description = input("Enter the title of new task: "), input("Enter the desc for new taks: ")
        session.add(Task(
            title=title,
            description=description,
            user_id=user.id
        ))
        session.commit()
        print(f"new task \"{title}\" for ${user.name}")
    
    except:
        print("Error")


def query_users():
    for user in session.query(User).all():
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    
    
def query_tasks():
    email = input("Enter email of the user for tasks: ")
    user = get_user_by_email(email=email)

    if not user:
        print("There is no user with that email!")
        return

    for task in session.query(Task).all():
        print(f"ID: {task.id}\ntitle: {task.title}\nOwner: {task.id}\nDesc: {task.description}")


def update_user():
    email = input("Enter email of the user to update: ")
    user = get_user_by_email(email=email)

    if not user:
        print("There is no user with that email")
        return
    
    user.name = input("Enter new username (leave itu blank if you don't want to change username)") or user.name
    user.email = input("Enter new email (leave itu blank if you don't want to change email)") or user.email

    session.commit()

    print("User updated succesfully")


def delete_user():
    emaiddl = input("Enter email of the user to delete: ")
    user = get_user_by_email(email)

    if not user:
        print("There is no user with that email")
        return
    
    session.delete(user)
    session.commit()
    print("User deleted succesfully")

# def delete_task():


# main ops
def main() -> None:
    actions = {
        "1": add_user,
        "2": add_task, 
        "3": query_users,
        "4": query_tasks,
        "5": update_user,
        "6": delete_user
    }

    while True:
        print("Options:\n1. Add User\n2. Add Task\n3. Query User\n4. Query Tasks\n5. Update User\n6. Delete  User\n7. Delete Task\n8. Exit")
        
        choice = input("Enter an option: ")
        if choice == "8":
            print("Adios")
            return
        
        action = actions.get(choice)
        if action:
            action()
        else:
            print("That is not an option!")

if __name__ == "__main__":
    main()

