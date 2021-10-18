# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, fields, _
from odoo.exceptions import UserError


class SlideSlideInherit(models.Model):
    _inherit = 'slide.slide'
    _description = 'Customize slide slide'
    
    class_room_id = fields.Many2one(comodel_name='class.room', string='Room name')

    @api.model
    def create(self, vals):
        result = super(SlideSlideInherit, self).create(vals)
        # default class room same slide channel
        if not result.class_room_id:
            result.class_room_id = result.channel_id.class_room_id
            
        # check total attendee in slide_id if total attendee greater capacity in room raise error
        if result.slide_partner_ids:
            if len(result.slide_partner_ids) > result.class_room_id.capacity:
                raise UserError('Number of attendees can not exceed capacity!')
        return result

    def write(self, vals):
        result = super(SlideSlideInherit, self).write(vals)

        # check total attendee in slide_id if total attendee greater capacity in room raise error
        if self.slide_partner_ids:
            if len(self.slide_partner_ids) > self.class_room_id.capacity:
                raise UserError('Number of attendees can not exceed capacity!')
    
        return result