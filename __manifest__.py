# -*- coding: utf-8 -*-
{
    'name': "Suplo test",
    'summary': """Suplo test""",
    'description': """
    """,
    'author': "Thinh Nguyen",
    'website': "",
    'category': 'web',
    'version': '14.0.1.0.0',
    'depends': ['website', 'base', 'website_slides',],
    'data': [
        'security/ir.model.access.csv',
        'views/slide_channel_view.xml',
        'views/class_rooms_view.xml',
        'views/slide_slide_view.xml',
        'views/res_partner_view.xml',

    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
