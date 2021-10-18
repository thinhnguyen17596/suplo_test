# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, fields


class SlideChannelInherit(models.Model):
    _inherit = 'slide.channel'
    _description = 'Customize slide channel'
    
    class_room_id = fields.Many2one(comodel_name='class.room', string='Room name', required=True)