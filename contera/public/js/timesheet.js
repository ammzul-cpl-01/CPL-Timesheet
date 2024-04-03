const formatDate = (date) => {
  const year = date.getFullYear();
  const month = (date.getMonth() + 1).toString().padStart(2, "0");
  const day = date.getDate().toString().padStart(2, "0");
  const hours = date.getHours().toString().padStart(2, "0");
  const minutes = date.getMinutes().toString().padStart(2, "0");
  const seconds = date.getSeconds().toString().padStart(2, "0");

  return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
};

frappe.ui.form.on("Timesheet", {
  onload: async function (frm, cdt, cdn) {
    frm.time_logs = [];
    if(!frappe.user.has_role("System Manager") || !frappe.user.has_role("Administrator")){
    setTimeout(() => {
      // Select the <use> element with the href attribute value '#icon-setting-gear'
      document.getElementsByClassName('form-grid')[0].children[0].children[0].firstChild.lastChild.style.pointerEvents = 'none'
    }, 500);
  }
  },
  custom_date: function (frm) {
    if (!frm.doc.custom_date) {
      frappe.throw("Please select Date");
    } else {
      let previousToTime = null; // Initialize to null for the first entry

      frm.doc.time_logs.forEach((time_log) => {
        if (previousToTime === null) {
          // Set the start time for the first entry
          time_log.from_time = `${frm.doc.custom_date} 10:00:00`;
        } else {
          // Set the start time for subsequent entries as the previous entry's end time
          time_log.from_time = previousToTime;
        }
        // Use native JavaScript Date object to calculate to_time based on from_time and hours
        const fromTimeDate = new Date(time_log.from_time);
        const toTimeDate = new Date(
          fromTimeDate.getTime() + time_log.hours * 60 * 60 * 1000
        );
        // Format to_time as YYYY-MM-DD HH:mm:ss
        time_log.to_time = formatDate(toTimeDate);
        // Update previousToTime for the next iteration
        previousToTime = formatDate(toTimeDate);
      });
    }
  },
});

frappe.ui.form.on("Timesheet Detail", {
  hours: function (frm, cdt, cdn) {
    if (!frm.doc.custom_date) {
      frappe.throw("Please select Date");
    } else {
      let previousToTime = null; // Initialize to null for the first entry

      frm.doc.time_logs.forEach((time_log) => {
        if (previousToTime === null) {
          // Set the start time for the first entry
          time_log.from_time = `${frm.doc.custom_date} 10:00:00`;
        } else {
          // Set the start time for subsequent entries as the previous entry's end time
          time_log.from_time = previousToTime;
        }

        // Use native JavaScript Date object to calculate to_time based on from_time and hours
        const fromTimeDate = new Date(time_log.from_time);
        const toTimeDate = new Date(
          fromTimeDate.getTime() + time_log.hours * 60 * 60 * 1000
        );

        // Format to_time as YYYY-MM-DD HH:mm:ss
        console.log(fromTimeDate, toTimeDate);
        time_log.to_time = formatDate(toTimeDate);

        // Update previousToTime for the next iteration
        previousToTime = formatDate(toTimeDate);
      });
    }
  },
});
