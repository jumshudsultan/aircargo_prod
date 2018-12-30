class SaleOrderInherited(models.Model) :
    _inherit = 'sale.order'

    custom_field = fields.Char(string='Custom File')