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
    invoice_value = fields.Float(string= 'Invoice Value')
    invoice_currency = fields.Many2one('res.currency', string="Invoice Currency")

    deklarasiya = fields.Float(string='Deklarasiya')
    kseroks = fields.Float(string='Kseroks')
    inspektor_maliyye = fields.Float(string='Inspektor Maliyye')
    inspektor_yuk = fields.Float(string='Inspektor Yuk')
    terminal_mebleg = fields.Float(string='Terminal Mebleg')
    kontrabanda = fields.Float(string='Kontrabanda')
    laboratoriya = fields.Float(string='Laboratoriya')
    kuryer_gomruk = fields.Float(string='Kuryer Gomruk')
    bank = fields.Float(string='Bank')
    bank_kom = fields.Float(string='Bank Kom.')
    fehle = fields.Float(string='Fehle')
    avtokar = fields.Float(string='Avtokar')
    buraxilish = fields.Float(string='Buraxilish')
    catdirilma = fields.Float(string='Catdirilma')
    beledci = fields.Float(string='Beledci')
    broker_fee = fields.Float(string='Broker Fee')
    diger_xercler = fields.Float(string='Diger Xercler')
    diger_xercler_6 = fields.Float(string='Diger Xercler 6%')

    cemi_mebleg = fields.Float(compute='_compute_sum', string="Cemi Mebleg")

    @api.onchange('deklarasiya', 'kseroks', 'inspektor_maliyye', 'inspektor_yuk', 'terminal_mebleg', 'kontrabanda', 'laboratoriya', 'kuryer_gomruk', 'bank', 'bank_kom', 'fehle', 'avtokar', 'buraxilish', 'catdirilma', 'beledci', 'broker_fee', 'diger_xercler', 'diger_xercler_6')
    def _compute_sum(self):
        self.cemi_mebleg = self.deklarasiya + self.kseroks + self.inspektor_maliyye + self.inspektor_yuk + self.terminal_mebleg + self.kontrabanda + self.laboratoriya + self.kuryer_gomruk + self.bank + self.bank_kom + self.fehle + self.avtokar + self.buraxilish + self.catdirilma + self.beledci + self.broker_fee + self.diger_xercler + self.diger_xercler_6