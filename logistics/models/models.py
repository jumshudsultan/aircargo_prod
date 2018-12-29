from odoo import models, fields, api

class Logistics(models.Model):
    _name = 'city.logistics'
    _description = "City"

    name = fields.Char(string="Title", required=True)

class Logistics(models.Model):
    _name = 'shipper.logistics'
    _description = "Shipper"

    name = fields.Char(string="Title", required=True)
    contact = fields.Text()

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100