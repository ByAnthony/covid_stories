from db.run_sql import run_sql
from models.ticket import Ticket

import repositories.contributor_repository as contributor_repository
import repositories.event_repository as event_repository


def save(ticket):
    sql = "INSERT INTO tickets (event_id, contributor_id) VALUES (%s, %s) RETURNING id"
    values = [ticket.event.id, ticket.contributor.id]
    results = run_sql(sql, values)
    ticket.id = results[0]['id']
    return ticket


def select_all():
    tickets = []
    sql = "SELECT * FROM tickets"
    results = run_sql(sql)

    for row in results:
        event = event_repository.select(row['event_id'])
        contributor = contributor_repository.select(row['contributor_id'])
        ticket = Ticket(event, contributor, row['id'])
        tickets.append(ticket)
    return tickets


def select(id):
    ticket = None
    sql = "SELECT * FROM tickets WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        event = event_repository.select(result['event_id'])
        contributor = contributor_repository.select(result['contributor_id'])
        ticket = Ticket(event, contributor, result['id'])
    return ticket


def delete(id):
    sql = "DELETE FROM tickets WHERE id = %s"
    values = [id]
    run_sql(sql, values)