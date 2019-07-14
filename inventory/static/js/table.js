
var roomNos=["519", "430", "426", "404", "404", "404", "404"];
var idNos=["2016AAPS204U", "2016A7PS085U", "2016A4PS148U", "2016A4PS240U", "2016A7PS075U", "2016AAPS330U", "2016A7PS310U"];
var sl=1;

var roomNo= [];
var idNo= [];
$.get("http://172.16.100.8:5000/{{table}}", function(data){
    console.log(data);

    insertData(data);});
console.log(roomNo.length);

$("#generate").on("click",function(){
    window.location.assign("http://172.16.100.8:5000/generateCSV.csv")
});

$("#passOut").on("click",function(){
    window.open("http://172.16.100.8:5000/passOut")
});
$("#insertExcel").on("click",function(){
    window.open("http://172.16.100.8:5000/insertExcel")
});

function filterSelection(i){
    var td1;
    var w = document.getElementById("customRadioInline1");
    var x = document.getElementById("customRadioInline2");
    var y = document.getElementById("customRadioInline3");
    var z = document.getElementById("customRadioInline4");

    var table = document.getElementById("t01");
    var tr = table.getElementsByTagName("tr");
    if (w.checked){
        td1 = tr[i].getElementsByTagName("td")[1];
    }

    else if(x.checked){
        td1 = tr[i].getElementsByTagName("td")[2];
    }

    else if(y.checked){
        td1 = tr[i].getElementsByTagName("td")[3];
    }

    else if(z.checked){
        td1 = tr[i].getElementsByTagName("td")[5];
    }
    
    return td1;
}

function myFunction(){
    var td;
    var input = document.getElementById("myInput");
    var filter = input.value.toUpperCase();
    var table = document.getElementById("t01");
    var tr = table.getElementsByTagName("tr");
    for (var i = 0; i < tr.length; i++) {
        td = filterSelection(i);
        if (td) {
          if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
          } else {
            tr[i].style.display = "none";
          }
        } 
      }
}

function insertData(data){

    for (var i=0; i<data[1].length;i++){
    var Sname = data[1][i];
    var SroomNo = data[2][i];
    var SidNo=data[0][i];
    var Sblock=data[3][i];

    $(".tbodyL").append("<tr class=\"table-secondary\" scope=\"row\"><td>"+sl+"</td><td>"+SroomNo+"</td><td>"+Sblock+"</td><td>"+Sname+"</td><td>123456789</td><td>"+SidNo+"</td></tr>");
    sl=sl+1;
}

$('#t01').find('tr').click( function(){
  var row = $(this).find('td:nth-child(6)').text();
  alert('You clicked ' + row);

    $.get("http://172.16.100.8:5000/getInfo",{name:row}, function(data){
        console.log(data);
        window.location.assign("http://172.16.100.8:5000/nextInfo");
        }
        );
});

}
