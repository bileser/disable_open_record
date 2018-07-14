# -*- coding: utf-8 -*-
{
    'name': "disable_open_record_example",

    'summary':  """
                    examples and comments for using disable_open_record which makes it possible disabling opening records in a tree view as annoying popups
                """,

    'description': """
        examples and comments for using disable_open_record which makes it possible disabling opening records in a tree view as annoying popups
        """,

    'author': "Oliver Schneider",
    'category': 'Odoo View',

    # always loaded
    'data': [
        'views/example_1.xml'
        , 'views/example_2.xml'
    ],

    'depends': ['disable_open_record', 'sale']

}
