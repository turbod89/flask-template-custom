from ..Base import Base

from .User import User
from .Group import Group


from werkzeug.security import check_password_hash, generate_password_hash

def init_app(app,db):
    print('models/auth/__init__.py init_app(app)')
    #generateRelationships(db)

def generate(db):

    groups = [
        {'name':'admin', 'description': 'This is the group of admins. Full access to all data.'},
        {'name':'active', 'description': 'Active users. Only users in this group will exists at logic effects.'},
        {'name':'registered', 'description': 'Registered users which have not actived their account yet.'},
        {'name':'blocked', 'description': 'Blocked users. The only they can do is loggin.'},
    ]
    
    users = [
        {
            'first_name': 'admin',
            'last_name': '',
            'email': 'admin@example.com',
            'password': 'abc123',
            'groups': ['admin','active'],
        },
        {
            'first_name': 'Gregory',
            'last_name': 'House',
            'email': 'ghouse@example.com',
            'password': 'abc123',
            'groups': ['active'],
        },
        {
            'first_name': 'James',
            'last_name': 'Wilson',
            'email': 'jwilson@example.com',
            'password': 'abc123',
            'groups': ['active'],
        },
        {
            'first_name': 'Lisa',
            'last_name': 'Cuddy',
            'email': 'lcuddy@example.com',
            'password': 'abc123',
            'groups': ['active'],
        },
        {
            'first_name': 'Allison',
            'last_name': 'Cameron',
            'email': 'acameron@example.com',
            'password': 'abc123',
            'groups': ['active'],
        },
        {
            'first_name': 'Eric',
            'last_name': 'Foremant',
            'email': 'eforeman@example.com',
            'password': 'abc123',
            'groups': ['active'],
        },
        {
            'first_name': 'Rober',
            'last_name': 'Chase',
            'email': 'rchase@example.com',
            'password': 'abc123',
            'groups': ['active'],
        },
    ]

    for tGroup in groups:
        group = Group(name=tGroup['name'], description = tGroup['description'])
        db.session.add(group)
        
    for tUser in users:
          user = User(
              first_name = tUser['first_name'],
              last_name = tUser['last_name'],
              email = tUser['email'],
              password = generate_password_hash(tUser['password']),
          )
          db.session.add(user)
    
    db.session.commit()
    
    for tUser in users:
        user = User.query.filter_by(email=tUser['email']).first()
        for sGroup in tUser['groups']:
            group = Group.query.filter_by(name=sGroup).first()
            user.groups.append(group)
    
    db.session.commit()
    




