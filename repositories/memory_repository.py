from db.run_sql import run_sql
from models.memory import Memory

import repositories.charity_repository as charity_repository
import repositories.contributor_repository as contributor_repository


def save(memory):
    sql = "INSERT INTO memories (title, contributor_id, story, date, charity_id) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [memory.title, memory.contributor.id, memory.story, memory.date, memory.charity.id]
    results = run_sql(sql, values)
    memory.id = results[0]['id']
    return memory


def select_all():
    memories = []
    sql = "SELECT * FROM memories ORDER BY date DESC"
    results = run_sql(sql)

    for row in results:
        contributor = contributor_repository.select(row['contributor_id'])
        charity = charity_repository.select(row['charity_id'])
        memory = Memory(row['title'], contributor, row['story'], row['date'], charity, row['id'])
        memories.append(memory)
    return memories


def select(id):
    memory = None
    sql = "SELECT * FROM memories WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        contributor = contributor_repository.select(result['contributor_id'])
        charity = charity_repository.select(result['charity_id'])
        memory = Memory(result['title'], contributor, result['story'], result['date'], charity, result['id'])
    return memory

def delete(id):
    sql = "DELETE FROM memories WHERE id = %s"
    values = [id]
    run_sql(sql, values)