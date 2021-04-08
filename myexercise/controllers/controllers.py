# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request, Response


class Myexercise(http.Controller):
    @http.route('/myexercise/myexercise/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    # @http.route('/api/list_event', auth='public', methods=['GET'])
    # def get_list_event(self):
    #     data = []
    #     event = request.env['example.event.odoo'].sudo().search([])
    #     headers_json = {'Content-Type': 'application/json'}    
    #     for eve in event:
    #         data.append({
    #             'name': eve.name,
    #             'description': eve.description
    #         })
    #     result = {
    #         'data': data,
    #         'errors': {},
    #         'meta': {}
    #     }
    #     return Response(json.dumps(result), headers=headers_json)

    # @http.route('/myexercise/myexercise/objects/', auth='public')
    # def list(self, **kw):
    #     return http.request.render('myexercise.listing', {
    #         'root': '/myexercise/myexercise',
    #         'objects': http.request.env['myexercise.myexercise'].search([]),
    #     })

#     @http.route('/myexercise/myexercise/objects/<model("myexercise.myexercise"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myexercise.object', {
#             'object': obj
#         })
