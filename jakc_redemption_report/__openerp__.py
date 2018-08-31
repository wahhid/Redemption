{
    'name' : 'Redemption and Point Management - Report Module',
    'version' : '1.0',
    'author' : 'JakC',
    'category' : 'Generic Modules/Redemption And Point Management',
    'depends' : ['base_setup','base','jakc_redemption'],
    'init_xml' : [],
    'data' : [    
        'security/ir.model.access.csv',    
        'jakc_redemption_report_view.xml',        
        'jakc_redemption_report_menu.xml',       
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}