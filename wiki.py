#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from bottle import get, run, static_file, template
# TODO: Add necessary py2neo imports


# TODO: Create a global graph connection


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
    # TODO: Execute a Cypher query to retrieve all nodes with
    #       the `Person` label and pass them into the template
    #       ordered by `name` property
    return template("person_list", people=[])


@get("/person/<name>")
def get_person(name):
    """ Page with details for a specific person.
    """
    # TODO: Execute a Cypher query to retrieve all details for
    #       a specific named person, including `name` and year
    #       of birth (`born`) as well as a list of all movies
    #       in which they have been involved; the template expects
    #       a 2-tuple of title and role for each movie, such as
    #       ("The Matrix", "Actor") or ("Apollo 13", "Director")
    return template("person", name="?", born="?", movies=[])


@get("/movie/")
def get_movie_list():
    """ List of all movies.
    """
    # TODO: Execute a Cypher query to retrieve all nodes with
    #       the `Movie` label and pass them into the template
    #       ordered by `title` property
    return template("movie_list", movies=[])


@get("/movie/<title>")
def get_movie(title):
    """ Page with details for a specific movie.
    """
    # TODO: Execute a Cypher query to retrieve all details for
    #       a specific titled movie, including `title`, year
    #       of release (`released`), name of the director and
    #       name of all actors in the movie's cast
    return template("movie", title="?", released="?", actors=[], director="?")


if __name__ == "__main__":
    run(host="localhost", port=8080, reloader=True)

