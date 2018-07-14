# -*- coding: utf-8 -*-
from odoo import models, fields

class DeCodeschneiderParent(models.Model):

    _name = 'de.codeschneider.parent'

    name = fields.Char("Description of this Wrapper")

    property_1 = fields.Char("Property 1")

    child_ids = fields.One2many('de.codeschneider.child', 'parent_id', 'Child Objects')
