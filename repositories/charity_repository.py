from pdb import run
from db.run_sql import run_sql
from models.charity import Charity
from models.contributor import Contributor
from models.memory import Memory
from models.event import Event

import repositories.charity_repository as charity_repository
import repositories.contributor_repository as contributor_repository


def save(charity):
    sql = "INSERT INTO charities (name, description, website) VALUES (%s, %s, %s) RETURNING id"
    values = [charity.name, charity.description, charity.website]
    results = run_sql(sql, values)
    charity.id = results[0]['id']
    return charity


def select_all():
    charities = []
    sql = "SELECT * FROM charities ORDER By name ASC"
    results = run_sql(sql)

    for row in results:
        charity = Charity(row['name'], row['description'], row['website'], row['id'])
        charities.append(charity)
    return charities


def select(id):
    charity = None
    sql = "SELECT * FROM charities WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        charity = Charity(result['name'], result['description'], result['website'], result['id'])
    return charity


def delete(id):
    sql = "DELETE FROM charities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(charity):
    sql = "UPDATE charities SET (name, description, website) = (%s, %s, %s) WHERE id=%s"
    values = [charity.name, charity.description, charity.website, charity.id]
    run_sql(sql, values)


def contributors(charity):
    contributors = []
    sql = "SELECT contributors.* FROM contributors INNER JOIN memories ON memories.contributor_id = contributors.id WHERE charity_id=%s"
    values = [charity.id]
    result = run_sql(sql, values)

    for row in result:
        contributor = Contributor(row['first_name'], row['last_name'], row['age'], row['profession'], row['address'], row['id'])
        contributors.append(contributor)
    return contributors


def memories(charity):
    memories = []
    sql = "SELECT charities.*, memories.* FROM charities RIGHT JOIN memories ON charities.id=memories.charity_id WHERE charity_id=%s"
    values = [charity.id]
    result = run_sql(sql, values)
    
    for row in result:
        contributor = contributor_repository.select(row['contributor_id'])
        charity = charity_repository.select(row['charity_id'])
        memory = Memory(row['title'], contributor, row['story'], row['date'], charity, row['id'])
        memories.append(memory)
    return memories


def events(charity):
    events = []
    sql = "SELECT charities.*, events.* FROM charities RIGHT JOIN events ON charities.id=events.charity_id WHERE charity_id=%s"
    values = [charity.id]
    result = run_sql(sql, values)

    for row in result:
        charity = charity_repository.select(row['charity_id'])
        event = Event(row['name'], row['description'], charity, row['date'], row['id'])
        events.append(event)
    return events