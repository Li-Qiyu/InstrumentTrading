;
var shop_newProduct_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $(".newProduct_wrap .do-newProduct").click(function (){
            var productName = $(".newProduct_wrap input[name=productName]").val();
            var price = $(".newProduct_wrap input[name=price]").val();
            var description = $(".newProduct_wrap input[name=description]").val();
            var images = $(".newProduct_wrap input[name=images]").val();
            if(productName==undefined){
                alert("Please input product name");
                return ;
            }
            if(price==undefined){
                alert("Please input price");
                return ;
            }
            if(description==undefined){
                alert("Please input description");
                return ;
            }
            if(images==undefined){
                alert("Please upload image");
                return ;
            }
        });
    }
};

$(document).ready(function(){
    shop_newProduct_ops.init();
});