from extensions import db


class User(db.Model):
    email = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(80))


    def checkPassword(self, password):
        if self.password != password:
            current_app.logger.warn(f'Password did not match for user:{self.username}')
            return False
        return True

    def __repr__(self) -> str:
        return f"<User {self.username}>"
    
    
    def as_dict(self) -> dict:
        return {
            'email': self.email,
            'username': self.username,
            'password': self.password
        }