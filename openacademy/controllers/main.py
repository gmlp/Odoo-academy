from openerp import http
from openerp.http import Controller, route

class Academy(Controller):


    @route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        teachers = http.request.env['openacademy.teacher']
        return http.request.render('openacademy.index', {
            'teachers': teachers.search([])
        })
    @http.route('/academy/<model("openacademy.teacher"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        print teacher.write_date
        return http.request.render('openacademy.biography', {
            'person': teacher
        })
