from openerp import fields, models


class OnlineCourse(models.Model):
    _inherit = 'product.template'

    teacher_id = fields.Many2one('openacademy.teacher', string="Teacher")

