from openerp import http
from openerp.http import Controller, route

class Academy(Controller):


    @route('/academy/academy/', auth='public')
    def index(self, **kw):
        return http.request.render('openacademy.index', {
            'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
        })
