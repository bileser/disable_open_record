# -*- coding: utf-8 -*-
from odoo import models, fields, api

class DeCodeschneiderChild(models.Model):

    _name = 'de.codeschneider.child'

    parent_id = fields.Many2one('de.codeschneider.parent')

    @api.depends('user_id', 'property_1', 'property_2')
    def _compute_name(self):
        for rec in self:
            rec.name = ' '.join(filter(None, [rec.user_id.name, rec.property_1, rec.property_2]))
    name = fields.Char('Description', compute=_compute_name)

    user_id = fields.Many2one('res.users', string='Some Object to jump to, User is the most basic')
    property_1 = fields.Selection([('a', 'a'), ('b', 'b'), ('c', 'c')], "Some Selection")
    property_2 = fields.Date('Some Date')


    @api.multi
    def open_this(self):
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': False,
            'res_model': 'de.codeschneider.child',
            'type': 'ir.actions.act_window',
            'nodestroy': True,
            'target': 'current',
            'res_id': self.id,
        }