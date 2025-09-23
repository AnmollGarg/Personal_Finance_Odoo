{
    'name': 'Personal Finance',
    'version': '1.0',
    'summary': '',
    'description': '',
    'category': 'Finance',
    'depends': ['base', 'mail'],
    'data': [
        'data/ir.sequence.xml',
        'views/personal_finance_views.xml',
        'views/personal_finance_bank_views.xml',
        'views/personal_finance_menus.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}