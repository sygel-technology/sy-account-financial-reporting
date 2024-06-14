.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl
    :alt: License: AGPL-3

===================================
Account Financial Reports Block PDF
===================================

This module allows to block the generation of financial reports in PDF format.
It is possible to configure the list of financial reports that have to be blocked. 


Configuration
=============

To configure the list of financial reports that cannot be printed in PDF you need to:

* Go to Settings > Technical > System Parameters.
* Find or create a system parameter called "forbidden.pdf.financial.reports".
* Introduce the technical name of the wizard generator models that need to be blocked
  separated by commas. The link between the financial reports in the module 
  account_financial_report and the technical name of their wizards is as follows:

  * General Ledger: general.ledger.report.wizard
  * Journal Ledger: journal.ledger.report.wizard
  * Trial Balance: trial.balance.report.wizard
  * Open Items: open.items.report.wizard
  * Aged Partner Balance: aged.partner.balance.report.wizard
  * VAT Report: vat.report.wizard

For instance, if the PDF generation of the General Ledger and Trial Balance reports have
to be blocked, the "forbidden.pdf.financial.reports" system parameter should contain the
value "general.ledger.report.wizard,trial.balance.report.wizard" (with no quotes).

Keep in mind that all the PDF reports are blocked by default when this module is
installed.

If a new report that inherits the abstract class account_financial_report_abstract_wizard
is developed, its PDF report can also be blocked by adding the name of its own wizard
in the "forbidden.pdf.financial.reports" system parameter list.


Usage
=====

When a user tries to generate the PDF file of a financial report whose PDF file have
been blocked, an error message appears.


Bug Tracker
===========

Bugs and errors are managed in `issues of GitHub <https://github.com/sygel-technology/sy-account-financial-reporting/issues>`_.
In case of problems, please check if your problem has already been
reported. If you are the first to discover it, help us solving it by indicating
a detailed description `here <https://github.com/sygel-technology/sy-account-financial-reporting/issues/new>`_.

Do not contact contributors directly about support or help with technical issues.


Credits
=======

Authors
~~~~~~~

* Sygel, Odoo Community Association (OCA)


Contributors
~~~~~~~~~~~~

* `Sygel <https://www.sygel.es>`__:

  * Manuel Regidor <manuel.regidor@sygel.es>
  * Valentin Vinagre <valentin.vinagre@sygel.es>


Maintainer
~~~~~~~~~~

This module is maintained by Sygel.

.. image:: https://www.sygel.es/logo.png
   :alt: Sygel
   :target: https://www.sygel.es

This module is part of the `Sygel/sy-account-financial-reporting <https://github.com/sygel-technology/sy-account-financial-reporting>`_.

To contribute to this module, please visit https://github.com/sygel-technology/.
