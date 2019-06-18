# -*- coding: utf-8 -*-
from odoo import http

# class TvReplace(http.Controller):
#     @http.route('/tv_replace/tv_replace/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tv_replace/tv_replace/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tv_replace.listing', {
#             'root': '/tv_replace/tv_replace',
#             'objects': http.request.env['tv_replace.tv_replace'].search([]),
#         })

#     @http.route('/tv_replace/tv_replace/objects/<model("tv_replace.tv_replace"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tv_replace.object', {
#             'object': obj
#         })