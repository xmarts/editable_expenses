# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ranplace_campo(models.Model):
    _inherit = 'hr.expense.sheet'

    expense_line_ids = fields.One2many('hr.expense', 'sheet_id', string='Expense Lines')
    
class remplace(models.Model):
    _inherit ='hr.expense'
                
    product_id = fields.Many2one('product.product', string='Product')
    unit_amount = fields.Float(string='Unit Price', )
    quantity = fields.Float(string="Cantidad")

    

        