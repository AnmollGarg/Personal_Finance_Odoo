from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PersonalFinanceDebt(models.Model):
    _name = 'personal.finance.debt'
    _description = 'Personal Finance Debt Details'
    _rec_name = 'debt_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    debt_id = fields.Char(required=True, tracking=True, default = 'New', readonly=True, help ='Unique Debt ID')
    debt_name = fields.Char(required=True, tracking=True)
    debt_type = fields.Selection([
        ('personal_loan', 'Personal Loan'),
        ('home_loan', 'Home Loan'),
        ('car_loan', 'Car Loan'),
        ('credit_card', 'Credit Card'),
        ('student_loan', 'Student Loan'),
        ('other', 'Other'),
    ],required=True, tracking=True)
    amount_debt = fields.Float(required=True, tracking=True)
    current_value = fields.Float(tracking=True,required=True)
    debt_date = fields.Date(default=fields.Date.context_today, required=True, tracking=True)
    repay_date = fields.Date(tracking=True)
    is_reoccurring = fields.Boolean(tracking=True, help ='Check if this is a recurring debt')
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

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('debt_id', 'New') == 'New':
                vals['debt_id'] = self.env['ir.sequence'].next_by_code('personal.finance.debt') or 'New'
        return super(PersonalFinanceDebt, self).create(vals_list)

    @api.constrains('transaction_ids')
    def _check_transaction_unique(self):
        for record in self:
            if record.transaction_ids:
                investment = self.env['personal.finance.investment'].search([
                    ('transaction_ids', '=', record.transaction_ids.id)
                ], limit=1)
                if investment:
                    raise ValidationError(
                        "This transaction is already linked to an investment. You cannot link the same transaction to both debt and investment."
                    )