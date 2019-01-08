from odoo import models, fields, api


class SaleCity(models.Model):
    _inherit = 'sale.order'

    city_name_pol = fields.Many2one('logistics.city', string="City Name POL")
    city_name_pod = fields.Many2one('logistics.city', string="City Name POD")
    shipper = fields.Many2one('logistics.shipper', string="Shipper")
    shipper_contact = fields.Text(string='Shipper Contact', related='shipper.contact')
    importer = fields.Many2one('res.partner', string="Importer")
    cargo_dimensions = fields.Char(string='Cargo Dimensions')
    transport_mean = fields.Many2one('logistics.transport', string="Transport Mean")
    waybill = fields.Char(string='Waybill')
    order_date = fields.Date(string='Order Date')
    arrival_date = fields.Date(string='Arrival Date')

    inspector = fields.Char(string='Inspector')
    customs_arrival_date = fields.Date(string='Arrival Date')
    customs_departure_date = fields.Date(string='Departure Date')
    customs_place = fields.Many2one('logistics.customs_place', string="Customs Place")
    terminal = fields.Many2one('logistics.terminal', string="Terminal")

    cargo_volume = fields.Float(string='Cargo Volume')
    invoice_value = fields.Float(string='Invoice Value')
    invoice_currency = fields.Many2one('res.currency', string="Invoice Currency")

    calculation_ids = fields.One2many('logistics.customs_calculation', 'sale_order', "Custom Calculations")
    load_categories = fields.Boolean(string="Load existing categories")
    
    @api.onchange('load_categories')
    def _load_categories(self):
        calculation_ids = []
        value = {}
        if self.load_categories:
            categories = self.env['logistics.customs_categories'].search([])
            for cat in categories:
                calculation_ids.append((0,0,{'name': cat.id}))
            value.update(calculation_ids=calculation_ids)
            return {'value': value}
        else:
            self.calculation_ids = None

class Customs_categories(models.Model):
    _name = 'logistics.customs_categories'
    _description = "Customs Categories"

    name = fields.Char(string="Payment Category", required=True)


class Customs_calculation(models.Model):
    _name = 'logistics.customs_calculation'
    _description = "Customs Calculation"

    name = fields.Many2one('logistics.customs_categories', string="Payment Category", required=True)
    amount = fields.Float(string="Amount")

    sale_order = fields.Many2one('sale.order', string='Sale Order', required=True, ondelete='cascade', index=True,
                                 copy=False, readonly=True)
