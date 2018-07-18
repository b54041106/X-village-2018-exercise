import re
username= input('username:')
password= input('password:')
class AuthSystem:
    def __init__(self):
        """Define regex"""#[0-9a-z] 表示可以是数字也可以是任何小写字母
        pattern1=r'(?P<username>[A-Z]{1}[a-zA-Z0-9]{5,11}' 
        pattern2=r'(?P<password>[0-9a-z]{6,})'
        self.username_regex = re.compile(pattern1)
        self.password_regex = re.compile(pattern2)
    
    def _check_username(self, username):
        """Check username is valid or not"""
        if self.username_regex.search(username) is not None:
            print("Correct username") #pattern + or
            return True
        else: 
            print("Username format error! Your username is {}")
            return False
        
    def _check_password(self, password):
        """Check password is valid or not"""
        if self.password_regex.search(password) is not None:
            print("Correct password")
            return True
        else:
            print("Password format error! Your password is {}")
            return False
        
    def authenticate(self, username, password):
        """authenticate the user"""
        if not self._check_username(username):
            return
        
        if not self._check_password(password):
            return
        
        print("Welcome, {}!")


auth = AuthSystem()
auth.authenticate(username, password)