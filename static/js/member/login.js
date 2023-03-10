;
var member_login_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        $(".login_wrap .do-login").click(function () {
            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("Processing");
                return;
            }
            var login_name = $(".login_wrap input[name=login_name]").val();
            var login_pwd = $(".login_wrap input[name=login_pwd]").val();
            if( login_name == undefined || login_name.length < 1 ){
                alert("Please input correct username");
                return;
            }

            if( login_pwd == undefined || login_pwd.length < 6 ){
                alert("Please input correct password");
                return;
            }

            btn_target.addClass("disabled");
            $.ajax({
                url: common_ops.buildUrl("/member/login"),
                type: "POST",
                data: {
                    login_name: login_name,
                    login_pwd: login_pwd
                },
                dataType: "json",
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (res.code == 200) {
                        callback = function () {
                            window.location.href = common_ops.buildUrl("/");
                        };
                    }
                    common_ops.alert(res.msg, callback);
                }
            });
        });
    }
};

$(document).ready(function () {
    member_login_ops.init();
});