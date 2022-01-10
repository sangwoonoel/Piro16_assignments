
const addBtn = document.querySelector(".addBtn");
const delAll = document.querySelector(".delAll");
const delLast = document.querySelector(".delLast");
const delCheck = document.querySelector(".delCheck");


addBtn.addEventListener("click", addPlan);
delAll.addEventListener('click', delAllPlan);
delLast.addEventListener('click', delLastPlan);
delCheck.addEventListener('click', delCheckPlan);


function addPlan() {
    let contents = document.querySelector('.addBar');
    if (!contents.value) {
        alert('내용을 입력해주세요.');
        contents.focus();
        return false;
    }

    let tr = document.createElement('tr');
    let input = document.createElement('input');
    input.setAttribute('type', 'checkbox');
    input.setAttribute('class', 'btn-chk');
    let td01 = document.createElement('td');
    td01.appendChild(input);
    tr.appendChild(td01);
    let td02 = document.createElement('td');
    td02.innerHTML = contents.value;
    tr.appendChild(td02);

    document.getElementById('listBody').appendChild(tr);
    contents.value='';
    contents.focus();

    //const target  = document.querySelector('.listBox');
    //let tr = document.createElement('tr');
    //let addBar = document.querySelector(".addBar").value;
    //let list = document.createElement('h1');
    //list.setAttribute('type', 'checkbox');
    //list.textContent = addBar;
    //target.append(list)
}


//전체 삭제 함수
function delAllPlan() {
    let list = document.getElementById('listBody');
    while(list.firstChild) {
    list.removeChild(list.firstChild);
    }
}

function delLastPlan() {
    let body = document.getElementById('listBody');
    let list = document.querySelectorAll('#listBody > tr');
    if(list.length > 0) {
        let delLen = list.length-1;
        body.removeChild(list[delLen]);
    } 
    else {
        alert('삭제할 항목이 없습니다');
        return false;
    }
}

//체크박스 삭제 함수
function delCheckPlan() {
    let body = document.getElementById('listBody');
    let chkbox = document.querySelectorAll('#listBody .btn-chk');
    
    for(let i in chkbox) {
        if(chkbox[i].checked) {
            body.removeChild(chkbox[i].parentNode.parentNode);
        }
    }
        

}


// list.removeChild(list.lastChild);
    //let addBar = document.querySelector(".addBar").value;
    //if (addBar != null) {
    //    planList.push(addBar);
   
    //showList();
//}

//function showList() {

    //let list = "<p>"
    //for (let i = 0; i <planList.length; i++) {
    //    list += "<input>" + planList[i];
    //}
    //list += "</p>";
    //list.setAttribute('type','checkbox');

    //document.querySelector(".listBox").innerHTML = list;
//}

