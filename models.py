from __init__ import db

class BlogModel(db.Model):
    __tablename__ = 'User'
    id         = db.Column(db.Integer(), primary_key = True)
    UsersName  = db.Column(db.String() , nullable    = False)
    blogTitle  = db.Column(db.String() , nullable    = False)
    blogBody   = db.Column(db.String() , nullable    = False)

    def __init__(self, UsersName, blogTitle, blogBody) -> None:
        self.UsersName = UsersName
        self.blogTitle = blogTitle
        self.blogBody  = blogBody