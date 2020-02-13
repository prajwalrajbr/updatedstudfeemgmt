const usn = document.getElementById('id_USN');
usn.addEventListener('keyup',checkUSN);

const admNo = document.getElementById('id_Adm_No');
admNo.addEventListener('keyup',checkAdmNo);

const form = document.querySelector('#stud-form');
form.addEventListener('submit',checkFields);

const pno = document.querySelector('#id_S_Pno');
pno.addEventListener('keyup',checkpno);

const dob = document.querySelector('#id_DOB');
dob.addEventListener('change',checkdob);

let res;
let usn_error=false;
let admNo_error=false;
let pno_error=false;
let dob_error=false;

var xhr = new XMLHttpRequest();// AJAX FOR USN LIST
xhr.open('GET','/entry/create-stud-pd/',true);
xhr.setRequestHeader('X-Requested-With','XMLHttpRequest');
xhr.onload = function(){
        
    if(this.status == 200){
        res =JSON.parse(this.responseText);// GET USN
    }
}
xhr.send();

let usnErrorExist=false;
let admNoErrorExists=false;

function checkUSN(e){
    if(e.target.value.length == 10){
        for(var i=0;i< res[0].length;i++){             
            if(e.target.value == res[0][i]){
                usn_error = true;
                usnErrorExist=false;
                if(!usnErrorExist){
                    if(document.querySelector('#error-msg-char')){
                        var deleteErrorMsg = document.querySelector('#error-msg-char');
                        deleteErrorMsg.remove();
                    }
                    if(document.querySelector('#error-msg')){
                        var deleteErrorMsg = document.querySelector('#error-msg');
                        deleteErrorMsg.remove();
                        usnErrorExist=false;                   
                    }
                    var usnError = document.querySelector('#stud-form');
                    var newErrorMsg = document.createElement('p');
                    newErrorMsg.className = 'alert alert-danger';
                    newErrorMsg.id = 'error-msg';
                    var errorText = document.createTextNode('USN already exists !!!');
                    var toInsertBefore = document.querySelector('#id_Gender').previousElementSibling;
                    newErrorMsg.appendChild(errorText);
                    usnError.insertBefore(newErrorMsg,toInsertBefore);
                    usnErrorExist=true;
                    break;
                } 
            } else {
                usn_error = false;
                if(document.querySelector('#error-msg-char')){
                    var deleteErrorMsg = document.querySelector('#error-msg-char');
                    deleteErrorMsg.remove();
                }
                if(document.querySelector('#error-msg')){
                    var deleteErrorMsg = document.querySelector('#error-msg');
                    deleteErrorMsg.remove();
                    usnErrorExist=false;                   
                }
            }
        }
    } else {
        usn_error = true;
        if(document.querySelector('#error-msg-char')){
        } else {
            if(document.querySelector('#error-msg')){
                var deleteErrorMsg = document.querySelector('#error-msg');
                deleteErrorMsg.remove();
                usnErrorExist=false;                   
            }
            var usnError = document.querySelector('#stud-form');
            var newErrorMsg = document.createElement('p');
            newErrorMsg.className = 'alert alert-danger';
            newErrorMsg.id = 'error-msg-char';
            var errorText = document.createTextNode('USN must be 10 characters !!!');
            var toInsertBefore = document.querySelector('#id_Gender').previousElementSibling;
            newErrorMsg.appendChild(errorText);
            usnError.insertBefore(newErrorMsg,toInsertBefore);
        }
    }
};

function checkAdmNo(e){
    for(var i=0;i< res[1].length;i++){             
        if(e.target.value == res[1][i]){
            admNo_error=true;
            admNoErrorExists=false;
            if(!admNoErrorExists){
                if(document.querySelector('#error-msg2')){
                    var deleteErrorMsg = document.querySelector('#error-msg2');
                    deleteErrorMsg.remove();
                    admNoErrorExists=false;                   
                }
                var usnError = document.querySelector('#stud-form');
                var newErrorMsg = document.createElement('p');
                newErrorMsg.className = 'alert alert-danger';
                newErrorMsg.id = 'error-msg2';
                var errorText = document.createTextNode('Admission Number already exists !!!');
                var toInsertBefore = document.querySelector('#id_Course').previousElementSibling;
                newErrorMsg.appendChild(errorText);
                usnError.insertBefore(newErrorMsg,toInsertBefore);
                admNoErrorExists=true;
                break;
            } 
        } else {
            admNo_error=false;
            if(document.querySelector('#error-msg2')){
                var deleteErrorMsg = document.querySelector('#error-msg2');
                deleteErrorMsg.remove();
                admNoErrorExists=false;                   
            }
        }
    }
};

