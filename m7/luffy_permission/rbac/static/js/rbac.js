var is_show = true
$('.father-child').click(function (event) {
    event.preventDefault()
    if (is_show) {
        $(this).next($('.child-menu')).slideUp(500)
        is_show = false
    } else {
        $(this).next($('.child-menu')).slideDown(500)
        is_show = true
    }
})