# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Footer Extra Info Account Move",
    "summary": "Footer Extra Info in invoices PDF",
    "version": "16.0.1.0.0",
    "category": "Account",
    "website": "https://github.com/sygel-technology/sy-account-financial-reporting",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["footer_extra_info_base", "account"],
    "data": ["views/account_fiscal_position_views.xml"],
}
