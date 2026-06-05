from datetime import datetime

class user:
    def __init__(self,username,email,password):
        self.username=username
        self._email=email
        self._password=password

    def get_mail(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email
    
    def set_email(self,new_email):
        self._email=new_email


user1=user("ritik","ritik@gmail.com","rkosiuu")
print(user1.get_mail())

user1.set_email("undertaker@gmail.com")
print(user1.get_mail())