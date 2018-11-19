# -*- coding: utf-8 -*-
{
    'name': "aniway_improve",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Aniway improvements
    """,

    'author': "NBE",
    'website': "http://www.nbe.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'models/product_template.xml',
        'views/product_template.xml',
        'views/point_of_sale_assets.xml',
    ],

    'qweb': [
        'static/src/xml/pos.xml',
    ],

}