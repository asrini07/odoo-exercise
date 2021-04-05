# -*- coding: utf-8 -*-
# from odoo import http


# class Myexercise(http.Controller):
#     @http.route('/myexercise/myexercise/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myexercise/myexercise/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('myexercise.listing', {
#             'root': '/myexercise/myexercise',
#             'objects': http.request.env['myexercise.myexercise'].search([]),
#         })

#     @http.route('/myexercise/myexercise/objects/<model("myexercise.myexercise"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myexercise.object', {
#             'object': obj
#         })
