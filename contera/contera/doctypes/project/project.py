import frappe


@frappe.whitelist()
def on_update(doc, _method):
    if doc.expected_start_date and doc.expected_end_date:
        if doc.expected_start_date > doc.expected_end_date:
            frappe.throw("Expected Start Date must be before Expected End Date")

    permission_doc_name = "User Permission"
    # remove permission for all the users
    permissions = frappe.get_all(permission_doc_name, filters={"allow": "Project", "for_value": doc.name}, fields=["name"])
    for permission in permissions:
        frappe.delete_doc(permission_doc_name, permission.name)

    # create permission if user is added to project
    for user in doc.users:
        # check if user permission for that particular project is there or not, if not then create one for that user
            frappe.get_doc({
                "doctype": permission_doc_name,
                "allow": "Project",
                "for_value": doc.name,
                "user": user.user
            }).insert(ignore_permissions=True)
