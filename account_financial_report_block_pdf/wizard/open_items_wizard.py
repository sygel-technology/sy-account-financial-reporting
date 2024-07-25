# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, models
from odoo.exceptions import ValidationError


class OpenItemsReportWizard(models.TransientModel):
    _inherit = "open.items.report.wizard"

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
