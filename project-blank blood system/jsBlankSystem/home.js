var $ = function(id){
    return document.getElementById(id);
}


//

var validateForm= function(){
    form.text[0] = $("fullname").value;
    form.text[1] = $("Email").value;
    form.text[2] = $("phone").value;
    form.text[3] = $("your-message").value;
    form.mail= form.text[1];
    form.phone =form.text[2];
    form.checkEmpty();
    form.checkMail();
    form.checkPhone();
    if(form.isvalid){
        $("contact-form").submit();
    }
}
var handleButtonDonateLink = function(){
    var className = "donate open";
    $("donate").setAttribute("class",className);
}
var handleButtonDonateBtn = function(){
    var className = "donate close";
    $("donate").setAttribute("class",className);
}
window.onload= function(){
    $("send").onclick = validateForm;
    $("link-donate").onclick = handleButtonDonateLink;
    $("time-close").onclick = handleButtonDonateBtn;
}