var $ = function(id){
    return document.getElementById(id)
}
var handlButton = function(){
     $("sign-up").nextElementSibling.setAttribute("id","box");
    $("sign-up").setAttribute("class","clear")
}
window.onload= function(){
    $("sign-up").onclick = handlButton;

}