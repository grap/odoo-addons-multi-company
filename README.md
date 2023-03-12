
<!-- /!\ Non OCA Context : Set here the badge of your runbot / runboat instance. -->
[![Pre-commit Status](https://github.com/grap/odoo-addons-multi-company/actions/workflows/pre-commit.yml/badge.svg?branch=12.0)](https://github.com/grap/odoo-addons-multi-company/actions/workflows/pre-commit.yml?query=branch%3A12.0)
[![Build Status](https://github.com/grap/odoo-addons-multi-company/actions/workflows/test.yml/badge.svg?branch=12.0)](https://github.com/grap/odoo-addons-multi-company/actions/workflows/test.yml?query=branch%3A12.0)
[![codecov](https://codecov.io/gh/grap/odoo-addons-multi-company/branch/12.0/graph/badge.svg)](https://codecov.io/gh/grap/odoo-addons-multi-company)
<!-- /!\ Non OCA Context : Set here the badge of your translation instance. -->

<!-- /!\ do not modify above this line -->

# Odoo Modules that add extra features to make Odoo working in multicompany context

 This project aim to deal with modules related to manage multi company in Odoo.
The modules will mainly add :
- Add a company_id fields on some models.
- Alter rules to make the access to the model, depending of the current company.
- Add company_id field on each form / tree / search view if the field is not available.


<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[multi_company_account](multi_company_account/) | 12.0.1.1.2 |  | Handle Multi company for Account Module
[multi_company_barcodes](multi_company_barcodes/) | 12.0.1.1.2 |  | Handle Multi company for Barcodes Module
[multi_company_base](multi_company_base/) | 12.0.1.1.3 |  | Handle Multi company for Base Module
[multi_company_crm](multi_company_crm/) | 12.0.1.1.1 |  | Handle Multi company for CRM Module
[multi_company_point_of_sale](multi_company_point_of_sale/) | 12.0.1.1.1 |  | Handle Multi company for Point of Sale Module
[multi_company_product](multi_company_product/) | 12.0.1.1.2 |  | Handle Multi company for Product Module
[multi_company_sale](multi_company_sale/) | 12.0.1.1.1 |  | Handle Multi company for Sale Module
[multi_company_sale_management](multi_company_sale_management/) | 12.0.1.1.1 |  | Handle Multi company for Sale Management Module
[multi_company_sales_team](multi_company_sales_team/) | 12.0.1.1.1 |  | Handle Multi company for Sales Team Module

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to GRAP
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----

## About GRAP

<p align="center">
   <img src="http://www.grap.coop/wp-content/uploads/2016/11/GRAP.png" width="200"/>
</p>

GRAP, [Groupement Régional Alimentaire de Proximité](http://www.grap.coop) is a
french company which brings together activities that sale food products in the
region Rhône Alpes. We promote organic and local food, social and solidarity
economy and cooperation.

The GRAP IT Team promote Free Software and developp all the Odoo modules under
AGPL-3 Licence.

You can find all these modules here:

* on the [OCA Apps Store](https://odoo-community.org/shop?&search=GRAP)
* on the [Odoo Apps Store](https://www.odoo.com/apps/modules/browse?author=GRAP).
* on [Odoo Code Search](https://odoo-code-search.com/ocs/search?q=author%3AOCA+author%3AGRAP)

You can also take a look on the following repositories:

* [grap-odoo-incubator](https://github.com/grap/grap-odoo-incubator)
* [grap-odoo-business](https://github.com/grap/grap-odoo-business)
* [grap-odoo-business-supplier-invoice](https://github.com/grap/grap-odoo-business-supplier-invoice)
* [odoo-addons-logistics](https://github.com/grap/odoo-addons-logistics)
* [odoo-addons-cae](https://github.com/grap/odoo-addons-cae)
* [odoo-addons-intercompany-trade](https://github.com/grap/odoo-addons-intercompany-trade)
* [odoo-addons-multi-company](https://github.com/grap/odoo-addons-multi-company)
* [odoo-addons-company-wizard](https://github.com/grap/odoo-addons-company-wizard)
