from odoo import api, fields, models
from datetime import datetime, date
from odoo.exceptions import UserError

import time
import pandas as pd


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    date_from = fields.Date()
    date_to = fields.Date()
    warranty = fields.Char(compute='_compute_warranty', store=True)
    time_interval = fields.Char(string="Warranty Left", compute='_compute_time_interval', store=True)

    @api.depends('date_from', 'date_to')
    def _compute_warranty(self):
        for rec in self:
            if not rec.date_from:
                continue
            if not rec.date_to:
                continue
            if rec.date_from and rec.date_to:
                from_date = "{}".format(datetime.strftime(rec.date_from, '%d%m%y'))
                to_date = "{}".format(datetime.strftime(rec.date_to, '%d%m%y'))
                rec.warranty = 'PWR/' + from_date + '/' + to_date

    @api.depends('date_from', 'date_to')
    def _compute_time_interval(selfs):
        for rec in selfs:
            if not rec.date_from:
                continue
            if not rec.date_to:
                continue
            if rec.date_from > rec.date_to:
                    raise UserError('ERROR')
            else:
                if rec.date_to > date.today():
                    if rec.date_from > date.today():
                        t = (rec.date_to - rec.date_from).days
                    else:
                        t = (rec.date_to - date.today()).days
                    rec.time_interval = ""
                    nam = int(t / 365)
                    thang = int((t % 365) / 30)
                    ngay = (t % 365) % 30
                    if nam > 1:
                        rec.time_interval += str(nam) + ' years '
                    elif nam == 1:
                        rec.time_interval += str(nam) + ' year '
                    if thang > 1:
                        rec.time_interval += str(thang) + ' months '
                    elif thang == 1:
                        rec.time_interval += str(thang) + ' month '
                    if ngay > 1:
                        rec.time_interval += str(ngay) + ' days '
                    elif ngay == 1:
                        rec.time_interval += str(ngay) + ' day '



    def update_warranty(self):
        if not self:
            return True

        return {
            'name': 'update warranty ',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'update.warranty',
            'views': [(False, 'form')],
            'context': {'default_product_id': [(6, 0, self.ids)]},
            'target': 'new',
        }
