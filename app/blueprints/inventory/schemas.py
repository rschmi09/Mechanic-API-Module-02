from app.extensions import ma
from app.models import Inventory, Service_Ticket
from marshmallow import fields


class Service_TicketMiniSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Service_Ticket
        include_fk = True


class InventorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inventory
        include_fk = True

    service_tickets = fields.Nested(
        Service_TicketMiniSchema(only=('id', 'service_date', 'service_desc')),
        many=True
    )   

inventory_schema = InventorySchema()
inventories_schema = InventorySchema(many=True)
