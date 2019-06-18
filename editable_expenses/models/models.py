# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ranplace_campo(models.Model):
    _inherit = 'hr.expense.sheet'

    expense_line_ids = fields.One2many('hr.expense', 'sheet_id', string='Expense Lines')
    

        