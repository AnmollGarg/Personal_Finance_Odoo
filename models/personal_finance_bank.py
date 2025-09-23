from odoo import models, fields, api

class PersonalFinanceBank(models.Model):
    _name = 'personal.finance.bank'
    _description = 'Personal Finance Bank Details'
    _rec_name = 'bank_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    bank_name = fields.Char(string='Bank Name', required=True, tracking=True)
    account_number = fields.Char(string='Account Number', required=True, tracking=True)
    ifsc_code = fields.Char(string='IFSC Code', required=True, tracking=True)
    account_holder_name = fields.Char(string='Account Holder Name', required=True, tracking=True)
    bank_branch = fields.Char(string='Bank Branch', tracking=True, required=True)
    account_type = fields.Selection([
        ('savings', 'Savings'),
        ('current', 'Current'),
    ], string='Account Type', required=True, tracking=True)
    balance = fields.Float(string='Balance', tracking=True, required=True)
    account_opening_date = fields.Date(string='Account Opening Date', tracking=True)
    account_status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('closed', 'Closed'),
    ], string='Account Status', default='active', tracking=True, required=True,)
    bank_address = fields.Text(string='Bank Address', tracking=True, required=True,)
    swift_code = fields.Char(string='SWIFT Code', tracking=True, required=True,)