import re
from time import time
from datetime import datetime
from app import db

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern,'-',s)

posts_tags = db.Table('posts_tags',db.Column('post_id', db.Integer,db.ForeignKey('post.id')),
                                    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id')))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())
    tags = db.relationship('Tag',secondary='posts_tags',backref=db.backref('post'),lazy='dynamic')
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()
        
    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
        else:
            self.slug = str(int(time()))
            
    def __repr__(self) -> str:
        return f'<Post id: {self.id}, title: {self.title}>'
    

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)