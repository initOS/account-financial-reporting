# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2011 Camptocamp SA (http://www.camptocamp.com)
#
# Author: Guewen Baconnier (Camptocamp)
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

import time

from lxml import etree
from datetime import datetime
from openerp.osv import fields, orm
from openerp.tools.translate import _


class AccountBalanceCommonWizard(orm.TransientModel):

    """Will launch trial balance report and pass required args"""

    _inherit = "account.common.account.report"
    _name = "account.common.balance.report"
    _description = "Common Balance Report"

    def _get_account_ids(self, cr, uid, context=None):
        res = False
        if context.get('active_model', False) == 'account.account' \
                and context.get('active_ids', False):
            res = context['active_ids']
        return res

    _columns = {
        'account_ids': fields.many2many(
            'account.account', string='Filter on accounts',
            help="Only selected accounts will be printed. Leave empty to \
            print all accounts."),
        'date_range': fields.many2one(
            'date.range',
            string='Date Range'
        ),
        'comparison_date_range': fields.many2one(
            'date.range',
            string='Date Range'
        ),
        'comparison_date_start': fields.datetime(
            string='Start Date'
        ),
        'comparison_date_end': fields.datetime(
            string='End Date'
        ),
        'partner_ids': fields.many2many(
            'res.partner', string='Filter on partner',
            help="Only selected partners will be printed. \
              Leave empty to print all partners."),
    }

    _defaults = {
        'account_ids': _get_account_ids,
    }

    def pre_print_report(self, cr, uid, ids, data, context=None):
        data = super(AccountBalanceCommonWizard, self).pre_print_report(
            cr, uid, ids, data, context)
        return data
