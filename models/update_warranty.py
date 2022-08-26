from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'update.warranty'
    _description = 'Description'

    name = fields.Char()
    from_date = fields.Date()
    to_date = fields.Date()
    product_id = fields.Many2many('product.template')

    def edit_warranty(self):
        for rec in self:
            for cus in rec.product_id:
                cus.write({
                    'date_from': self.from_date,
                    'date_to': self.to_date
                })
