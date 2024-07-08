# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    invoice_shipping_address_print = fields.Boolean(
        string='Print The Shipping Invoice On The Invoice',
        compute='_compute_invoice_shipping_address_print',
        store=True,
        readonly=False,
    )

    @api.depends('partner_shipping_id', 'company_id')
    def _compute_invoice_shipping_address_print(self):
        for record in self:
            result = record.company_id.invoice_shipping_address_print
            if record.partner_shipping_id:
                if record.partner_shipping_id.invoice_shipping_address_print:
                    result = True if record.partner_shipping_id.invoice_shipping_address_print == 'show' else False

                elif record.partner_shipping_id.commercial_partner_id.invoice_shipping_address_print:
                    result = True if record.partner_shipping_id.commercial_partner_id.invoice_shipping_address_print == 'show' else False               
            record.invoice_shipping_address_print = result
