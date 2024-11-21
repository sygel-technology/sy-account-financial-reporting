# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests import tagged

from odoo.addons.account.tests.common import AccountTestInvoicingCommon


@tagged("post_install", "-at_install")
class TestFooterExtraInfoAccountMove(AccountTestInvoicingCommon):
    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super().setUpClass(chart_template_ref=chart_template_ref)

    def test_footer_extra_info(self):
        footer_extra_info_invoice = self.create_invoice()
        self.fiscal_pos_a.write({"footer_extra_info": "EXTRA INFO"})
        footer_extra_info_invoice.write({"fiscal_position_id": self.fiscal_pos_a.id})
        self.assertTrue(
            footer_extra_info_invoice.footer_extra_info,
        )
        self.assertEqual(
            footer_extra_info_invoice.footer_extra_info,
            footer_extra_info_invoice.fiscal_position_id.footer_extra_info,
        )
