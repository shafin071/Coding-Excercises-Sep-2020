
jQuery(document).ready(function($) {

    // Declaring all the selectors
    let emptyFieldWarning = "Please enter a task";
    let InputFieldSelector = "#myInput";
    let TableBodySelector = "#todo tbody";

    // Trigger event for "Add" button click
    // Calls appendNewTask function on event
    $(":button").click(() => {
        appendNewTask();
    }); 

   
    // Trigger event for Enter key
    // Calls appendNewTask function on event
    $('#myInput').keypress((e) => {
        if(e.which == 13) {  // 13 is the ID of Enter key
            appendNewTask();
        }  
    });

    
    /**
     * appendNewTask description:
     * This function checks if the input field is empty on trigger events. 
     * Will send alert to the user if field is empty
     * Otherwise, append the new task to the Tasks table
     * 
     * @param Args: None
     * @param Returns: None
     */
    function appendNewTask () {
        let newTask = $(InputFieldSelector).val();
        if (!newTask) {
            alert(emptyFieldWarning);
        }
        else {
            // Append new row to table
            $(TableBodySelector).append(
                '<tr class="row"><td>' + newTask + '</td><td class="t_completed"></td><td class="item_complete"> <input type="checkbox"> </td></tr>'
                );
        }
        
    } // End of appendNewTask




    // This function uses event delegation to cross out the task if the checkbox is checked
    // Upon checking, current time will appear in Time Completed column
    $("#todo").on("change", ":checkbox", function(){

        // Toggle CSS class that controls line-through effect on text
        $(this).closest("tr").find("td:first").toggleClass("crossout");

        // Get current time and format it per requirement
        let current = new Date();
        let month = current.toLocaleString('default', { month: 'short' });
        let day = current.getDate();
        let year = current.getFullYear();
        let time = new Intl.DateTimeFormat('default',
                                                    {
                                                        hour12: true,
                                                        hour: 'numeric',
                                                        minute: 'numeric'
                                                    }).format(current);

        let currentTimeStamp = month + ' ' + day + ', ' + year + ', ' + time;

        // If the respective row is checked, timestamp will hold formatted time, else it'll be blank                                              
        timestamp = ($(this).closest("tr").find(":checkbox").is(":checked")) ? currentTimeStamp : "";

        // Set timestamp in Time Completed column
        $(this).closest("tr").find("td:eq(1)").html(timestamp);

    }); // End of checkbox checked trigger function
    





    
}); // End of document function
