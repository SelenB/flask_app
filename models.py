from sqlalchemy import sql, orm
from app import db

#to do-check the uniqueness of each attribute.
#albums = orm.relationshio('Albums')-it is unclear whether 
    #this is needed because as defined on the 
    #er diagram, there is no artist associated with 
    #album.
class Artists(db.Model):
    __tablename__ = 'artists'
    id = db.Column('id', db.String(200), primary_key=True)
    artist_name = db.Column('artist_name',db.String(200), unique=True)
    genres = db.Column('genres',db.String(200), unique=False)
    pop = db.Column('pop',db.Integer(), unique=False)
    followers = db.Column('followers',db.Integer(), unique=False)
    image_url = db.Column('image_url', db.String(400), unique= False)
    #not sure about this to specify one to many relationship between classes.
    topartists = orm.relationship('Topartists')
    created = orm.relationship('Createdby')
    tracksonalbum=orm.relationship('Albumcontainstrack')

class Listeners(db.Model):
    __tablename__ = 'listeners'
    id = db.column('id', db.String(200), primary_key=True)
    display_name = db.column('display_name', db.String(200), nullable= False)
    followers = db.column('followers',db.Integer(), nullable = False)
    image_url = db.Column('image_url',db.String(400), unique= False, nullable = False)
    #not sure about this to specify one to many relationship between classes.
    topartists = orm.relationship('Topartists')
    toptracks = orm.relationship('Toptracks')


class Tracks(db.Model):
    __tablename__ = 'tracks'
    id = db.column('id', db.String(200), primary_key=True)
    track_name = db.column('track_name', db.String(200), nullable= False)
    pop = db.column('pop',db.Integer(), nullable = False)
    review_url = db.Column('review_url',db.String(400), unique= False, nullable = False)

class Albums(db.Model):
    __tablename__ = 'listeners'
    id = db.column('id', db.String(200), primary_key=True)
    name = db.column('name', db.String(200), nullable= False)
    album_type = db.column('album_type', db.String(200), nullable = False)
    image_url = db.Column('image_url',String(400), unique= False, nullable = False)
    #not sure about this to specify one to many relationship between classes.
    tracksonalbum=orm.relationship('Albumcontainstrack')


class Topartists(db.Model):
    __tablename__ = 'topartists'
    listener_id = db.column('listener_id', db.String(200), db.ForeignKey('listeners.id'), primary_key = True)
    artist_id = db.column('artist_id', db.String(200), db.ForeignKey('artists.id'), primary_key = True)
    time_span = db.column('time_span', db.String(200), primary_key=True)

   
class Toptracks(db.Model):
    __tablename__ = 'toptracks'
    listener_id = db.column('listener_id', db.String(200), db.ForeignKey('listeners.id'), primary_key = True)
    track_id = db.column('track_id', db.String(200), db.ForeignKey('tracks.id'), primary_key = True)
    time_span = db.column('time_span', db.String(200), primary_key=True)

#to-do this table seems redundant.
class Createdby(db.Model):
    __tablename__ = 'createdby'
    artist_id = db.column('artist_id', db.String(200), db.ForeignKey('artists.id'), primary_key = True)
    track_id = db.column('track_id', db.String(200), db.ForeignKey('tracks.id'), primary_key = True)

class Albumcontainstrack(db.Model):
    __tablename__ = 'albumcontainstrack'
    artist_id = db.column('artist_id', db.String(200), db.ForeignKey('artists.id'), primary_key = True)
    album_id = db.column('album_id', db.String(200), db.ForeignKey('albums.id'), primary_key = True)


    
