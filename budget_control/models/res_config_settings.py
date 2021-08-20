# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    budget_include_tax = fields.Boolean(
        related="company_id.budget_include_tax", readonly=False
    )
    budget_kpi_template_id = fields.Many2one(
        comodel_name="mis.report",
        related="company_id.budget_kpi_template_id",
        readonly=False,
    )
    # Modules
    module_budget_control_purchase_request = fields.Boolean(string="Purchase Request")
    module_budget_control_purchase = fields.Boolean(string="Purchase")
    module_budget_control_expense = fields.Boolean(string="Expense")