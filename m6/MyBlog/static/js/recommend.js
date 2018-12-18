$(function(){
    $('#div_digg div').click(function(){
        $.ajax({
            url:"",
            type: "post",
            data: {
                "article_title":$('.title a').text(),
                'tag': $(this).attr('class'),
                'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
            },
            success: function(data){
                var current_num = $('.'+data.tag).children()[0].innerText
                if(data.msg == '推荐成功' || data.msg == '反对成功'){
                    $('.'+data.tag).children()[0].innerText = parseInt(current_num + 1)
                }
                $('#digg_tips').text(data.msg);
            }
        })
    })


})
