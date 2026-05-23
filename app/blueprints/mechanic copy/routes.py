from .schemas import mechanic_service_ticket_schema, mechanics_service_tickets_schema
from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy import select
from app.models import MechanicServiceTicket, db
from . import mechanics_service_tickets_bp


# Create mechanic service ticket (POST) - C in CRUD
@mechanics_service_tickets_bp.route('/', methods=['POST'])
def create_mechanic_service_ticket():
    try:
        mechanic_service_ticket_data = mechanic_service_ticket_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    query = select(MechanicServiceTicket).where(MechanicServiceTicket.service_id == mechanic_service_ticket_data['service_id'])
    existing_mechanic_service_ticket = db.session.execute(query).scalars().all()
    if existing_mechanic_service_ticket:
        return jsonify({'error': 'Service Ticket already associated with an account'}), 400

    new_mechanic_service_ticket = MechanicServiceTicket(**mechanic_service_ticket_data)

    db.session.add(new_mechanic_service_ticket)
    db.session.commit()
    return mechanic_service_ticket_schema.jsonify(new_mechanic_service_ticket), 201


# Get all mechanic service tickets (GET) - R in CRUD
@mechanics_service_tickets_bp.route('/', methods=['GET'])
def get_mechanics_service_tickets():

    try:
        page = int(request.args.get('page'))
        per_page = int(request.args.get('per_page'))

        query = select(MechanicServiceTicket)
        mechanics_service_tickets = db.paginate(query, page=page, per_page=per_page)

        return mechanics_service_tickets_schema.jsonify(mechanics_service_tickets),200

    except:
        query = select(MechanicServiceTicket)
        mechanics_service_tickets = db.session.execute(query).scalars().all()

        return mechanics_service_tickets_schema.jsonify(mechanics_service_tickets)


# Get Specific mechanic service ticket (GET) - R in CRUD
@mechanics_service_tickets_bp.route('/<int:mechanic_service_ticket_id>', methods=['GET'])
def get_mechanic_service_ticket(mechanic_service_ticket_id):
    mechanic_service_ticket = db.session.get(MechanicServiceTicket, mechanic_service_ticket_id)

    if mechanic_service_ticket:
        return mechanic_service_ticket_schema.jsonify(mechanic_service_ticket), 200
    return jsonify({'error': 'Service Ticket not found.'}), 404


# Get list of mechanics in order of who has worked on the most service_tickets
#mechanics_service_tickets_bp.route('/workload', methods=['GET'])
#def mechanic_workload():
    #query = select(MechanicServiceTicket)
    #mechanics = db.session.execute(query).scalars().all()

    #mechanics.sort(key= lambda mechanic: len(mechanic.service_tickets), reverse=True)

    #return mechanics_service_tickets_schema.jsonify(mechanics)



# Update Specific mechanic service ticket (PUT) - U in CRUD
@mechanics_service_tickets_bp.route('/<int:mechanic_service_ticket_id>', methods=['PUT'])
def update_mechanic_service_ticket(mechanic_service_ticket_id):

    mechanic_service_ticket = db.session.get(MechanicServiceTicket, mechanic_service_ticket_id)

    if not mechanic_service_ticket:
        return jsonify({'error': 'Assignment not found.'}), 404
    
    try:
        data = mechanic_service_ticket_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    # only allow safe fields
    if 'mechanic_in' in data:
        mechanic_service_ticket.mechanic_id = data['mechanic_id']
    
    if 'service_in' in data:
        mechanic_service_ticket.service_id = data['service_id']

    if 'start_date' in data:
        mechanic_service_ticket.start_date = data['start_date']    

    db.session.commit()
    
    return mechanic_service_ticket_schema.jsonify(mechanic_service_ticket), 200


# Delete Specific mechanic (DELETE) - D in CRUD
@mechanics_service_tickets_bp.route('/<int:mechanic_serivce_ticket_id>', methods=['DELETE'])
def delete_mechanic_service_ticket(mechanic_service_ticket_id):
    mechanic_service_ticket = db.session.get(MechanicServiceTicket, mechanic_service_ticket_id)

    if not mechanic_service_ticket:
        return jsonify({'error': 'Service Ticket not found.'}), 404
    
    db.session.delete(mechanic_service_ticket)
    db.session.commit()
    return jsonify({'message': f'Service Ticket id: {mechanic_service_ticket_id}, sucessfully deleted.'}), 200