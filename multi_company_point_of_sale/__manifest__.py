# Copyright (C) 2020-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Multi Company - Point of Sale Module",
    "version": "12.0.1.1.0",
    "category": "Multi Company",
    "summary": "Handle Multi company for Point of Sale Module",
    "author": "GRAP",
    "website": "http://www.grap.coop",
    "license": "AGPL-3",
    "depends": [
        "multi_company_base",
        "point_of_sale",
    ],
    "data": [
        "security/ir_rule.xml",
    ],
    "installable": True,
}
