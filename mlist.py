from models import MovieList

movielist = MovieList.query.all()

movdc = {}

for i in movielist:
    lname = i.name
    lrelease = i.release
    movdc[lname] = lrelease








