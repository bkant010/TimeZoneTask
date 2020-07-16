function validateForm() {
debugger;
var x = document.MyForm["start_day"].value;
  var y = document.MyForm["end_day"].value;
  if ((x != "" && y == "")||(x == "" && y != "")){
    alert("Fill Both or Skip Both");
    return false;
  }
}