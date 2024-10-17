    function convertStringToDate(inputString) { //STRING TO DATE FUNCTION
        var parts = inputString.split(' | ');
        var dateParts = parts[0].split('-');
        var timeParts = parts[1].split(':');
        var months = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.'];
        var month = months[parseInt(dateParts[0], 10) - 1];
        var day = parseInt(dateParts[1], 10);
        var year = parseInt(dateParts[2], 10);
        var hour = parseInt(timeParts[0], 10);
        var minute = parseInt(timeParts[1], 10);
        var period = hour >= 12 ? 'pm' : 'am';
        if (hour > 12) {
            hour = hour - 12;
        }
        return `${month} ${day}, ${year}, ${hour}:${minute.toString().padStart(2, '0')} ${period}`;
    }
    var bookingDate = document.getElementById("booking-date")
    bookingDate.innerHTML = convertStringToDate(bookingDate.innerHTML)

    function submitForm(status){
        if(status === "Rejected"){
            document.getElementById("booking-status").value = status
            document.getElementById("action-form").submit()
        }
        document.getElementById("booking-status").value = status
    }
    
