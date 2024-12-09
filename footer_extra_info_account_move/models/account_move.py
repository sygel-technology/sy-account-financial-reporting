# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class AccountMove(models.Model):
    _name = "account.move"
    _inherit = ["account.move", "footer.extra.info.mixin"]

    def _compute_footer_extra_info(self):
        for move in self:
            move.footer_extra_info = move.fiscal_position_id.footer_extra_info
