{
    'name': "mytest_2",
    'summary': "Manage books easily",
    'description': """
Manage Library
==============
Description related to library.
""",
    'author': "Your name",
    'website': "http://www.example.com",
    'category': 'Uncategorized',
    'version': '15.0.13.0.1.0.1',
    'depends': ['base', 'account', 'sale_management'],
    'data': ['security/groups.xml',
             'security/ir.model.access.csv',
             'views/product_template_inherit.xml'],
    'demo': ['data/demo.xml'],
}
