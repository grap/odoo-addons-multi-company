# Copyright (C) 2014-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Multi Company - Sales Team Module",
    "version": "12.0.1.1.1",
    "category": "Multi Company",
    "summary": "Handle Multi company for Sales Team Module",
    "author": "GRAP",
    "website": "https://github.com/grap/odoo-addons-multi-company",
    "license": "AGPL-3",
    "depends": [
        "sales_team",
        # GRAP
        "multi_company_base",
    ],
    "data": [
        "views/view_crm_team.xml",
    ],
    "installable": True,
}
