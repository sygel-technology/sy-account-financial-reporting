# Copyright 2025 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class TestAccountFinancialReportBlockPdf(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.config = cls.env["ir.config_parameter"].sudo()
        cls.wizard_model = cls.env["general.ledger.report.wizard"]

    def test_button_export_pdf_blocked(self):
        self.config.set_param(
            "forbidden.pdf.financial.reports", "general.ledger.report.wizard"
        )
        wizard = self.wizard_model.create(
            {
                "company_id": self.env.company.id,
            }
        )
        with self.assertRaises(ValidationError) as e:
            wizard.button_export_pdf()
        self.assertIn("PDF reports are not permitted", str(e.exception))
