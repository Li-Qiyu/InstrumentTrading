;
var member_reg_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $(".reg_wrap .do-reg").click(function (){
            var username = $(".reg_wrap input[name=username]").val();
            var password = $(".reg_wrap input[name=password]").val();
            var password2 = $(".reg_wrap input[name=password2]").val();
            if(username==undefined || username.length<1){
                alert("Please input correct username");
                return ;
            }
            if(password==undefined || password.length<6){
                alert("Please input correct password (at least 6 characters)");
                return ;
            }
            if(password2==undefined || password2!==password){
                alert("The check password is not the same");
                return ;
            }
        });
    }
};

$(document).ready(function(){
    member_reg_ops.init();
});