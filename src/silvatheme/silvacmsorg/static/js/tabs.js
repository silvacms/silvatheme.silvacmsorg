
(function($) {
    $(document).ready(function(){
        $('.tabs ul li a').click(function(){
            var $link = $(this);
            var tab = $link.attr('href');
            $('.tabs ul li').removeClass('selected');
            $link.parent().addClass('selected');
            $('.tabs section').removeClass('selected');
            $(tab).addClass('selected');
            return false;
        });
    });
})(jQuery);
