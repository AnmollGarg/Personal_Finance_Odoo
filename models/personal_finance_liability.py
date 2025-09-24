from odoo import models, fields, api

class PersonalFinanceLiability(models.Model):
    _name = 'personal.finance.liability'
    _description = 'Personal Finance liability Details'
    _rec_name = 'liability_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    liability_id = fields.Char(required=True, tracking=True, default = 'New', readonly=True, help ='Unique Liability ID')
    liability_name = fields.Char(required=True, tracking=True)
    liability_ids = fields.Many2one('personal.finance.debt', tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('liability_id', 'New') == 'New':
            vals['liability_id'] = self.env['ir.sequence'].next_by_code('personal.finance.liability') or 'New'
        return super(PersonalFinanceLiability, self).create(vals)