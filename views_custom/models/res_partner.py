from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    first_name = fields.Char(string="First Name")
    second_name = fields.Char(string="Second Name")
    last_name = fields.Char(string="Last Name")
