// CHECKBOX

if(document.querySelector("input[name=paid1]")){
    var checkbox1 = document.querySelector("input[name=paid1]").addEventListener('change',checked);
}
if(document.querySelector("input[name=paid2]")){
    var checkbox2 = document.querySelector("input[name=paid2]").addEventListener('change',checked);
}
if(document.querySelector("input[name=paid3]")){
    var checkbox3 = document.querySelector("input[name=paid3]").addEventListener('change',checked);
}
if(document.querySelector("input[name=paid4]")){
    var checkbox4 = document.querySelector("input[name=paid4]").addEventListener('change',checked);
}
if(document.querySelector("input[name=paid5]")){
    var checkbox5 = document.querySelector("input[name=paid5]").addEventListener('change',checked);
}
if(document.querySelector("input[name=paid6]")){
    var checkbox6 = document.querySelector("input[name=paid6]").addEventListener('change',checked);
}
if(document.querySelector("input[name=paid7]")){
    var checkbox7 = document.querySelector("input[name=paid7]").addEventListener('change',checked);
}
if(document.querySelector("input[name=paid8]")){
    var checkbox8 = document.querySelector("input[name=paid8]").addEventListener('change',checked);
}
if(document.querySelector("input[name=paid9]")){
    var checkbox9 = document.querySelector("input[name=paid9]").addEventListener('change',checked);
}
if(document.querySelector("input[name=paid10]")){
    var checkbox10 = document.querySelector("input[name=paid10]").addEventListener('change',checked);
}
if(document.querySelector("input[name=paid11]")){
    var checkbox11 = document.querySelector("input[name=paid11]").addEventListener('change',checked);
}
if(document.querySelector("input[name=paid12]")){
    var checkbox12 = document.querySelector("input[name=paid12]").addEventListener('change',checked);
}
if(document.querySelector("input[name=paid13]")){
    var checkbox13 = document.querySelector("input[name=paid13]").addEventListener('change',checked);
}
if(document.querySelector("input[name=paid14]")){
    var checkbox14 = document.querySelector("input[name=paid14]").addEventListener('change',checked);
}
if(document.querySelector("input[name=paid15]")){
    var checkbox15 = document.querySelector("input[name=paid15]").addEventListener('change',checked);
}

var total = 0;
document.getElementById('paying').innerText = total;

function checked(e) {
    if(this.checked) {
        e.target.parentElement.parentElement.className="alert alert-success";
        total = total + parseInt(e.target.parentElement.previousSibling.previousSibling.innerText);
        document.getElementById('paying').innerText = total;
        
    } else {
        e.target.parentElement.parentElement.className="alert";
        total = total - e.target.parentElement.previousSibling.previousSibling.innerText;
        document.getElementById('paying').innerText = total;
    }
};

// FEE IN RS. INPUT 

if(document.querySelector('#amt-form')){ //CHECK IF THERE IS AN INPUT FOR FEES
    const amtform = document.querySelector('#amt-form');
    amtform.addEventListener('submit',clicked);
}
let res;
const usn = document.getElementById('usn').textContent;// GET USN
    
var xhr = new XMLHttpRequest();// AJAX FOR FEES-DUE FOR USN
xhr.open('GET','/entry/fee/'+usn,true);
xhr.setRequestHeader('X-Requested-With','XMLHttpRequest');
xhr.onload = function(){
        
    if(this.status == 200){
        res =parseInt(JSON.parse(this.responseText),10);// GET DUE
        
    }
}   
xhr.send(); 
function clicked(e) {

        if (document.querySelector("input[name=amt]").value <= 0 || document.querySelector("input[name=amt]").value > res) {      
            e.preventDefault();
            alert('Enter Valid Fees');
            var errorMsgDiv = document.querySelector('#error-msg-div');
            errorMsgDiv.className='alert alert-warning';
            var newErrorMsg = document.createElement('h5');
            var errorText = document.createTextNode('Enter Valid Fees');
            var toInsertBefore = document.querySelector('#toInsertBefore');
            newErrorMsg.appendChild(errorText);
            errorMsgDiv.insertBefore(newErrorMsg,toInsertBefore);
            setTimeout(() => {
                newErrorMsg.remove();
                errorMsgDiv.className='';
            }, 3000);       
    }  
       
};

// SELECT ALL CHECKBOXES 


if(document.getElementById('selectAllCB')){
const CB = document.getElementById('selectAllCB');
CB.addEventListener('change',selectCBAll);
}

if(document.getElementById('selectAll')){
const selectAll = document.getElementById('selectAll');
selectAll.addEventListener('click',selectAllCheckbox);
}

const checkBoxes = document.querySelectorAll("input[type=checkbox]");

function selectCBAll(e){
    if(this.checked){
        total = parseInt(document.getElementById('due').innerText);
        document.getElementById('paying').innerText = total;
        checkBoxes.forEach(element => {
                element.checked=true;
                element.parentElement.parentElement.className="alert alert-success";
        });
        checkBoxes[0].parentElement.parentElement.className="";
    } else {
        total = 0;
        document.getElementById('paying').innerText = total;
        checkBoxes.forEach(element => {
            element.checked=false;
            element.parentElement.parentElement.className="";
    });
    }
}

function selectAllCheckbox(e){
    e.preventDefault();
    if(checkBoxes[0].checked){
        total = 0;
        document.getElementById('paying').innerText = total;
        checkBoxes.forEach(element => {
            element.checked=false;
            element.parentElement.parentElement.className="";
        });
    } else {
        total = parseInt(document.getElementById('due').innerText);
        document.getElementById('paying').innerText = total;
        checkBoxes.forEach(element => {
                element.checked=true;
                element.parentElement.parentElement.className="alert alert-success";
        });
        checkBoxes[0].parentElement.parentElement.className="";
    }
}
