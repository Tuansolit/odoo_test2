from odoo import fields, models, api
import pandas as pd
from datetime import datetime, timedelta, date


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_money = fields.Float(compute='_compute_discount_money', store=True)

    time_intervaler = fields.Char(compute='_warranty_check', store=True)

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
    def _compute_amount(self):
        res = super(SaleOrderLine, self)._compute_amount()
        for line in self:
            if not line.product_id.warranty:
                line.update({
                    'price_subtotal': line.price_subtotal - line.discount_money,
                    'price_total': line.price_subtotal - line.discount_money,

                })
        return res

    @api.depends('product_id.warranty', 'price_unit', 'product_uom_qty')
    def _compute_discount_money(self):
        for line in self:
            if not line.product_id.warranty:
                line.update({
                    'discount_money': line.price_subtotal - (line.price_subtotal * 90) / 100
                })

    @api.depends('product_id.time_interval', 'product_id.date_to')
    def _warranty_check(selfs):
        for line in selfs:
            if not line.product_id.date_from:
                continue
            if not line.product_id.date_to:
                continue
            else:
                # if line.product_id.date_to > date.today():
                line.time_intervaler = line.product_id.time_interval
