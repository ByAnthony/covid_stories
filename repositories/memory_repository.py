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