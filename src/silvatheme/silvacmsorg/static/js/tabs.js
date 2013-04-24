(function($) {
    $(document).ready(function(){
        $('.tabs ul li a').click(function(){
            var $link = $(this);
            var anchor = $link.val().split('#');
            var tab = '#' + anchor.slice(-1);
            $('.tabs ul li').removeClass('selected');
            $link.parent().addClass('selected');
            $('.tabs section').removeClass('selected');
            $(tab).addClass('selected');
            return false;
        });
    });
})(jQuery);
