from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    discount_money = fields.Float(compute='_compute_discount_money', store=True)

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
    def _compute_amount(self):
        res = super(SaleOrderLine, self)._compute_amount()
        for line in self:
            if not line.product_id.warranty:
                line.update({
                    'price_subtotal': line.price_subtotal - (line.price_subtotal * 10) / 100,
                    'price_total': line.price_subtotal - (line.price_subtotal * 10) / 100,

                })
        return res

    @api.depends('product_id.warranty', 'price_unit', 'product_uom_qty')
    def _compute_discount_money(self):
        for line in self:
            if not line.product_id.warranty:
                line.update({
                    'discount_money': line.price_subtotal - (line.price_subtotal * 90) / 100
                })
