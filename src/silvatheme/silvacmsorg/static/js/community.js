 $(document).ready(function() {
    	    
      $("#tabNav div.tab").hide(); 
	      $("#tabs li:first").attr("id","current");
	      $("#tabNav div:first").fadeIn(); 
    
      $('#tabs a').click(function(e) {
        e.preventDefault();        
        $("#tabNav div.tab").hide(); 
        $("#tabs li").attr("id",""); 
        $(this).parent().attr("id","current"); 
        $('#' + $(this).attr('title')).fadeIn();
    });
    
      $(".infoText").hide();
      $(".infoButton").click(function()
      {
        $(this).next(".infoText").slideToggle('slow');
      });
    });
    
      $("#toggleButton").click(function () {
      $("#toggleBar").toggle('slow');
    });
    
      $("#dark").click( function(){ $
		  ("body").removeClass('bg2').addClass("bg1");

	  });

	    $("#light").click( function(){ $
		  ("body").removeClass("bg1").addClass("bg2");
	  });

	    $("#light").click( function(){ $
		  ("#community #tabs li a").addClass("tabsLight")
	  });
	  $("#dark").click( function(){ $
		  ("#community #tabs li a").removeClass("tabsLight")
	  });
	    
	    
    });  
