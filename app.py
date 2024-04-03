from neo4j import GraphDatabase
from flask  import Flask ,  render_template

# Neo4j database connection settings
URI = "neo4j+s://18288252.databases.neo4j.io"
AUTH = ("neo4j", "e01cqJAgsfWi-sAdpYhsYwl5PtJGzGcaOPl1cbxChjs")


app = Flask(__name__)


driver = GraphDatabase.driver(URI, auth=AUTH)


def get_session():
    return driver.session()


@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
