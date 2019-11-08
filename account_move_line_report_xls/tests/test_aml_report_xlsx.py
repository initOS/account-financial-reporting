# Copyright 2009-2018 Noviat.
# Copyright 2020 initOS GmbH <https://initos.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestAmlReportXlsx(TransactionCase):

    def setUp(self):
        super(TestAmlReportXlsx, self).setUp()
        inv = self.env.ref('l10n_generic_coa.demo_invoice_1')
        ctx = {
            'report_name': 'account_move_line_report_xls.account_move_line_xlsx',
            'active_model': 'account.move.line',
            'active_ids': inv.move_id.line_ids.ids,
        }
        self.report = self.env['ir.actions.report'].with_context(ctx)

    def test_aml_report_xlsx(self):
        report_xls = self.report.render_xlsx(None, None)
        self.assertEqual(report_xls[1], 'xlsx')
