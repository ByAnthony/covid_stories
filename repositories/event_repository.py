from db.run_sql import run_sql
from models.event import Event


def save(event):
    sql = "INSERT INTO events (name, description, charity_id, fee, date) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [event.name, event.description, event.charity.id, event.fee, event.date]
    results = run_sql(sql, values)
    event.id = results[0]['id']
    return event