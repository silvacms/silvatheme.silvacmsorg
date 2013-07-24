(function($) {
    $(document).ready(function(){
        // tab navigation
        $('#tabs section').hide();
        $('#tabs section:first').show();
        $('#tabs ul li:first').addClass('selected');
        $('#tabs ul li a').click(function(){
            $('#tabs ul li').removeClass('selected');
            $(this).parent().addClass('selected');
            var currentAnchor = $(this).attr('href');
            var currentAnchorParts = currentAnchor.split('#');
            var currentTab = currentAnchorParts.slice(-1);
            var currentId = '#' + currentTab;
            $('#tabs section').hide();
            $(currentId).show();
            return false;
        });

        // info box
        $('.info-box p:eq(1)').addClass('infoText');
        $('.info-box p:eq(1)').hide();
        $('.info-box p:eq(0)').click(function() {
            $(this).next('p').slideToggle('slow');
        });

        // sticky panel
        var stickyPanelOptions = {
            topPadding: 40,
            afterDetachCSSClass: 'detached',
            savePanelSpace: true,
            parentSelector: null
        };
        $(".stickypanel").stickyPanel(stickyPanelOptions);

        // masonry
        $('.software-groups').masonry({
            // options
            itemSelector : '.package',
            columnWidth : 330,
            gutterWidth : 30
        });

        // truncate list
        var items = $('ul.truncate-list').children().length;
        var moreLink = $('<li class="show-all button green small"><a href="" title="show all results">Show all ' + items + ' links</a></li>');

        // hiding all list items after the first 5
        $('ul.truncate-list').children('li:gt(4)').hide();

        // adding the 'Show More' link
        if (items > 5) {
            $('ul.truncate-list').append(moreLink);
        }

        // binding a click event to 'Show More'
        moreLink.find('a').on('click', function (){
            // hiding 'Show More' and showing the rest of the list items in this ul
            $(this).parent().hide().siblings('li').show();
            // preventing default action and event bubbling
            return false;
        });

    });
})(jQuery);
