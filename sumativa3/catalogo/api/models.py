from ninja import Schema
from typing import List

# Este es el esquema utilizado para la creación de posts exclusivamente
class MessageSchema(Schema):
    message: str

class ServiceInputSchema(Schema):
    nombre: str
    descripcion: str
    provedor: int
    valor: int
    from_date: str
    thru_date: str

class ProviderOutputSchema(Schema):
    fantasynombre: str
    tax_nombre: str
    tax_id: str
    permitir: bool

class AddressOutputSchema(Schema):
    provedor: int
    type: str
    direccion1: str
    direccion2: str
    codigopostal: str
    ciudad: str
    region: str
    pais: str

class ContactOutputSchema(Schema):
    provedor: int
    type: str
    first_nombre: str
    last_nombre: str
    email: str
    telefono: str
    mobile: str

class ServiceOutputSchema(Schema):
    nombre: str
    descripcion: str
    provedor: ProviderOutputSchema
    valor: int
    from_date: str
    thru_date: str
    contacto: List[ContactOutputSchema]
    direccion: AddressOutputSchema






