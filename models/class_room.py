# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, fields

class ClassRoom(models.Model):
    _name = 'class.room'
    _description = 'Place where courses are held'

    name = fields.Char(string="Room name")
    capacity = fields.Integer(string='Capacity')