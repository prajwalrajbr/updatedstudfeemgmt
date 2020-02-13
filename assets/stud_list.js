
// SORT 

let sort=document.getElementById('id_sort')
sort.addEventListener('change',sorting);

function sorting(e){
    if(e.target.value=='noDue'){
        let sd= document.querySelectorAll('#sdetails');
        
        for (let i=0;i<sd.length;i++){
            sd[i].setAttribute("style","");
        }

        for (let i=0;i<sd.length;i++){
            if(sd[i].childNodes[7].innerText==0){
            } else {
                sd[i].setAttribute("style","display:none");
            }
        }
        count();
    } else if (e.target.value=='paid75'){
        let sd= document.querySelectorAll('#sdetails');
        
        for (let i=0;i<sd.length;i++){
            sd[i].setAttribute("style","");
        }

        for (let i=0;i<sd.length;i++){
            let total=sd[i].childNodes[5].innerText;
            total=total/100*75;
            total = sd[i].childNodes[5].innerText - total;
            if(sd[i].childNodes[7].innerText<=total){
            } else {
                sd[i].setAttribute("style","display:none");
            }
        }
        count();
    } else if (e.target.value=='plt75'){
        let sd= document.querySelectorAll('#sdetails');
        
        for (let i=0;i<sd.length;i++){
            sd[i].setAttribute("style","");
        }

        for (let i=0;i<sd.length;i++){
            let total=sd[i].childNodes[5].innerText;
            total=total/100*75;
            total = sd[i].childNodes[5].innerText - total;
            if(sd[i].childNodes[7].innerText>total){
            } else {
                sd[i].setAttribute("style","display:none");
            }
        }
        count();
    } else {
        let sd= document.querySelectorAll('#sdetails');
        
        for (let i=0;i<sd.length;i++){
            sd[i].setAttribute("style","");
        }
        count();
    }
}

// STUDENT COUNT AFTER SORT

function count(){
    let count=0;
    const sdetails = document.querySelectorAll('#sdetails');
    for(let s=0;s<sdetails.length;s++){
        if(sdetails[s].style[0]=='display'){
            count++;
        }
    }
    count = sdetails.length - count ;
    document.getElementById('stotal').textContent = 'Total no. of students is : '+count;
}

// TOTAL NO OF STUDENTS

const sdetails = document.querySelectorAll('#sdetails');
document.getElementById('stotal').textContent = 'Total no. of students is : '+sdetails.length;


