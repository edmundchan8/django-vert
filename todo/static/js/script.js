// Wait for dom content to load before calling javascript
document.addEventListener('DOMContentLoaded', function(){

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Select all elements with class 'completed-btn'
    const completedCheckbox = document.querySelectorAll('.completed-check');

    // Loop through each button and add a click event listener
    completedCheckbox.forEach(checkbox => {
      checkbox.addEventListener('click', handleClick);
    });

    function handleClick(event){

        var data = `id=${this.value}`

        // AJAX request
        const xhr = new XMLHttpRequest();

        xhr.open('POST', 'complete_task/')

        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        const csrftoken = getCookie('csrftoken');
        xhr.setRequestHeader('X-CSRFToken', csrftoken);

        xhr.onload = function(){
            if (xhr.status === 200) {
                callback(xhr.responseText);
            } else {
                console.log('AJAX request failed: ', xhr.statusText);
            }
        }

        xhr.send(data);
    }


});