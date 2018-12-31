from odoo import models, fields, api


class SaleCity(models.Model):
    _inherit = 'sale.order'

    city_name = fields.Many2one('logistics.city', string="City Name")
    shipper = fields.Many2one('logistics.shipper', string="Shipper")
    shipper_contact = fields.Char(string='Shipper Contact', related=logistics.shipper.contact)