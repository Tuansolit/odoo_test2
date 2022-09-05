from odoo import fields, models, api


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    Calculated_discount_total = fields.Float(compute='_compute_Calculated_discount_total', store=True)

    @api.depends('order_line.discount_money')
    def _compute_Calculated_discount_total(self):
        s = 0
        for rec in self:
            for line in rec.order_line:
                s += line.discount_money
            rec.Calculated_discount_total = s

