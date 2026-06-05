from datetime import datetime

class user:
    def __init__(self,username,email,password):
        self.username=username
        self._email=email
        self._password=password

        @property
        def email(self):
            return self._email
        
        @email.setter
        def email(self,new_email):
            if "@" in new_email:
                self._email=new_email

        
user1=user("ritik","ritikgmail.com","rkosiuu")
user1.email="this is not @ an email"
print(user1.email)
