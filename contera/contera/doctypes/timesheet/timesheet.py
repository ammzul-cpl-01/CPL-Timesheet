import frappe
from datetime import datetime


def has_role(user, role):
    user_roles = frappe.get_roles(user)
    print(user_roles)
    return role in user_roles


@frappe.whitelist()
def before_save(doc, _method):
    for time_log in doc.time_logs:
        project = frappe.get_doc("Project", time_log.project)
        start_date = project.expected_start_date
        end_date = project.expected_end_date

        print(doc.custom_date)
        if datetime.strptime(doc.custom_date, '%Y-%m-%d').date() < start_date or datetime.strptime(doc.custom_date,
                                                                                                   '%Y-%m-%d').date() > end_date:
            frappe.throw("Time Log From Time must be between Project Start Date and End Date")

    today_sheets = frappe.get_all("Timesheet", filters={"employee": doc.employee, "custom_date": doc.custom_date},
                                  fields=["*"])

    if len(today_sheets) > 0 and today_sheets[0].name != doc.name and today_sheets[0].docstatus == 1:
        frappe.throw("An Active Timesheet for " + doc.custom_date + " already exists")

    if doc.total_hours > 24:
        frappe.throw("Total Hours must be less than 24")

    employee = frappe.get_doc("Employee", doc.employee)
    holiday_list = frappe.get_doc("Holiday List", employee.holiday_list)
    holidays = holiday_list.holidays
    is_holiday = False

    for holiday in holidays:
        if str(holiday.holiday_date) == doc.custom_date:
            is_holiday = True
            break

    if not is_holiday and doc.total_hours < 8 and not has_role(frappe.session.user, "Administrator"):
        frappe.throw("Total Hours must be at least 8")

    previous_to_time = None  # Initialize to None for the first entry

    for time_log in doc.time_logs:
        if previous_to_time is None:
            # Set the start time for the first entry
            time_log.from_time = doc.custom_date + " 10:00:00"
        else:
            # Set the start time for subsequent entries as the previous entry's end time
            time_log.from_time = previous_to_time

        # Use frappe.utils.add_to_date to calculate to_time based on from_time and hours
        time_log.to_time = frappe.utils.add_to_date(time_log.from_time, hours=time_log.hours)

        # Update previous_to_time for the next iteration
        previous_to_time = time_log.to_time
