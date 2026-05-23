#from app.extensions import ma
#from app.models import Mechanic, Service_Ticket, MechanicServiceTicket
#from marshmallow import fields


#class Service_TicketSchema(ma.SQLAlchemyAutoSchema):
    #class Meta:
        #model = Service_Ticket
        #include_fk = True


#class MechanicServiceTicketSchema(ma.SQLAlchemyAutoSchema):
    #class Meta:
        #model = MechanicServiceTicket
        #fields = ('mechanic_id', 'service_id', 'start_date')
        #include_fk = True
        

    #service_tickets = fields.Nested(
        #Service_TicketSchema(only=('id', 'service_date', 'service_desc')),
         #many=True
    #)

#mechanic_service_ticket_schema = MechanicServiceTicketSchema()
#mechanics_service_tickets_schema = MechanicServiceTicketSchema(many=True)
