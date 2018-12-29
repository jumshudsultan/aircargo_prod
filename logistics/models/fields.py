< ?xml
version = '1.0'
encoding = 'UTF-8'? >
< odoo >
< record
id = "logistics_pol"
model = "ir.model.fields"
< field
name = "field_description" > POL < / field >
< field
name = "model" > sale.order < / field >
< field
name = "model_id"
ref = "sale.model_sale_order" / >
< field
name = "name" > logistics_pol < / field >
< field
name = "relation" > logistics.city < / field >
< field
name = "selectable"
eval = "True" / >
< field
name = "state" > manual < / field >
< field
name = "store"
eval = "True" / >
< field
name = "ttype" > many2one < / field >
< / record >

< / odoo >
