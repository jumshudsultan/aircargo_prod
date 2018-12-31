from odoo import models, fields, api


class SaleCity(models.Model):
    _inherit = 'sale.order'

    city_name_pol = fields.Many2one('logistics.city', string="City Name")
    city_name_pod = fields.Many2one('logistics.city', string="City Name")
    shipper = fields.Many2one('logistics.shipper', string="Shipper")
    shipper_contact = fields.Text(string='Shipper Contact', related='shipper.contact')
    importer = fields.Many2one('res.partner', string="Importer")
    cargo_dimensions = fields.Char(string='Cargo Dimensions')
    transport_mean = fields.Many2one('logistics.transport', string="Transport Mean")
    waybill = fields.Char(string='Waybill')
    order_date = fields.Date(string='Order Date')
    arrival_date = fields.Date(string='Arrival Date')
    inspector = fields.Char(string='Inspector')
    custom_arrival_date = fields.Date(string='Arrival Date')
    custom_departure_date = fields.Date(string='Departure Date')
    customs_place = fields.Many2one('logistics.customs_place', string="Customs Place")
    terminal = fields.Many2one('logistics.terminal', string="Terminal")
