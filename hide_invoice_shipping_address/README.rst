.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
	:target: http://www.gnu.org/licenses/agpl
	:alt: License: AGPL-3


=============================
Hide Invoice Shipping Address
=============================
This module keeps the shipping address hidden on the invoice.


Installation
============
To install this module, you need to:

#. Just install.


Configuration
=============

To configure this module, you need to:

#. Activate or deactivate the "Print The Shipping Invoice On The Invoice" option in 
   Accounting > configuration > Settings > Customer Invoices if the shipping address has 
   to be shown or hidden in customer invoices PDFs. This option applies when the customer does
   not have a value set in its field "Print The Shipping Invoice On The Invoice".

#. The "Print The Shipping Invoice On The Invoice" field can be found in the "Sales/Purchases" 
   tab in the partner form view. Select "Yes" or "No" depending on whether the invoice address has 
   to be shown in customer invoices PDFs. If no option is set, it will be applied the option selected 
   in the field "Print The Shipping Invoice On The Invoice" in Accounting > Configration > Settings > Customer Invoices.


Usage
=====

To use this module, you need to:

#. On the sales invoice, just below the customer shipping address, we will find a check that will 
   indicate whether or not this invoice will hide the shipping address when printed. This option will 
   mainly take into account the settings specified in the shipping address contact. If it is blank, 
   check the client configuration. And if it is also empty, it takes into account the general configuration we have. 


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

* Valentin Vinagre <valentin.vinagre@sygel.es>
* Roger Sans <roger.sans@sygel.es>


Maintainer
~~~~~~~~~~

This module is maintained by Sygel.

.. image:: https://www.sygel.es/logo.png
   :alt: Sygel
   :target: https://www.sygel.es


This module is part of the `Sygel/sy-account-financial-reporting <https://github.com/sygel-technology/sy-account-financial-reporting>`_.

To contribute to this module, please visit https://github.com/sygel-technology.
