# Copyright (C) 2021-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Multi Company - Sale Management Module",
    "version": "12.0.1.1.0",
    "category": "Multi Company",
    "summary": "Handle Multi company for Sale Management Module",
    "author": "GRAP",
    "website": "http://www.grap.coop",
    "license": "AGPL-3",
    "depends": [
        "multi_company_base",
        "sale_management",
    ],
    "data": [
        "security/ir_rule.xml",
        "views/view_sale_order_template.xml",
    ],
    "images": [
        "static/description/sale_order_template_form.png",
    ],
    "installable": True,
}
