$('.father-menu').click(function (event) {
    event.preventDefault()
    console.log($(this).find('div'))
    $(this).find($('.child-menu')).toggleClass('hide')
})


$('.child-menu-item').click(function (event) {
    event.stopPropagation()
})