import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-account-financial-reporting",
    description="Meta package for sygel-technology-sy-account-financial-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_financial_report_block_pdf>=16.0dev,<16.1dev',
        'odoo-addon-footer_extra_info_account_move>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
