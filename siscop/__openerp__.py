# -*- coding: utf-8 -*-
{
    'name': 'SISCOP UNL',
    'version': '1.0',
    #'category': 'Project Management',
    'description': '''
Module for generate Orders for Public Purchases at Universidad Nacional de Loja
''',
    'author': 'miltonlab',
    'website': 'http://1000tonlab.wordpress.com',
    'depends': ['base', 'hr', 'purchase', 'web'],
    #'update_xml': [
    #    'res.partner.csv',
    #],
    'data': [
        'hr_view.xml',
        'purchase_view.xml',
        'security/siscop_security.xml',
        'data/users.xml',
        #'data/res.users.csv',
    ],
    'js' : ['static/src/js/siscop.js'],
    'test': [
    ],
    # Set to False if you want to prevent the module to be known by OpenERP
    # (and thus appearing in the list of modules).
    'installable': True,
    # Set to True if you want the module to be automatically whenever all its
    # dependencies are installed.
    'auto_install': False,
}