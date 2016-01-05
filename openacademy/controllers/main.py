from openerp.http import Controller, route


class Academy(Controller):
    @route('/academy/academy/', auth='public')
    def index(self, **kw):
        return "HELLO, WORLD"
