# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    invoice_shipping_address_print = fields.Boolean(
        string="Print The Shipping Invoice On The Invoice",
        compute="_compute_invoice_shipping_address_print",
        store=True,
        readonly=False,
    )

    @api.depends("partner_shipping_id", "company_id")
    def _compute_invoice_shipping_address_print(self):
        for record in self:
            result = record.company_id.invoice_shipping_address_print
            if record.partner_shipping_id:
                partner_shipping_state = (
                    record.partner_shipping_id.invoice_shipping_address_print
                )
                if record.partner_shipping_id.invoice_shipping_address_print:
                    result = True if partner_shipping_state == "show" else False

                elif record.partner_shipping_id.commercial_partner_id:
                    partner_shipping = record.partner_shipping_id
                    commercial_partner = partner_shipping.commercial_partner_id
                    commercial_partner_state = (
                        commercial_partner.invoice_shipping_address_print
                    )
                    result = True if commercial_partner_state == "show" else False
            record.invoice_shipping_address_print = result
