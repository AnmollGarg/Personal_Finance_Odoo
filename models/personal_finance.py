from odoo import models, fields, api

class PersonalFinance(models.Model):
    _name = 'personal.finance'
    _description = 'Personal Finance Management'
    _rec_name = 'transaction_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    transaction_type = fields.Selection([
        ('income', 'Income'),
        ('expense', 'Expense'),
    ], string='Transaction Type', required=True, tracking=True)

    transaction_name = fields.Char(string='Transaction Name', required=True, tracking=True, default = 'New', readonly=True)
    amount = fields.Float(string='Amount', required=True, tracking=True)
    date = fields.Date(string='Date', default=fields.Date.context_today, required=True, tracking=True)
    category_income = fields.Selection([
        ('salary', 'Salary'),
        ('dividend', 'Dividend'),
        ('intrest', 'Intrest'),
        ('gift', 'Gift'),
        ('other', 'Other'),
    ], string='Category Income', required=True, tracking=True)
    category_expense = fields.Selection([
        ('food', 'Food'),
        ('rent', 'Rent'),
        ('utilities', 'Utilities'),
        ('entertainment', 'Entertainment'),
        ('travel', 'Travel'),
        ('other', 'Other'),
    ], string='Category Expense', required=True, tracking=True)

    transaction_from = fields.Selection([
        ('bank_transfer', 'Bank Transfer'),
        ('cheque', 'Cheque'),
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('upi', 'UPI'),
    ])

    bank_ids = fields.Many2one('personal.finance.bank', string='Bank', tracking=True)

    notes = fields.Text(string='Notes', tracking=True)
    attachment = fields.Binary(string='Attachment', tracking=True)

    @api.model
    def create(self, vals):
            if vals.get('transaction_name', 'New') == 'New':
                vals['transaction_name'] = self.env['ir.sequence'].next_by_code('personal.finance') or 'New'
            return super(PersonalFinance, self).create(vals)
