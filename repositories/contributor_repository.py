from db.run_sql import run_sql
from models.contributor import Contributor
from models.charity import Charity
from models.memory import Memory

import repositories.charity_repository as charity_repository
import repositories.contributor_repository as contributor_repository


def save(contributor):
    sql = "INSERT INTO contributors (first_name, last_name, age, profession, address) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [contributor.first_name, contributor.last_name, contributor.age, contributor.profession, contributor.address]
    results = run_sql(sql, values)
    contributor.id = results[0]['id']
    return contributor


def select_all():
    contributors = []
    sql = "SELECT * FROM contributors ORDER BY last_name ASC"
    results = run_sql(sql)

    for row in results:
        contributor = Contributor(row['first_name'], row['last_name'], row['age'], row['profession'], row['address'], row['id'])
        contributors.append(contributor)
    return contributors


def select(id):
    contributor = None
    sql = "SELECT * FROM contributors WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        contributor = Contributor(result['first_name'], result['last_name'], result['age'], result['profession'], result['address'], result['id'])
    return contributor


def charities(contributor):
    charities = []
    sql = "SELECT charities.* FROM charities INNER JOIN memories ON memories.charity_id = charities.id WHERE contributor_id=%s"
    values = [contributor.id]
    result = run_sql(sql, values)

    for row in result:
        charity = Charity(row['name'], row['description'], row['website'], row['id'])
        charities.append(charity)
    return charities


def memories(contributor):
    memories = []
    sql = "SELECT contributors.*, memories.* FROM contributors RIGHT JOIN memories ON contributors.id=memories.contributor_id WHERE contributor_id=%s"
    values = [contributor.id]
    result = run_sql(sql, values)
    
    for row in result:
        contributor = contributor_repository.select(row['contributor_id'])
        charity = charity_repository.select(row['charity_id'])
        memory = Memory(row['title'], contributor, row['story'], row['date'], charity, row['id'])
        memories.append(memory)
    return memories