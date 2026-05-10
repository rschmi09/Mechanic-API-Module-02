from .schemas import service_ticket_schema, service_tickets_schema
from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy import select
from app.models import Service_Ticket, db
from . import service_tickets_bp
from app.models import Mechanic


# Create Service Ticket (POST) - C in CRUD
@service_tickets_bp.route('/', methods=['POST'])
def create_service_ticket():
    try:
        service_ticket_data = service_ticket_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_service_ticket = Service_Ticket(**service_ticket_data)

    db.session.add(new_service_ticket)
    db.session.commit()
    return service_ticket_schema.jsonify(new_service_ticket), 201


# Get all Service Tickets (GET) - R in CRUD
@service_tickets_bp.route('/', methods=['GET'])
def get_service_tickets():
    query = select(Service_Ticket)
    service_tickets = db.session.execute(query).scalars().all()

    return service_tickets_schema.jsonify(service_tickets)


# Get Specific Service_Ticket (GET) - R in CRUD
@service_tickets_bp.route('/<int:service_ticket_id>', methods=['GET'])
def get_service_ticket(service_ticket_id):
    service_ticket = db.session.get(Service_Ticket, service_ticket_id)

    if service_ticket:
        return service_ticket_schema.jsonify(service_ticket), 200
    return jsonify({'error': 'Service_Ticket not found.'}), 404


# Update Specific Service_Ticket (PUT) - U in CRUD
@service_tickets_bp.route('/<int:service_ticket_id>', methods=['PUT'])
def update_service_ticket(service_ticket_id):
    service_ticket = db.session.get(Service_Ticket, service_ticket_id)

    if not service_ticket:
        return jsonify({'error': 'Service_Ticket not found.'}), 404
    
    try:
        service_ticket_data = service_ticket_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    for key, value in service_ticket_data.items():
        setattr(service_ticket, key, value)

    db.session.commit()
    return service_ticket_schema.jsonify(service_ticket), 200


# Assign Mechanic (PUT) - U in CRUD
@service_tickets_bp.route('/<int:service_ticket_id>/assign-mechanic/<int:mechanic_id>', methods=['PUT'])
def assign_mechanic(service_ticket_id, mechanic_id):
    service_ticket = db.session.get(Service_Ticket, service_ticket_id)
    mechanic = db.session.get(Mechanic, mechanic_id)

    if not service_ticket:
        return jsonify({'error': 'Service ticket not found.'}), 404
    
    if not mechanic:
        return jsonify({'error': 'Mechanic not found.'})
    
    service_ticket.mechanics.append(mechanic)

    db.session.commit()
    return jsonify({'messaege': f'Mechanic {mechanic_id} assigned to service ticket {service_ticket_id}'}), 200


# Remove Mechanic (PUT) - U in CRUD
@service_tickets_bp.route('/<int:service_ticket_id>/remove-mechanic/<int:mechanic_id>', methods=['PUT'])
def remove_mechanic(service_ticket_id, mechanic_id):
    service_ticket = db.session.get(Service_Ticket, service_ticket_id)
    mechanic = db.session.get(Mechanic, mechanic_id)

    if not service_ticket:
        return jsonify({'error': "Service ticket not found."}), 404
    
    if not mechanic:
        return jsonify({'error': 'Mechanic not found.'}), 404
    
    if mechanic not in service_ticket.mechanics:
        return jsonify({'error': 'Mechanic not assigned to this ticket.'}), 400
    
    service_ticket.mechanics.remove(mechanic)

    db.session.commit()
    return jsonify({'message': f'Mechanic {mechanic_id} removed from service ticket {service_ticket_id}.'}), 200


# Delete Specific Service_Ticket (DELETE) - D in CRUD
@service_tickets_bp.route('/<int:service_ticket_id>', methods=['DELETE'])
def delete_service_ticket(service_ticket_id):
    service_ticket = db.session.get(Service_Ticket, service_ticket_id)

    if not service_ticket:
        return jsonify({'error': 'Service_Ticket not found.'}), 404
    
    db.session.delete(service_ticket)
    db.session.commit()
    return jsonify({'message': f'Service_Ticket id: {service_ticket_id}, sucessfully deleted.'}), 200