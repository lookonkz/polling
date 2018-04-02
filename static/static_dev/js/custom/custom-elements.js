(function($) { "use strict";


	//Preloader

	Royal_Preloader.config({
		mode           : 'progress',
		background     : '#ffffff',
		showProgress   : true,
		showPercentage : false
	});


	// /* Scroll Animation */
	//
	// window.scrollReveal = new scrollReveal();


	//Parallax & fade on scroll

	function scrollBanner() {
	  $(document).scroll(function(){
		var scrollPos = $(this).scrollTop();
		$('.parallax-fade-top').css({
		  'top' : (scrollPos/2)+'px',
		  'opacity' : 1-(scrollPos/750)
		});
	  });
	}
	scrollBanner();

	
	
	
	$(document).ready(function() {
	
	
		/* Scroll Too */
	
		$(".scroll").on('click', function(event){

			event.preventDefault();

			var full_url = this.href;
			var parts = full_url.split("#");
			var trgt = parts[1];
			var target_offset = $("#"+trgt).offset();
			var target_top = target_offset.top - 60;

			$('html, body').animate({scrollTop:target_top}, 800);
		});

			
		//Scroll back to top
	
		var offset = 300;
		var duration = 600;
		jQuery(window).on('scroll', function() {
			if (jQuery(this).scrollTop() > offset) {
				jQuery('.scroll-to-top').fadeIn(duration);
			} else {
				jQuery('.scroll-to-top').fadeOut(duration);
			}
		});
				
		jQuery('.scroll-to-top').on('click', function(event) {
			event.preventDefault();
			jQuery('html, body').animate({scrollTop: 0}, duration);
			return false;
		})

			
		// Type text
		
		var typed = new Typed('#typed-1', {
			strings: ['Belgrade', 'New York', 'Athens', 'Berlin', 'Copenhagen', 'Moscow', 'Prague', 'Paris'],
			typeSpeed:45,
			backSpeed:0,
			startDelay:200,
			backDelay:2200,
			loop:true,
			loopCount:false,
			showCursor:true,
			cursorChar:"|",
			attr:null
		});	
		
		var typed2 = new Typed('#typed-2', {
			strings: ['a web developer.', 'a web designer.'],
			typeSpeed:45,
			backSpeed:0,
			startDelay:200,
			backDelay:2200,
			loop:true,
			loopCount:false,
			showCursor:true,
			cursorChar:"_",
			attr:null
		});	
		
		
		// Activate Carousel
		
		$('.carousel').carousel({
			interval: false
		});

		// Activate Tooltip
		
		$(".tipped").tipper();

		
		// Activate bootstrapSwitch
		
		$("[name='my-checkbox']").bootstrapSwitch();
	
	
		// Facts Counter 
	
		$('.counter-numb').counterUp({
			delay: 10,
			time: 1000
		});
		
		
		//Parallax
		
		$('.parallax').parallax("50%", 0.3);		
		
		
		/* Video */
		
		$(".container").fitVids();
						
		$('.vimeo a,.youtube a').on('click', function (e) {
			e.preventDefault();
			var videoLink = $(this).attr('href');
			var classeV = $(this).parent();
			var PlaceV = $(this).parent();
			if ($(this).parent().hasClass('youtube')) {
				$(this).parent().wrapAll('<div class="video-wrapper">');
				$(PlaceV).html('<iframe frameborder="0" height="333" src="' + videoLink + '?autoplay=1&showinfo=0" title="YouTube video player" width="547"></iframe>');
			} else {
				$(this).parent().wrapAll('<div class="video-wrapper">');
				$(PlaceV).html('<iframe src="' + videoLink + '?title=0&amp;byline=0&amp;portrait=0&amp;autoplay=1&amp;color=6dc234" width="500" height="281" frameborder="0"></iframe>');
			}
		});	
		
		





		//add custom buttons for the zoom-in/zoom-out on the map
		function CustomZoomControl(controlDiv, map) {
			//grap the zoom elements from the DOM and insert them in the map 
			var controlUIzoomIn= document.getElementById('cd-zoom-in'),
				controlUIzoomOut= document.getElementById('cd-zoom-out');
			controlDiv.appendChild(controlUIzoomIn);
			controlDiv.appendChild(controlUIzoomOut);

			// Setup the click event listeners and zoom-in or out according to the clicked element
			google.maps.event.addDomListener(controlUIzoomIn, 'click', function() {
				map.setZoom(map.getZoom()+1)
			});
			google.maps.event.addDomListener(controlUIzoomOut, 'click', function() {
				map.setZoom(map.getZoom()-1)
			});
		}

		var zoomControlDiv = document.createElement('div');
		var zoomControl = new CustomZoomControl(zoomControlDiv, map);

		//insert the zoom div on the top left of the map
		map.controls[google.maps.ControlPosition.LEFT_TOP].push(zoomControlDiv);
		
		
	});	

  })(jQuery); 