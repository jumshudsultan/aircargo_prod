from odoo import models, fields, api


class SaleCity(models.Model):
    _inherit = 'sale.order'

    city_name = fields.Many2one('logistics.city', string="City Name")