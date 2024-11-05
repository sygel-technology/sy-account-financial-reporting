import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-sygel-technology-sy-account-financial-reporting",
    description="Meta package for sygel-technology-sy-account-financial-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-account_financial_report_block_pdf',
        'odoo14-addon-hide_invoice_shipping_address',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
