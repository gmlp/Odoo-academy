from openerp import fields, models


class OnlineCourse(models.Model):
    _name = 'openacademy.online_course'
    _inherit = 'mail.thread'

    name = fields.Char()
    teacher_id = fields.Many2one('openacademy.teacher', string="Teacher")

