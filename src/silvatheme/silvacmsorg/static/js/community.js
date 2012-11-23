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
	  
	  $('.menu').stickyfloat();
			$('.menu2').stickyfloat('update',{ duration : 0 });
			
			// after page refresh, make sure the values are returned to their defaults
			$('.menu :text').each(function(){
				$(this).val(this.defaultValue);
			});
			
			$('.menu :checkbox').on('change', function(){
				var elem = $(this).parents('.menu'),
					prop = this.className,
					options = {};
	
				options[prop] = this.checked ? true : false;
				elem.stickyfloat('update', options);
			});

			$('.menu .cssTransition:checkbox').on('change', function(){
				var elem = $(this).parents('.menu'),
					val = this.checked ? 0 : elem.find('.duration').val();
				
				elem.toggleClass('transition200');
				elem.stickyfloat('update',{cssTransition: this.checked});
			});
			
			$('.menu :checkbox').each(function(){
				$(this).prop('checked', this.defaultChecked);
			});

	    
	    
    });  
