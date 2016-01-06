from openerp import models, fields, api


class Teacher(models.Model):
    _name = 'openacademy.teacher'

    name = fields.Char()
