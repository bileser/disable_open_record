# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrderLine(models.Model):

    _name = 'sale.order.line'
    _inherit = 'sale.order.line'

    @api.multi
    def open_this(self):
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': False,
            'res_model': 'sale.order.line',
            'type': 'ir.actions.act_window',
            'nodestroy': True,
            'target': 'current',
            'res_id': self.id,
        }