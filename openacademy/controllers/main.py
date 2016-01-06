from openerp import http
from openerp.http import Controller, route

class Academy(Controller):


    @route('/academy/academy/', auth='public')
    def index(self, **kw):
        teachers = http.request.env['openacademy.teacher']
        return http.request.render('openacademy.index', {
            'teachers': teachers.search([])
        })
