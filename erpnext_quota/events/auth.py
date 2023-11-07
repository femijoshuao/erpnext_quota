import frappe
from frappe import _
from frappe.utils.data import date_diff, today


def successful_login(login_manager):
    """
    on_login verify if site is not expired
    """
    quota = frappe.get_site_config()['quota']
    valid_till = quota['valid_till']
    diff = date_diff(valid_till, today())
    if diff < 0:
        frappe.throw(_("Dear Customer, your ERP instance has been temporarily suspended due to an inactive subscription. Please renew your subscription on time to avoid permanent deletion of your data. For more information, please contact sales."), frappe.AuthenticationError)
