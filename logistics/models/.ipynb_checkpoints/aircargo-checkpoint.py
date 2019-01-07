from odoo import models, fields, api

class City(models.Model):
    _name = 'logistics.city'
    _description = "City"

    name = fields.Char(string="City Name", required=True)

class Shipper(models.Model):
    _name = 'logistics.shipper'
    _description = "Shipper"

    name = fields.Char(string="Shipper Name", required=True)
    contact = fields.Text()

class Transport(models.Model):
    _name = 'logistics.transport'
    _description = "Transport mean"

    name = fields.Char(string="Transport Mean", required=True)

class Customs_place(models.Model):
    _name = 'logistics.customs_place'
    _description = "Customs Place"

    name = fields.Char(string="Custom Place", required=True)

class Terminal(models.Model):
    _name = 'logistics.terminal'
    _description = "Terminal"

    name = fields.Char(string="Terminal", required=True)

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Purchase_Order(models.Model):
    _inherit = 'purchase.order'

    sale_order = fields.Many2one('sale.order',
    string="Sale Order")

    class Sale_Order(models.Model):
        _inherit = 'sale.order'

        po_count = fields.Integer(compute='_po_count')

        @api.multi
        def _po_count(self ):
            results = self.env['purchase.order'].read_group([('sale_order', 'in', self.ids)], 'sale_order', 'sale_order')
            dic = {}
            for x in results:
                dic[x['sale_order'][0]] = x['sale_order_count']
            for record in self:
                record['po_count'] = dic.get(record.id, 0)