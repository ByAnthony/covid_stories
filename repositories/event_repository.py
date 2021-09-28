from db.run_sql import run_sql
from models.event import Event

import repositories.charity_repository as charity_repository

def save(event):
    sql = "INSERT INTO events (name, description, charity_id, date) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [event.name, event.description, event.charity.id, event.date]
    results = run_sql(sql, values)
    event.id = results[0]['id']
    return event


def select_all():
    events = []
    sql = "SELECT * FROM events ORDER BY date DESC"
    results = run_sql(sql)

    for row in results:
        charity = charity_repository.select(row['charity_id'])
        event = Event(row['name'], row['description'], charity, row['date'], row['id'])
        events.append(event)
    return events


def select(id):
    event = None
    sql = "SELECT * FROM events WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        charity = charity_repository.select(result['charity_id'])
        event = Event(result['name'], result['description'], charity, result['date'], result['id'])
    return event


def delete(id):
    sql = "DELETE FROM events WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(events):
    sql = "UPDATE events SET (name, description, charity_id, date) = (%s, %s, %s) WHERE id=%s"
    values = [events.name, events.description, events.charity.id, events.date, events.id]
    run_sql(sql, values)