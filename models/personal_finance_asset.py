from odoo import models, fields, api

class PersonalFinanceAsset(models.Model):
    _name = 'personal.finance.asset'
    _description = 'Personal Finance Asset Details'
    _rec_name = 'asset_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    asset_id = fields.Char(required=True, tracking=True, default = 'New', readonly=True, help ='Unique Asset ID')
    asset_name = fields.Char(required=True, tracking=True)
    asset_ids = fields.Many2one('personal.finance.investment', string='Investment', tracking=True, help ='Link to the related investment')

    @api.model
    def create(self, vals):
        if vals.get('asset_id', 'New') == 'New':
            vals['asset_id'] = self.env['ir.sequence'].next_by_code('personal.finance.asset') or 'New'
        return super(PersonalFinanceAsset, self).create(vals)