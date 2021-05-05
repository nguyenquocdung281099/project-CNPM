var form = {
    isvalid: true,
    text : [],
    mail:"",
    phone:"",
    checkEmpty: function(){
        for (const key in this.text) {
            if(this.text[key] == "")
        {
            alert("please fill out form !" ) ;
            this.isvalid =false;
        }
        }
    },
    checkMail : function()
    {
        var pattenMail = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/; 
        if(!pattenMail.test(this.mail)){
            alert("Please enter the correct email");
            this.isvalid =false;
        }
    },
    checkPhone: function(){
        var pattenPhone = /[0-9]{10}/;
        if(!pattenPhone.test(this.phone)){
            alert("Please enter the correct phone");
            this.isvalid =false;
            
        }
    }
}