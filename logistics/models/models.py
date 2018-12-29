from odoo import models, fields, api

class City(models.Model):
    _name = 'logistics.city'
    _description = "City"

    name = fields.Char(string="Title", required=True)

class Shipper(models.Model):
    _name = 'logistics.shipper'
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