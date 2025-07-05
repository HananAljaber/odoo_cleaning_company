# -*- coding: utf-8 -*-
# from odoo import http


# class CleaningCompany(http.Controller):
#     @http.route('/cleaning_company/cleaning_company', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cleaning_company/cleaning_company/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cleaning_company.listing', {
#             'root': '/cleaning_company/cleaning_company',
#             'objects': http.request.env['cleaning_company.cleaning_company'].search([]),
#         })

#     @http.route('/cleaning_company/cleaning_company/objects/<model("cleaning_company.cleaning_company"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cleaning_company.object', {
#             'object': obj
#         })