function checkFields(e){
    if(usn_error == true || admNo_error == true || pno_error == true || dob_error == true){
        e.preventDefault();
        alert('Check the fields correctly !!!');
    }
};

function checkpno(e){
    if(e.target.value.length == 10){
            if(document.querySelector('#error-msg-pno')){
                var deleteErrorMsg = document.querySelector('#error-msg-pno');
                deleteErrorMsg.remove();                 
            }
            let k=0;
            for(let i=0;i<10;i++){   
                if(parseInt(e.target.value[i])||parseInt(e.target.value[i])==0){
                } else {
                    k++;
                }
            }
            if(k==0){  
                pno_error=false; 
                if(document.querySelector('#error-msg-pno-char')){
                    var deleteErrorMsg = document.querySelector('#error-msg-pno-char');
                    deleteErrorMsg.remove();          
                }
            } else {
                if(document.querySelector('#error-msg-pno-char')){
                    var deleteErrorMsg = document.querySelector('#error-msg-pno-char');
                    deleteErrorMsg.remove();             
                }
                var pnoError = document.querySelector('#stud-form');
                var newErrorMsg = document.createElement('p');
                newErrorMsg.className = 'alert alert-danger';
                newErrorMsg.id = 'error-msg-pno-char';
                var errorText = document.createTextNode('Phone Number must contain only Numbers !!!');
                var toInsertBefore = document.getElementsByTagName('textarea')[0].previousElementSibling;
                newErrorMsg.appendChild(errorText);
                pnoError.insertBefore(newErrorMsg,toInsertBefore); 
                pno_error=true;      
            }
    } else {
                if(document.querySelector('#error-msg-pno-char')){
                    var deleteErrorMsg = document.querySelector('#error-msg-pno-char');
                    deleteErrorMsg.remove();             
                }
                if(document.querySelector('#error-msg-pno')){              
                } else {
                    var pnoError = document.querySelector('#stud-form');
                    var newErrorMsg = document.createElement('p');
                    newErrorMsg.className = 'alert alert-danger';
                    newErrorMsg.id = 'error-msg-pno';
                    var errorText = document.createTextNode('Phone Number must be 10 digits !!!');
                    var toInsertBefore = document.getElementsByTagName('textarea')[0].previousElementSibling;
                    newErrorMsg.appendChild(errorText);
                    pnoError.insertBefore(newErrorMsg,toInsertBefore);
                }  
                pno_error=true;    
    }
}

function checkdob(e){
    if(e.target.value !=''){
        if(parseInt(e.target.value)<=(document.querySelector('#id_Adm_Year').value)-15 && parseInt(e.target.value)>=(document.querySelector('#id_Adm_Year').value)-25){
            dob_error=false;

            if(document.querySelector('#error-msg-dob')){
                var deleteErrorMsg = document.querySelector('#error-msg-dob');
                deleteErrorMsg.remove();             
            }


        } else {
            dob_error=true;

            if(document.querySelector('#error-msg-dob')){
                var deleteErrorMsg = document.querySelector('#error-msg-dob');
                deleteErrorMsg.remove();             
            }

            var dobError = document.querySelector('#stud-form');
            var newErrorMsg = document.createElement('p');
            newErrorMsg.className = 'alert alert-danger';
            newErrorMsg.id = 'error-msg-dob';
            var errorText = document.createTextNode('Enter the Date Of Birth correctly !!!');
            var toInsertBefore = document.getElementById('id_POB').previousElementSibling;
            newErrorMsg.appendChild(errorText);
            dobError.insertBefore(newErrorMsg,toInsertBefore);

        }
    }
}