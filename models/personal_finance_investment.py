from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PersonalFinanceInvestment(models.Model):
    _name = 'personal.finance.investment'
    _description = 'Personal Finance Investment Details'
    _rec_name = 'investment_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    investment_id = fields.Char(required=True, tracking=True, default = 'New', readonly=True, help ='Unique Investment ID')
    investment_name = fields.Char(required=True, tracking=True)
    investment_type = fields.Selection([
        ('stocks', 'Stocks'),
        ('bonds', 'Bonds'),
        ('mutual_funds', 'Mutual Funds'),
        ('real_estate', 'Real Estate'),
        ('cryptocurrency', 'Cryptocurrency'),
        ('gold', 'Gold'),
        ('fixed_deposit', 'Fixed Deposit'),
        ('other', 'Other'),
    ],required=True, tracking=True)
    amount_invested = fields.Float(required=True, tracking=True)
    current_value = fields.Float(tracking=True,required=True)
    investment_date = fields.Date(default=fields.Date.context_today, required=True, tracking=True)
    maturity_date = fields.Date(tracking=True)
    is_reoccurring = fields.Boolean(tracking=True, help ='Check if this is a recurring investment for Stocks and Mutual Funds')
    is_one_time = fields.Boolean(tracking=True)
    is_monthly = fields.Boolean(tracking=True)
    interest_rate = fields.Float(tracking=True, required=True, help ='in percentage')
    risk_level = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ],tracking=True, required=True)
    transaction_ids = fields.Many2one('personal.finance', string='Transaction', tracking=True, help ='Link to the related transaction', required = True)
    notes = fields.Text(tracking=True)
    attachment = fields.Binary(tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('investment_id', 'New') == 'New':
            vals['investment_id'] = self.env['ir.sequence'].next_by_code('personal.finance.investment') or 'New'
        return super(PersonalFinanceInvestment, self).create(vals)

    @api.constrains('transaction_ids')
    def _check_transaction_unique(self):
        for record in self:
            if record.transaction_ids:
                debt = self.env['personal.finance.debt'].search([
                    ('transaction_ids', '=', record.transaction_ids.id)
                ], limit=1)
                if debt:
                    raise ValidationError(
                        "This transaction is already linked to a debt. You cannot link the same transaction to both investment and debt."
                    )