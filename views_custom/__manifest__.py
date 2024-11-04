# -*- coding: utf-8 -*-
{
    'name': 'Personalizacion de Vistas',
    'category': 'Hidden',
    'summary': 'Custom Views',
    'description': "Custom Views",
    'depends': ['base', 'contacts', 'sale'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'views_custom/static/src/scss/*.css',
        ],
    },
    'application': False,
    'license': 'LGPL-3',
}
