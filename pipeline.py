import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    dbName = os.getenv("dbName")
    dbUser = os.getenv("dbUser")
    dbPassword = os.getenv("dbPassword")
    dbPort = os.getenv("dbPort")
    dbHost = os.getenv("dbHost")
    
    conn = psycopg2.connect(
        host=dbHost, 
        port=dbPort, 
        dbname=dbName, 
        user=dbUser, 
        password=dbPassword
    )
    return conn

def fetch_enseignants(cursor):
    cursor.execute('SELECT * FROM enseignants;')
    enseignants_dict = []
    for row in cursor:
        enseignant_dict = {
            'Enseignant': row[1],
            'Responsable': row[3]
        }
        enseignants_dict.append(enseignant_dict)
    return enseignants_dict

def fetch_eleves(cursor):
    cursor.execute('SELECT * FROM eleves;')
    eleves_dict = []
    for row in cursor:
        eleve_dict = {
            'Eleve': row[1],
            'Responsable': row[3]
        }
        eleves_dict.append(eleve_dict)
    return eleves_dict

def associate_students_with_teachers(enseignants, eleves):
    for enseignant in enseignants:
        enseignant['nb_associes'] = 0

    for eleve in eleves:
        eleve['associes_a'] = 'Non trouvé'
        for enseignant in enseignants:
            if enseignant.get('Responsable') == eleve.get('Responsable'):
                enseignant['nb_associes'] += 1
                eleve['associes_a'] = enseignant.get('Enseignant')

def print_res(enseignants, eleves):
    for enseignant in enseignants:
        print(f"L'enseignant : {enseignant.get('Enseignant')} a {enseignant.get('nb_associes')} élève(s) associé(s).")

    for eleve in eleves:
        print(f"L'élève : {eleve.get('Eleve')} est associé au prof : {eleve.get('associes_a')}")

def main():
    conn = connect_db()
    cursor = conn.cursor()

    enseignants = fetch_enseignants(cursor)
    eleves = fetch_eleves(cursor)

    associate_students_with_teachers(enseignants, eleves)
    print_res(enseignants, eleves)

    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
