# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, models
from odoo.exceptions import ValidationError


class AbstractWizard(models.AbstractModel):
    _inherit = "account_financial_report_abstract_wizard"

    @api.model
    def _get_forbidden_pdf_reports(self):
        forbidden_pdf_reports = []
        forbidden_report_parameter = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("forbidden.pdf.financial.reports")
        )
        if forbidden_report_parameter:
            forbidden_pdf_reports = forbidden_report_parameter.replace(" ", "").split(
                ","
            )
        return forbidden_pdf_reports

    def button_export_pdf(self):
        self.ensure_one()
        if self._name in self._get_forbidden_pdf_reports():
            raise ValidationError(
                _(
                    "{} PDF reports are not permitted. You can generate it in "
                    "XLSX format and print it as a PDF file"
                ).format(self._description)
            )
        return super().button_export_pdf()
