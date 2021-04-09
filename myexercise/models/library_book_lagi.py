from odoo import models, fields, api

class LibraryBookLagi(models.Model):
    _name = 'library.book.lagi'
    _description = 'Library Book Lagi'

    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')
    state = fields.Selection([
        ('draft', 'Not Available'),
        ('available', 'Available'), 
        ('lost', 'Lost')],
        'State', default="draft")
        
    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('draft', 'available'), ('available', 'borrowed'),
                    ('borrowed', 'available'), ('available', 'lost'),
                    ('borrowed', 'lost'), ('lost', 'available')]
        return (old_state, new_state) in allowed

    def change_state(self, new_state):
        for book in self:
            if book.is_allowed_transition(book.state, new_state):
                book.state = new_state
            else:
                continue

    def make_available(self):
        self.change_state('available')

    def make_borrowed(self):
        self.change_state('borrowed')

    def make_lost(self):
        self.change_state('lost')