# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Hide Invoice Shipping Address",
    "version": "15.0.1.0.0",
    "author": "Sygel, Odoo Community Association (OCA)",
    "category": "Reporting",
    "license": "AGPL-3",
    "summary": "Keep the shipping address hidden on the invoice.",
    "website": "https://github.com/sygel-technology/sy-account-financial-reporting",
    "depends": [
        "account",
        "sale",
    ],
    "data": [
        "views/res_partner_view.xml",
        "views/account_move_view.xml",
        "views/res_config_settings_view.xml",
        "views/res_partner_view.xml",
        "report/report_invoice.xml",
    ],
}
