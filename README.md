[![Build Status](https://travis-ci.org/odoo-cae/odoo-addons-multi-company.svg?branch=12.0)](https://travis-ci.org/odoo-cae/odoo-addons-multi-company)
[![codecov](https://codecov.io/gh/odoo-cae/odoo-addons-multi-company/branch/12.0/graph/badge.svg)](https://codecov.io/gh/odoo-cae/odoo-addons-multi-company)
[![Coverage Status](https://coveralls.io/repos/github/odoo-cae/odoo-addons-multi-company/badge.svg?branch=12.0)](https://coveralls.io/github/odoo-cae/odoo-addons-multi-company?branch=12.0)
[![Code Climate](https://codeclimate.com/github/odoo-cae/odoo-addons-multi-company/badges/gpa.svg)](https://codeclimate.com/github/odoo-cae/odoo-addons-multi-company)


Odoo Addons for Multi Company Context
=====================================

This project aim to deal with modules related to manage multi company in Odoo.

The modules will mainly add :

* Add a ```company_id``` fields on some models.

* Alter rules to make the access to the model, depending of the current company.

* Add ```company_id``` field on each form / tree / search view if the field
  is not available.

[//]: # (addons)

Available addons
----------------
addon | version | summary
--- | --- | ---
[multi_company_account](multi_company_account/) | 12.0.1.0.1 | Handle Multi company for Account Module
[multi_company_barcodes](multi_company_barcodes/) | 12.0.1.0.2 | Handle Multi company for Barcodes Module
[multi_company_base](multi_company_base/) | 12.0.1.0.1 | Handle Multi company for Base Module
[multi_company_crm](multi_company_crm/) | 12.0.1.0.1 | Handle Multi company for CRM Module
[multi_company_point_of_sale](multi_company_point_of_sale/) | 12.0.1.0.2 | Handle Multi company for Point of Sale Module
[multi_company_product](multi_company_product/) | 12.0.1.0.1 | Handle Multi company for Product Module
[multi_company_sale](multi_company_sale/) | 12.0.1.0.1 | Handle Multi company for Sale Module
[multi_company_sales_team](multi_company_sales_team/) | 12.0.1.0.1 | Handle Multi company for Sales Team Module

[//]: # (end addons)

# Funders

The development of the modules has been financially supported by:

<p align="center">
   <img src="http://www.grap.coop/wp-content/uploads/2016/11/GRAP.png" width="200"/>
</p>

GRAP, [Groupement Régional Alimentaire de Proximité](http://www.grap.coop) is a
french company which brings together activities that sale food products in the
region Rhône Alpes. We promote organic and local food, social and solidarity
economy and cooperation.

The GRAP IT Team promote Free Software and developp all the Odoo modules under
AGPL-3 Licence. You can get find all this modules here :
* on the [OCA Apps Store](https://odoo-community.org/shop?&search=GRAP)
* on the [Odoo Apps Store](https://www.odoo.com/apps/modules/browse?author=GRAP).
