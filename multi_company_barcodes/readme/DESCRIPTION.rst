This module extend Odoo functionnalities, regarding multi companies features,
for the Barcodes module.

* It adds company field on ``barcode.nomenclature`` model and it related ``barcode.rule``
  model, with according ``ir.rule``.

* It adds company fields on the tree, form and search views, of each model
  if this field is not available.
