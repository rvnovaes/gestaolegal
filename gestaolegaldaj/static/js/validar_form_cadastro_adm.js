"use strict";

function TestaCPF(strCPF) {
    var Soma;
    var Resto;
    Soma = 0;
  if (strCPF === "00000000000") return false;
     
  for (i=1; i<=9; i++) Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (11 - i);
  Resto = (Soma * 10) % 11;
   
    if ((Resto === 10) || (Resto == 11))  Resto = 0;
    if (Resto != parseInt(strCPF.substring(9, 10)) ) return false;
   
  Soma = 0;
    for (i = 1; i <= 10; i++) Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (12 - i);
    Resto = (Soma * 10) % 11;
   
    if ((Resto === 10) || (Resto === 11))  Resto = 0;
    if (Resto != parseInt(strCPF.substring(10, 11) ) ) return false;
    return true;
}

function validar() {

  var elemento_selecionado = document.getElementById('val-bolsista');
  var string_selecionada = elemento_selecionado.options[elemento_selecionado.selectedIndex].text;

  if(string_selecionada === 'Sim'){
      document.getElementById("tipo_bolsa").hidden = false;
      document.getElementById("inicio").hidden = false;
      document.getElementById("fim").hidden = false;
  }
  else{
 
   //document.getElementById("val-tipoBolsa").disabled = true;
   document.getElementById("tipo_bolsa").hidden = true;
   document.getElementById("inicio").hidden = true;
   document.getElementById("fim").hidden = true;
  }
  
}

function validatedate(inputText)
{
var dateformat = /^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$/;
// Match the date format through regular expression
if(inputText.value.match(dateformat))
{
document.form1.text1.focus();
//Test which seperator is used '/' or '-'
var opera1 = inputText.value.split('/');
var opera2 = inputText.value.split('-');
lopera1 = opera1.length;
lopera2 = opera2.length;
// Extract the string into month, date and year
if (lopera1>1)
{
var pdate = inputText.value.split('/');
}
else if (lopera2>1)
{
var pdate = inputText.value.split('-');
}
var dd = parseInt(pdate[0]);
var mm  = parseInt(pdate[1]);
var yy = parseInt(pdate[2]);
// Create list of days of a month [assume there is no leap year by default]
var ListofDays = [31,28,31,30,31,30,31,31,30,31,30,31];
if (mm===1 || mm>2)
{
if (dd>ListofDays[mm-1])
{
alert('Invalid date format!');
return false;
}
}
if (mm===2)
{
var lyear = false;
if ( (!(yy % 4) && yy % 100) || !(yy % 400)) 
{
lyear = true;
}
if ((lyear===false) && (dd>=29))
{
alert('Invalid date format!');
return false;
}
if ((lyear===true) && (dd>29))
{
alert('Invalid date format!');
return false;
}
}
}
else
{
alert("Invalid date format!");
document.form1.text1.focus();
return false;
}
}
