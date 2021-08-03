# Copyright (C) 2021-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class SaleOrderTemplateOption(models.Model):
    _inherit = "sale.order.template.option"

    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        related="sale_order_template_id.company_id",
        store=True,
    )
