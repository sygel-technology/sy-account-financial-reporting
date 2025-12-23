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
