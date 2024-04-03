import frappe

@frappe.whitelist()

def daily():
    # check if any timesheet is not submitted
    timesheets = frappe.get_all("Timesheet", filters={"status": "Draft"}, fields=["name"])

    if timesheets:
        # Timesheets are not submitted
        for timesheet in timesheets:
            # submit timesheet if it is older than 5 days
            if timesheet.modified < frappe.utils.add_days(frappe.utils.nowdate(), -5):
                frappe.db.set_value("Timesheet", timesheet.name, "status", "Submitted")
    else:
        # All timesheets are submitted
        pass

@frappe.whitelist()
def monthly():
    from frappe.utils import getdate
    month = getdate(frappe.utils.today()).month-1
    year = getdate(frappe.utils.today()).year
    if month == 0:
        month = 12
        year = year - 1
    from_date = str(year) + "-" + str(month) + "-01"
    to_date = str(year) + "-" + str(month) + "-31"

    # check if any timesheet is not submitted
    timesheets = frappe.get_all("Timesheet", filters=[["Timesheet", "docstatus", "=", 0],["Timesheet", "custom_date", "between", [from_date, to_date]]], fields=["name"])


    if timesheets:
        # Timesheets are not submitted
        for timesheet in timesheets:
            frappe.db.set_value("Timesheet", timesheet.name, "docstatus", 1)
    else:
        # All timesheets are submitted
        pass
