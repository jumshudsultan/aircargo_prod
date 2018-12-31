from odoo import models, fields, api


class SaleCity(models.Model):
    _inherit = 'sale.order'

    city_name_pol = fields.Many2one('logistics.city', string="City Name")
    city_name_pod = fields.Many2one('logistics.city', string="City Name")
    shipper = fields.Many2one('logistics.shipper', string="Shipper")
    shipper_contact = fields.Char(string='Shipper Contact', related=shipper.contact)
