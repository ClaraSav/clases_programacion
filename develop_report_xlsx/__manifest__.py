# -*- coding: utf-8 -*-
{
    'name': 'Develop Report XLSX',
    'category': 'Hidden',
    'summary': 'Custom Report',
    'description': "Custom Report",
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/report_wizard_views.xml',
    ],
    'application': False,
    'license': 'LGPL-3',
}
