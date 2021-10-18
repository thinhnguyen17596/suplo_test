# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, fields, _
from odoo.exceptions import UserError


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'
    _description = 'Customize res_partner'
    

