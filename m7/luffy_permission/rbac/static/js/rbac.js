$('.father-menu-item').click(function (event) {
    event.preventDefault()
    $(this).siblings($('.child-menu')).toggleClass('show')
    $(this).siblings($('.child-menu')).toggleClass('hide')
})


$('.child-menu-item').click(function (event) {
    event.stopPropagation()
})


// //实现的点击右侧内容区域的按钮后，左侧菜单栏的选中样式不会丢失
// $('.right-body a').click(function (event) {
//     event.preventDefault()
//     console.log($('.selected').attr('class'))
//     $('.selected').attr('class','child-menu-item selected')
// })