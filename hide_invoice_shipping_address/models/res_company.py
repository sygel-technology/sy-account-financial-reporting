# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    invoice_shipping_address_print = fields.Boolean(
        string='Print The Shipping Invoice On The Invoice',
        default=True,
    )
