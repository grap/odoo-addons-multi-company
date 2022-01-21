# Copyright (C) 2018-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Multi Company - CRM Module",
    "version": "12.0.1.1.1",
    "category": "Multi Company",
    "summary": "Handle Multi company for CRM Module",
    "author": "GRAP",
    "website": "https://github.com/grap/odoo-addons-multi-company",
    "license": "AGPL-3",
    "depends": [
        "crm",
        # GRAP
        "multi_company_base",
    ],
    "data": [
        "security/ir_rule.xml",
        "views/view_crm_lead.xml",
        "views/view_crm_lead_tag.xml",
        "views/view_crm_lost_reason.xml",
        "views/view_crm_stage.xml",
    ],
    "installable": True,
}
