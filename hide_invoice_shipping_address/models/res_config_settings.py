# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    invoice_shipping_address_print = fields.Boolean(
        string="Print The Shipping Invoice On The Invoice",
        related="company_id.invoice_shipping_address_print",
        readonly=False,
    )
