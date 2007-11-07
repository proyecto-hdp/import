function seleccionarFila(fila, id){
var objeto = document.getElementById(id);          
    if(objeto.className=="seleccionada"){
        objeto.style.backgroundColor="white";
        objeto.className="deseleccionada";
    }
    else{
        objeto.style.backgroundColor="#2980b9";
        objeto.className="seleccionada";
        var t = document.getElementById('chk'+id).checked=true;
    }
}

/*function probar(f){//probando seleccion de checkboxes y radiobuttons
    var chks = document.getElementsByName("chk_tab");
    var r =document.getElementsByName("radio");
    for(var i = 0; i<chks.length; i++){
        if(chks[i].checked){
            alert("elemento: "+chks[i].value +"\n seleccionado: "+chks[i].checked);
        }
    }
    for(var i=0; i<r.length;i++){
        if(r[i].checked){
            alert("elemento: "+r[i].value +"\n seleccionado: "+r[i].checked);
        }
    }
}*/