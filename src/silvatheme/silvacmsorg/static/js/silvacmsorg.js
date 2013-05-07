$(document).ready(function() {

  // toggle bar
  $("#toggleButton").click(function () {
    $("#toggleBar").toggle('slow');
  });

  // truncate list
  var moreLink = $('<li class="show-all"><a href="">Show More</a></li>');

  // hiding all list items after the first 5
  $('ul.truncate-list').children('li:gt(4)').hide();

  // adding the 'Show More' link
  $('ul.truncate-list').append(moreLink);

  // binding a click event to 'Show More'
  moreLink.find('a').on('click', function (){

     // hiding 'Show More' and showing the rest of the list items in this ul
     $(this).parent().hide().siblings('li').show();

     // preventing default action and event bubbling
     return false;
  });

}


