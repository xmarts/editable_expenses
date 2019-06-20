# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ranplace_campo(models.Model):
    _inherit = 'hr.expense.sheet'

    expense_line_ids = fields.One2many('hr.expense', 'sheet_id', string='Expense Lines')
    
class remplace(models.Model):
    _inherit ='hr.expense'
                
    product_id = fields.Many2one('product.product', string='Product',states={'draft': [('readonly', False)], 'refused': [('readonly', False)],'approved': [('readonly', False)],'reported': [('readonly', False)]})
    unit_amount = fields.Float(string='Unit Price',states={'draft': [('readonly', False)], 'refused': [('readonly', False)],'approved': [('readonly', False)],'reported': [('readonly', False)]} )
    quantity = fields.Float(string="Cantidad",states={'draft': [('readonly', False)], 'refused': [('readonly', False)],'approved': [('readonly', False)],'reported': [('readonly', False)]})

    

        