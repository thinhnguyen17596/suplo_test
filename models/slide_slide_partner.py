# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, fields
from odoo.exceptions import UserError


class SlideSlidePartnerInherit(models.Model):
    _inherit = 'slide.slide.partner'
    _description = 'Customize slide slide partner'

    @api.model
    def create(self, vals):
        result = super(SlideSlidePartnerInherit, self).create(vals)
        
        # check total attendee in slide_id if total attendee greater capacity in room raise error
        if result.slide_id:
            total_attendee = self.env['slide.slide.partner'].search_count([('slide_id', '=', result.slide_id.id)])
            if total_attendee > result.slide_id.class_room_id.capacity:
                raise UserError('Number of attendees can not exceed capacity!')

        # check person can not be an instructor and attendee of the same course and the same lesson.
        if result.partner_id:
            if result.partner_id.id == result.channel_id.user_id.self.id:
                raise UserError(
                    'You can not be an instructor and attendee of the same course and the same lesson!')
            
        return result

    