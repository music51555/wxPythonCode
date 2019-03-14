var is_show = true
$('.father-menu-item').click(function (event) {
    event.preventDefault()
    if (is_show) {
        $(this).siblings($('.child-menu')).slideUp(500)
        is_show = false
    } else {
        $(this).siblings($('.child-menu')).slideDown(500)
        is_show = true
    }
})
// $('.child-menu').click(function (event) {
//     // event.preventDefault()
//     console.log(1111111)
//     $(this).parent().siblings($('.father-menu')).children('.child-menu').slideUp(500)
//     is_show = false
// })