from pdb import run
from db.run_sql import run_sql
from models.charity import Charity

def save(charity):
    sql = "INSERT INTO charities (name, description, website) VALUES (%s, %s, %s) RETURNING id"
    values = [charity.name, charity.description, charity.website]
    results = run_sql(sql, values)
    charity.id = results[0]['id']
    return charity

def select_all():
    charities = []
    sql = "SELECT * FROM charities"
    results = run_sql(sql)

    for row in results:
        charity = Charity(row['name'], row['description'], row['website'], row['id'])
        charities.append(charity)
    return charities