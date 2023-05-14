# -*- coding: utf-8 -*-
# Powered by Federico Ranieri.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

from odoo import models, fields, api
from odoo.tools import datetime
from odoo.tools.float_utils import float_compare, float_round


class AccountMove(models.Model):
    _inherit = 'account.move'

    fatturapa_aruba_state_sdi = fields.Char(related='fatturapa_attachment_out_id.aruba_sdi_state')

