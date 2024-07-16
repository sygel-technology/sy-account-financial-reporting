# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    invoice_shipping_address_print = fields.Selection(
        string="Print The Shipping Invoice On The Invoice",
        selection=[
            ("show", "Show"),
            ("hide", "Hide"),
        ],
    )
