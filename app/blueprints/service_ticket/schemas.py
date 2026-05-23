from app.extensions import ma
from app.models import Service_Ticket, Mechanic, Inventory
from marshmallow import fields


class MechanicMiniSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Mechanic
        include_fk = True

    #id = fields.Int()
    #name = fields.String()


class InventoryMiniSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inventory
        include_fk = True


#class MechanicServiceTicketSchema(ma.SQLAlchemyAutoSchema):
    #class Meta:
        #model = MechanicServiceTicket
        #include_fk = True

    #mechanic = fields.Nested(MechanicSchema(only=('id', 'name')))


class Service_TicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Service_Ticket
        include_fk = True

    mechanics = fields.Nested(
        MechanicMiniSchema(only=('id', 'name')),
        many=True
    )

    inventories = fields.Nested(
        InventoryMiniSchema(only=('id', 'name', 'price')),
        many = True
    )

class EditServiceTicketSchema(ma.Schema):
    add_mechanic_ids = fields.List(fields.Int(), required=True)
    remove_mechanic_ids = fields.List(fields.Int(), required=True)

    class Meta:
        fields = ('add_mechanic_ids', 'remove_mechanic_ids')


service_ticket_schema = Service_TicketSchema()
service_tickets_schema = Service_TicketSchema(many=True)

edit_service_ticket_schema = EditServiceTicketSchema()


