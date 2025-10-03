# Copyright 2025 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.tests.common import TransactionCase


class TestAccountInvoiceReportHideDeliveryAddress(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.company = cls.env["res.company"].create(
            {
                "name": "Test Company",
                "invoice_shipping_address_print": True,
            }
        )
        cls.journal = cls.env["account.journal"].create(
            {
                "name": "Test Sales Journal",
                "type": "sale",
                "code": "TSJ",
                "company_id": cls.company.id,
            }
        )
        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Cliente Principal",
                "company_id": cls.company.id,
            }
        )
        cls.partner_shipping = cls.env["res.partner"].create(
            {
                "name": "Cliente Dirección Envío",
                "parent_id": cls.partner.id,
                "type": "delivery",
                "company_id": cls.company.id,
            }
        )
        cls.invoice = cls.env["account.move"].create(
            {
                "move_type": "out_invoice",
                "partner_id": cls.partner.id,
                "company_id": cls.company.id,
                "journal_id": cls.journal.id,
            }
        )

    def test_default_company_value(self):
        self.invoice.partner_shipping_id = False
        self.invoice._compute_invoice_shipping_address_print()
        self.assertEqual(
            self.invoice.invoice_shipping_address_print,
            self.company.invoice_shipping_address_print,
        )

    def test_shipping_address_show(self):
        self.partner_shipping.invoice_shipping_address_print = "show"
        self.invoice.partner_shipping_id = self.partner_shipping
        self.invoice._compute_invoice_shipping_address_print()
        self.assertTrue(self.invoice.invoice_shipping_address_print)

    def test_shipping_address_hide(self):
        self.partner_shipping.invoice_shipping_address_print = "hide"
        self.invoice.partner_shipping_id = self.partner_shipping
        self.invoice._compute_invoice_shipping_address_print()
        self.assertFalse(self.invoice.invoice_shipping_address_print)

    def test_commercial_partner_show(self):
        self.partner_shipping.invoice_shipping_address_print = False
        self.partner.invoice_shipping_address_print = "show"
        self.invoice.partner_shipping_id = self.partner_shipping
        self.invoice._compute_invoice_shipping_address_print()
        self.assertTrue(self.invoice.invoice_shipping_address_print)

    def test_commercial_partner_hide(self):
        self.partner_shipping.invoice_shipping_address_print = False
        self.partner.invoice_shipping_address_print = "hide"
        self.invoice.partner_shipping_id = self.partner_shipping
        self.invoice._compute_invoice_shipping_address_print()
        self.assertFalse(self.invoice.invoice_shipping_address_print)
