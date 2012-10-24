 $(document).ready(function() {
    
	  /* Binding a click event handler to the links: */
	    $('li.droppable a').click(function(e){
	 
	        /* Finding the drop down list that corresponds to the current section: */
	        var dropDown = $(this).parent().next();
	 
	        /* Closing all other drop down sections, except the current one */
	        $('.dropdown').not(dropDown).slideUp('slow');
	        dropDown.slideToggle('slow');
	 
	        /* Preventing the default event (which would be to navigate the browser to the link's address) */
	        e.preventDefault();
	    })
	    
      $("#tabNav div.tab").hide(); // Initially hide all content
	      $("#tabs li:first").attr("id","current"); // Activate first tab
	      $("#tabNav div:first").fadeIn(); // Show first tab content
    
      $('#tabs a').click(function(e) {
        e.preventDefault();        
        $("#tabNav div.tab").hide(); //Hide all content
        $("#tabs li").attr("id",""); //Reset id's
        $(this).parent().attr("id","current"); // Activate this
        $('#' + $(this).attr('title')).fadeIn(); // Show content for current tab
    });
	    
	    
    });  
