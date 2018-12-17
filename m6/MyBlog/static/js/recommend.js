$(function(){
    $('#div_digg div').click(function(){
        $.ajax({
            url:"",
            type: "post",
            data: {
                "article_title":$('.title a').text(),
                //如果在block标签中添加js代码，那么可以在ajax的data中使用{{ }}模板标签，但要使用双引号括起来
                "article_id":'{{ artile_obj.title }}',
                //tag值，可以使用jquery提供的hasClass方法，如$(this).hasClass('diggit')来判断用户点击的是点赞还是踩灭，结果是True或False，在视图函数反序列化后，存入is_up列，不用手写True或False了
                'tag': $(this).attr('class'),
                'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
            },
            success: function(data){
                if(data.msg == '推荐成功' || data.msg == '反对成功'){
                    $('#digg_tips').text(data.msg);
                    console.log($('.'+data.tag).children()[0])
                    $('.'+data.tag).children()[0].innerText = parseInt($('.'+data.tag).children()[0].innerText + 1)
                }else{
                    $('#digg_tips').text(data.msg)
                }
            }
        })
    })
})
