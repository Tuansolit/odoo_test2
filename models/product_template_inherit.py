from odoo import api, fields, models
from datetime import datetime, timedelta, date

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    shit = fields.Char('Shit')

    date_from = fields.Date()

    date_to = fields.Date()

    warranty = fields.Char(compute='_compute_warranty', store=True)

    @api.depends('date_from', 'date_to')
    def _compute_warranty(self):
        for rec in self:
            if not rec.date_from:
                continue
            if not rec.date_to:
                continue
            if rec.date_to and rec.date_to:
                from_date = "{}".format(datetime.strftime(rec.date_from, '%d%m%y'))
                to_date = "{}".format(datetime.strftime(rec.date_to, '%d%m%y'))
                rec.warranty = 'PWR/' + from_date + '/' + to_date


