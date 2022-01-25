# Copyright (C) 2013-Today: GRAP (http://www.grap.coop)
# @author: Julien WESTE
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Multi Company - Account Module",
    "version": "12.0.1.1.2",
    "category": "Multi Company",
    "summary": "Handle Multi company for Account Module",
    "author": "GRAP",
    "website": "https://github.com/grap/odoo-addons-multi-company",
    "license": "AGPL-3",
    "depends": [
        "account",
        # GRAP
        "multi_company_base",
    ],
    "data": [
        "views/view_account_account.xml",
        "views/view_account_invoice.xml",
        "views/view_account_journal.xml",
        "views/view_account_move.xml",
        "views/view_account_move_line.xml",
        "views/view_account_payment.xml",
    ],
    "demo": [
        "demo/res_groups.xml",
    ],
    "installable": True,
}
