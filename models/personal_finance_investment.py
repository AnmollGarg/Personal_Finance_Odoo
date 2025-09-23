from odoo import models, fields, api

class PersonalFinanceInvestment(models.Model):
    _name = 'personal.finance.investment'
    _description = 'Personal Finance Investment Details'
    _rec_name = 'investment_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    investment_id = fields.Char(string='Investment Name', required=True, tracking=True, default = 'New', readonly=True)
    investment_name = fields.Char(string='Investment Name', required=True, tracking=True)
    investment_type = fields.Selection([
        ('stocks', 'Stocks'),
        ('bonds', 'Bonds'),
        ('mutual_funds', 'Mutual Funds'),
        ('real_estate', 'Real Estate'),
        ('cryptocurrency', 'Cryptocurrency'),
        ('gold', 'Gold'),
        ('fixed_deposit', 'Fixed Deposit'),
        ('other', 'Other'),
    ], string='Investment Type', required=True, tracking=True)
    amount_invested = fields.Float(string='Amount Invested', required=True, tracking=True)
    current_value = fields.Float(string='Current Value', tracking=True,required=True)
    investment_date = fields.Date(string='Investment Date', default=fields.Date.context_today, required=True, tracking=True)
    maturity_date = fields.Date(string='Maturity Date', tracking=True)
    is_reoccurring = fields.Boolean(string='Is Recurring', tracking=True, help ='Check if this is a recurring investment for Stocks and Mutual Funds')
    is_one_time = fields.Boolean(string='Is One-Time', tracking=True)
    is_monthly = fields.Boolean(string='Is Monthly', tracking=True)
    interest_rate = fields.Float(string='Interest Rate (%)', tracking=True, required=True)
    risk_level = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], string='Risk Level', tracking=True, required=True)
    notes = fields.Text(string='Notes', tracking=True)
    attachment = fields.Binary(string='Attachment', tracking=True)

    @api.model
    def create(self, vals):
            if vals.get('investment_id', 'New') == 'New':
                vals['investment_id'] = self.env['ir.sequence'].next_by_code('personal.finance.investment') or 'New'
            return super(PersonalFinanceInvestment, self).create(vals)