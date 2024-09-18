import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

def connect() :
    dbName = os.getenv("dbName")
    dbUser = os.getenv("dbUser")
    dbPassword = os.getenv("dbPassword")
    dbPort = os.getenv("dbPort")
    dbHost = os.getenv("dbHost")
    conn = psycopg2.connect(host = dbHost,port = dbPort ,dbname =  dbName, user =  dbUser , password = dbPassword )
    
    cursor = conn.cursor()
    cursor.execute('select * from enseignants ; ')
    enseignants_dict = []
    

    for row in cursor:
        enseignant_dict = {
         'Enseignant' :  row[1],
         'Responsable' : row[3] 
        }
        enseignants_dict.append(enseignant_dict)
        
    eleves_dict = []
    cursor.execute('select * from eleves ;')
    for row in cursor:
        eleve_dict = {
        'Eleve' :  row[1],
        'Responsable' : row[3] 
        }
        eleves_dict.append(eleve_dict)
        
        
    for enseignant in enseignants_dict:
        enseignant['nb_associes'] = 0

    for eleve in eleves_dict:
        eleve['associes_a'] = 'Non trouvé'
        
        for enseignant in enseignants_dict:
            if enseignant.get('Responsable') == eleve.get('Responsable'):
                enseignant['nb_associes'] += 1
                eleve['associes_a'] = enseignant.get('Enseignant')

    for enseignant in enseignants_dict:
        print(f"L'enseignant : {enseignant.get('Enseignant')} a {enseignant.get('nb_associes')} élève(s) associé(s).")

    for eleve in eleves_dict:
        print(f"L'élève : {eleve.get('Eleve')} est associé au prof : {eleve.get('associes_a')}")
    
    
    print(enseignants_dict)
if __name__ == '__main__':
    connect()
    
   

    

    