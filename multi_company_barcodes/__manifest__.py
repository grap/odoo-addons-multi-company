# Copyright (C) 2014-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Multi Company - Barcodes Module",
    "version": "12.0.1.0.3",
    "category": "Multi Company",
    "summary": "Handle Multi company for Barcodes Module",
    "author": "GRAP",
    "website": "http://www.grap.coop",
    "license": "AGPL-3",
    "depends": [
        "multi_company_base",
        "barcodes",
    ],
    "data": [
        "security/ir_rule.xml",
        "views/view_barcode_nomenclature.xml",
    ],
    "installable": True,
}
