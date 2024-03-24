// Create a new div element
var newDivb1 = document.createElement('div');
var newDivb = document.createElement('div');
var newDiv1 = document.createElement('div');
var newDiv = document.createElement('div');

// Add class name to the new div
newDiv.classList.add('flex-container');

// Create a label element
var label = document.createElement('label');
label.textContent = 'ادخل الباركود'; // Set label text

// Create an input element
var labelb = document.createElement('label');
labelb.textContent = 'الدفع كلي'

var button = document.createElement('input');
button.setAttribute('type', 'button');
button.setAttribute('value', 'الدقع الكلي'); // Set default value if needed

var inputField = document.createElement('input');
inputField.setAttribute('id', 'read_barcode');
inputField.setAttribute('type', 'number');
inputField.setAttribute('value', '0'); // Set default value if needed

// Append label and input field to the new div
newDivb.appendChild(labelb);
newDivb.appendChild(button);
newDivb1.appendChild(newDivb);

newDiv.appendChild(label);
newDiv.appendChild(inputField);
newDiv1.appendChild(newDiv)
// Find the parent element where you want to append the new div
var parentElement = document.querySelector("#receipt_form > div > fieldset ");
newDiv1.className="form-row field-total_price"
newDivb1.className="form-row field-total_price"
// Append the new div to the parent element
parentElement.appendChild(newDiv1);
parentElement.insertBefore(newDivb1,parentElement.firstChild)
button.addEventListener('click',function(){
    document.querySelector("#id_Paid").value=Number(document.querySelector(".readonly").textContent)
})
// Focus on the input field
inputField.focus();
inputField.addEventListener('input', function(event) {
    // Log the input value to the console
    
    if (event.target.value.trim() !== '') {
        // Call get_item only if the input value is not empty
        get_item(event.target.value);
    } else {
        // Handle the case where the input value is empty
        // You can add additional handling here if needed
    }});
function get_item(id)
{

    var result;
    $.ajax({
                type: 'GET',
                url: '/get_item/' + String(id) + '/',
                success: function(response){
                    const it = response.item
                    var  t = document.querySelectorAll('table')[3]
                    var rows = t.querySelectorAll('tbody tr')
                    var that = rows[rows.length-3]
                    rows[rows.length-1].querySelector('a').click()
                    document.getElementById('read_barcode').value=''


                    that.querySelector('.field-item_pk p').textContent=it.id
                    that.querySelector('.field-quantity input').value=it.quantity
                    that.querySelector('.field-selling_price input').value=it.selling_price
                    selectElement=that.querySelector('.field-item select');

                    for (var i = 0; i < selectElement.options.length; i++) {
                        var option = selectElement.options[i];
                        
                        // Check if the option's value matches the selected item value
                        if (option.value ==it.id) {
                            // Set the option as selected
                            option.selected = true;
                            
                            // Exit the loop since the item has been found
                            break;
                        }
                    }
                    calculation()

                    set_calculation()
                },
                error: function(xhr, errmsg, err){
                    console.log('erroe');
                }
            });
    
}




function createPrintButton() {
    if (window.location.href.includes('change')) {
        // Create a new submit button element
        var printButton = document.createElement('input');
        printButton.setAttribute('type', 'button');
        printButton.setAttribute('value', 'الطباعة');
        printButton.setAttribute('id', 'print');

        // Add event listener to the print button
        // (You can add your event listener code here)

        // Add the button to the .submit-row div
        var submitRow = document.querySelector('.submit-row');
        
        // Append the printButton as the first child of submitRow
        submitRow.insertBefore(printButton, submitRow.firstChild);
        printButton.addEventListener('click', function() {
            window.location.href = '/receipt/'+document.querySelector("#content > h2").textContent+'/';
        });
        // Remove all event listeners from the print button

    } else {
        // Do nothing or handle other cases
        console.log('Current URL does not contain the word "change".');
    }
}



// Call the function to create the print button
createPrintButton();


function calculation(){
    var table = document.querySelectorAll('table')[3];
    try
    {
        var total=0
        var i=0
        while(true)
            {
                var p =document.querySelector(`#id_sells_set-${i}-selling_price`)
                
                var quantity=document.querySelector(`#id_sells_set-${i}-quantity`)
                total+=Number(p.value)*Number(quantity.value);
                i++;
            }
    }
    catch
    {
        
    }
    document.querySelector('.form-row.field-total_price .readonly').textContent=total
    }
    function set_calculation(){
    var table = document.querySelectorAll('table')[3];
    try
    {
    var i=0;
        while(true)
            {
                var p =document.querySelector(`#id_sells_set-${i}-selling_price`)
                p.addEventListener('input',calculation)
                var q=document.querySelector(`#id_sells_set-${i}-quantity`)
                    q.addEventListener('input',calculation)
                i++;
    
            }
    }
    catch
    {
        
    }
    }
    


    set_calculation()
    calculation()
    document.addEventListener("DOMContentLoaded", function() {
        // This function will be executed after the page has fullyf loaded
        // Define your calculations here
        
        // First setTimeout executes after 1 second
        setTimeout(calculation, 1000);
    
        // Second setTimeout executes after 2 seconds
        setTimeout(set_calculation, 2000);
    });
    var a =document.querySelector('tr.add-row > td > a')
        a.document.addEventListener('click',set_calculation)
        console.log(11111111111111111111111111111111111111111)