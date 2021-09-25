from db.run_sql import run_sql
from models.contributor import Contributor

def save(contributor):
    sql = "INSERT INTO contributors (first_name, last_name, age, profession, address) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [contributor.first_name, contributor.last_name, contributor.age, contributor.profession, contributor.address]
    results = run_sql(sql, values)
    contributor.id = results[0]['id']
    return contributor