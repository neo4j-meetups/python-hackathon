#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from bottle import get, run, static_file, template
from py2neo.neo4j import GraphDatabaseService, CypherQuery


# Set up a link to the local graph database.
graph = GraphDatabaseService()


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
    statement = """\
    MATCH (p:Person)
    RETURN p.name AS name
    ORDER BY name
    """
    return template("person_list", people=CypherQuery(graph, statement).execute())


@get("/person/<name>")
def get_person(name):
    """ Page with details for a specific person.
    """
    statement = """\
    MATCH (p:Person) WHERE p.name = {N}
    OPTIONAL MATCH (p)-[:ACTED_IN]->(ma:Movie)
    OPTIONAL MATCH (p)-[:DIRECTED]->(md:Movie)
    RETURN p.name AS name, p.born AS born,
           collect(DISTINCT ma.title) AS movies_acted_in,
           collect(DISTINCT md.title) AS movies_directed
    """
    records = CypherQuery(graph, statement).execute(N=name)
    name, born, movies_acted_in, movies_directed = records[0]
    movies = [(movie, "Actor") for movie in movies_acted_in] + \
             [(movie, "Director") for movie in movies_directed]
    return template("person", name=name, born=born, movies=movies)


@get("/movie/")
def get_movie_list():
    """ List of all movies.
    """
    statement = """\
    MATCH (m:Movie)
    RETURN m.title AS title, m.released AS released
    ORDER BY m.title
    """
    return template("movie_list", movies=CypherQuery(graph, statement).execute())


@get("/movie/<title>")
def get_movie(title):
    """ Page with details for a specific movie.
    """
    statement = """\
    MATCH (m:Movie) WHERE m.title = {T}
    OPTIONAL MATCH (m)<-[:ACTED_IN]-(a:Person)
    OPTIONAL MATCH (m)<-[:DIRECTED]-(d:Person)
    RETURN m.title AS title, m.released AS released,
           collect(a.name) AS actors, d.name AS director
    """
    records = CypherQuery(graph, statement).execute(T=title)
    title, released, actors, director = records[0]
    return template("movie", title=title, released=released,
                             actors=actors, director=director)


if __name__ == "__main__":
    run(host="localhost", port=8080, reloader=True)

