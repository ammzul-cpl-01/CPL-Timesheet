app_name = "contera"
app_title = "Contera"
app_publisher = "Hybrowlabs Technologies"
app_description = "contera timesheet customisations"
app_email = "support@hybrowlabs.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/contera/css/contera.css"
# app_include_js = "/assets/contera/js/contera.js"

# include js, css files in header of web template
# web_include_css = "/assets/contera/css/contera.css"
# web_include_js = "/assets/contera/js/contera.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "contera/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Timesheet" : "public/js/timesheet.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "contera/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "contera.utils.jinja_methods",
# 	"filters": "contera.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "contera.install.before_install"
# after_install = "contera.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "contera.uninstall.before_uninstall"
# after_uninstall = "contera.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "contera.utils.before_app_install"
# after_app_install = "contera.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "contera.utils.before_app_uninstall"
# after_app_uninstall = "contera.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "contera.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
    "Timesheet": {
        "before_save": "contera.contera.doctypes.timesheet.timesheet.before_save",
    },
    "Project": {
		"on_update": "contera.contera.doctypes.project.project.on_update"
	}
}

# Scheduled Tasks
# ---------------

scheduler_events = {
	# "all": [
	# 	"contera.tasks.all"
	# ],
	# "daily": [
	# 	"contera.tasks.daily"
	# ],
	# "hourly": [
	# 	"contera.tasks.hourly"
	# ],
	# "weekly": [
	# 	"contera.tasks.weekly"
	# ],
 	"cron": {
		"00 14 9 * *": [
			"contera.tasks.monthly"
		],
 	}
}

# Testing
# -------

# before_tests = "contera.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "contera.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "contera.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["contera.utils.before_request"]
# after_request = ["contera.utils.after_request"]

# Job Events
# ----------
# before_job = ["contera.utils.before_job"]
# after_job = ["contera.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"contera.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

