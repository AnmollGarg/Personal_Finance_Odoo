from odoo import models, fields, api

class PersonalFinanceBank(models.Model):
    _name = 'personal.finance.bank'
    _description = 'Personal Finance Bank Details'
    _rec_name = 'bank_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    bank_name = fields.Char(required=True, tracking=True)
    account_number = fields.Char(required=True, tracking=True)
    ifsc_code = fields.Char(required=True, tracking=True)
    account_holder_name = fields.Char(required=True, tracking=True)
    bank_branch = fields.Char(tracking=True, required=True)
    account_type = fields.Selection([
        ('savings', 'Savings'),
        ('current', 'Current'),
    ],required=True, tracking=True)
    balance = fields.Float(tracking=True, required=True)