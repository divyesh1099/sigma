$(function () {
    $(window).on('scroll', function () {
        if ( $(window).scrollTop() > 10 ) {
            $('.navbar').addClass('active');
        } else {
            $('.navbar').removeClass('active');
        }
    });
});

$(function () {
    var startDate = new Date('1985-01-01'),
        endDate = new Date('2021-01-01');
    $('#from-datepicker').datetimepicker({
        //other option
        startDate: startDate, //set start date
        endDate: endDate //set end date
    });
});