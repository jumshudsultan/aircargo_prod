from odoo import models, fields, api

class City(models.Model):
    _name = 'logistics.city'
    _description = "City"

    name = fields.Char(string="City Name", required=True)

class Shipper(models.Model):
    _name = 'logistics.shipper'
    _description = "Shipper"

    name = fields.Char(string="Title", required=True)
    contact = fields.Text()

class Transport(models.Model):
    _name = 'logistics.transport'
    _description = "Transport mean"

    name = fields.Char(string="Name", required=True)

class Customs_place(models.Model):
    _name = 'logistics.customs_place'
    _description = "Customs Place"

    name = fields.Char(string="Name", required=True)

class Terminal(models.Model):
    _name = 'logistics.terminal'
    _description = "Terminal"

    name = fields.Char(string="Name", required=True)

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100