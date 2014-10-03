#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from bottle import get, run, static_file, template


@get('/css/<filename:re:.*\.css>')
def get_css(filename):
    return static_file(filename, root="static", mimetype="text/css")


@get('/images/<filename:re:.*\.png>')
def get_image(filename):
    return static_file(filename, root="static", mimetype="image/png")


@get("/")
def get_index():
    """ Index page.
    """
    return template("index")


@get("/person/")
def get_person_list():
    """ List of all people.
    """
    return template("person_list", people=[])


@get("/person/<name>")
def get_person(name):
    """ Page with details for a specific person.
    """
    return template("person", name="?", born="?", movies=[])


@get("/movie/")
def get_movie_list():
    """ List of all movies.
    """
    return template("movie_list", movies=[])


@get("/movie/<title>")
def get_movie(title):
    """ Page with details for a specific movie.
    """
    return template("movie", title="?", released="?", actors=[], director="?")


if __name__ == "__main__":
    run(host="localhost", port=8080, reloader=True)

