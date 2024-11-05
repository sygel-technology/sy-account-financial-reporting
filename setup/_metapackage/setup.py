import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-sygel-technology-sy-account-financial-reporting",
    description="Meta package for sygel-technology-sy-account-financial-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-account_financial_report_block_pdf',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 13.0',
    ]
)
