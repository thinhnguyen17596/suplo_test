# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, fields
from odoo.exceptions import UserError


class SlideChannelPartnerInherit(models.Model):
    _inherit = 'slide.channel.partner'
    _description = 'Customize slide channel partner'
    
    @api.model
    def create(self, vals):
        result = super(SlideChannelPartnerInherit, self).create(vals)
        
        # check total attendee in slide_id if total attendee greater capacity in room raise error
        if result.channel_id:
            total = self.env['slide.channel.partner'].search_count([('channel_id', '=', result.channel_id.id)])
            if total > result.channel_id.class_room_id.capacity:
                raise UserError('Number of attendees can not exceed capacity!')
            
        # check person can not be an instructor and attendee of the same course and the same lesson.
        if result.partner_id:
            if result.partner_id.id == result.channel_id.user_id.self.id:
                raise UserError('You can not be an instructor and attendee of the same course and the same lesson!')
        
        return result

