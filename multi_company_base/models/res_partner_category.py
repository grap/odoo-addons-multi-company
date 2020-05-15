# Copyright (C) 2020-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResPartnerCategory(models.Model):
    _inherit = 'res.partner.category'

    company_id = fields.Many2one(
        comodel_name='res.company', string='Company',
        default=lambda self: self.env.user.company_id)
