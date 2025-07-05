# -*- coding: utf-8 -*-
{
    'name': "cleaning_company",
    'summary': "Integrated Cleaning Services App",
    'description': "Manage cleaning orders, quotations, invoices and Kanban workflow.",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Services',
    'version': '0.1',
    'depends': ['base', 'mail', 'sale', 'account'],

    'assets': {
        'web.assets_backend': [
            'cleaning_company/static/src/css/style.css',
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/cleaning_service_views.xml',
        'views/cleaning_order_views.xml',
    ],
}
