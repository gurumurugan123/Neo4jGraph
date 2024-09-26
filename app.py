from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from neo4j import GraphDatabase

app = Flask(__name__)

# Neo4j connection details
neo4j_uri = "bolt://localhost:7687"
neo4j_user = "neo4j" 
neo4j_password = "guru2020"  # Your Neo4j password

# Create a driver instance
driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

def create_candidate(tx, name, email):
    tx.run("CREATE (c:Candidate {name: $name, email: $email})", name=name, email=email)

def create_college(tx, college):
    tx.run("MERGE (co:College {name: $college})", college=college)

def create_degree(tx, degree):
    tx.run("MERGE (d:Degree {name: $degree})", degree=degree)

def create_year_of_passout(tx, year):
    tx.run("MERGE (y:YearOfPassout {year: $year})", year=year)

def create_relationships(tx, candidate_name, college_name, year_of_passout, degree_name, skills):
    tx.run("""
        MATCH (c:Candidate {name: $candidate_name}),
              (co:College {name: $college_name}),
              (d:Degree {name: $degree_name}),
              (y:YearOfPassout {year: $year_of_passout})
        MERGE (c)-[:Passed_Out]->(y)
        MERGE (c)-[:Studied_at]->(co)
        MERGE (c)-[:Has_degree]->(d)
        FOREACH (skill IN $skills | 
            MERGE (s:Skill {name: skill})
            MERGE (c)-[:Has_skill]->(s)
        )
    """, candidate_name=candidate_name, college_name=college_name, 
       year_of_passout=year_of_passout, degree_name=degree_name, skills=skills)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Handle file upload
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            # Read the CSV file
            df = pd.read_csv(file)

            # Push data to Neo4j
            with driver.session() as session:
                for index, row in df.iterrows():
                    candidate_name = row['Name']
                    candidate_email = row['Email']
                    college_name = row['College']
                    degree_name = row['Degree']
                    year_of_passout = row['Year of Passout']
                    skills = [skill.strip() for skill in row['Skills'].split(',')]  # Ensure this retrieves skills

                    session.write_transaction(create_candidate, candidate_name, candidate_email)
                    session.write_transaction(create_college, college_name)
                    session.write_transaction(create_degree, degree_name)
                    session.write_transaction(create_year_of_passout, year_of_passout)
                    session.write_transaction(create_relationships, candidate_name, college_name, year_of_passout, degree_name, skills)

            # Redirect to the same page to display uploaded data
            return redirect(url_for('upload_file'))

    # Fetch candidates data to display
    candidates = []
    with driver.session() as session:
        result = session.run("""
            MATCH (c:Candidate)-[:Passed_Out]->(y:YearOfPassout),
                  (c)-[:Studied_at]->(co:College),
                  (c)-[:Has_degree]->(d:Degree),
                  (c)-[:Has_skill]->(s:Skill)
            RETURN c.name AS name, c.email AS email, co.name AS college, 
                   d.name AS degree, y.year AS year_of_passout, collect(s.name) AS skills
        """)
        candidates = [record for record in result]

    return render_template('upload.html', candidates=candidates)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
