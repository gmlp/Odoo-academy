from openerp import models, fields, api


class Teacher(models.Model):
    _name = 'openacademy.teacher'

    name = fields.Char()
    biography = fields.Html()
    course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")
