# -*- coding: utf-8 -*-
{
    'name': "editable_expenses",

    'summary': """
        remplazar campo para poder editar en el modulo gastos en un estado""",

    'description': """
        editar campos en el estado approved
    """,

    'author': "XMARTS",
    'email': 'desarrollo@xmarts.com',
    'website': "https://xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_expense'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
}
