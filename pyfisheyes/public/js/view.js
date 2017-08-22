var pweek = ""
		$("document").ready(function(){
			if (ck == '1')
				$("[name='pweekday']").attr("checked","checked");
			else
				$("[name='pweekday']").removeAttr("checked");
			$("[name='item']").removeAttr("checked");
			//Default Action
			//alert($.cookie("set_default_day"));
			$(".tab_content").hide(); //Hide all content
			$("ul.tabs li:first").addClass("active").show(); //Activate first tab
			$(".tab_content:first").show(); //Show first tab content
			
			$( "#dialog" ).dialog({
	 			autoOpen: false,
	 			show: "blind",
	 			hide: "explode"
	 		});
			
			//On Click Event
			$("ul.tabs li").click(function() {
				$("ul.tabs li").removeClass("active"); //Remove any "active" class
				$(this).addClass("active"); //Add "active" class to selected tab
				$(".tab_content").hide(); //Hide all tab content
				var activeTab = $(this).find("a").attr("href"); //Find the rel attribute value to identify the active tab + content
				$(activeTab).fadeIn(); //Fade in the active content
				return false;
			});

			
			$( "#datepicker" ).datepicker({ 
				dateFormat: 'yy-mm-dd',
				onSelect: function(dateText, inst) { 
					date=dateText;
					refresh_page();	
		   		},
			   defaultDate:date	
			  });				
				
		
				$( "#datepicker2" ).datepicker({ dateFormat: 'yy-mm-dd',
					   onSelect: function(dateText, inst) { 
							date2=dateText;
							//refresh_page();
							//$.cookie("set_default_day", null);
							location.href = "/view/data/"+tid+"?d2="+date2;
							
				   		 },
					   defaultDate:date2					   
				 });				
		
		    // function of loading image
		    function LoadImage(imgsrc, alink)
		    {  
                // current obj
                var curr = $("#portfolio_0");
                curr.html("<img src='/load2.gif' alt='loading...' />");
                curr.attr('class','loading');
                //alert('finished');
                // new image object
                var img = new Image();
                // image onload
                $(img).load(function () {
                    $(this).css('display','none'); // since .hide() failed in safari
                    //$(curr).removeClass('loading').append(this);
                    if (pagename == "realtime"){
                    	$(curr).removeClass('loading').html("<a class='largeimg' href='"+alink+"'><img src='"+$(this).attr('src')+"'> </a>");
                    }
                    else{
                    	$(curr).removeClass('loading').html(this);
                    }
                    $(this).fadeIn('slow',function(){
                            // once the current loaded, trigger the next image
                            //alert('finished');
                        });
                }).error(function () {
                    // on error remove current
                    $(curr).remove();
                    // trigger the next image
                }).attr('src', imgsrc);
		    }
		    //function changeImage(imgsrc, alink){
		    	//$("#imglink").attr("href",alink);
		    	//$("#img").attr("src",imgsrc);
		    	
		   // }
			function refresh_page () {
				//var rndnum = Math.floor(Math.random()*100000);				 
				LoadImage(imgpath+'/view/graph/'+tid+'/' + opt + '/'+date+'/'+date2+'/1.png' , imgpath+'/view/graph2/'+tid+'/' + opt + '/'+date2+'/7126x650/2.png');
			    $('#page-area').load('/view/data/'+tid+'/1/'+date+'/'+date2+'?partial=1',function(){});
			    
			}
			function refresh_graph (p) {
				//var rndnum = Math.floor(Math.random()*100000);				
				if (p==1){
					//alert("1234");
					//pweek = "pweekday=1";
					location.href= "/view/data/"+tid+"?pweekday=1&ck=1&d2="+date2;
					//LoadImage(imgpath+'/view/graph/'+tid+'/' + opt + '/'+date+'/'+date2+'/1.png?' + pweek, imgpath+'/view/graph2/'+tid+'/' + opt + '/'+date2+'/7126x650/2.png?' + pweek);
				}
				else {
					location.href= "/view/data/"+tid+"?d2="+date2;
					//LoadImage(imgpath+'/view/graph/'+tid+'/' + opt + '/'+date+'/'+date2+'/1.png', imgpath+'/view/graph2/'+tid+'/' + opt + '/'+date2+'/7126x650/2.png');
					//alert("22221234");
				}
			}

			function set_default_day(dayname) {
				if (dayname == ''){
					$.cookie("set_default_day", null);
					//location.reload();
				}
				else {
					$.cookie("set_default_day", dayname, { expires: 7 });					
					//location.reload();
				}
				
			}
			 /*hidden line*/
			  $("[name='item']").bind('click',function(){
					  opt="";
					  $("[name='item']").each(function(){
					  	if ($(this).attr('checked')){
					  		opt+=$(this).val()+",";
					  		
					  	}
					  	
					  });
					  if (opt == ""){opt=0}
					  refresh_page();
				  });
			 /*hidden pweekday */
			 $("[name='pweekday']").bind('click',function(){
					/*  
					  $("[name='pweekday']").each(function(){
					  	if ($(this).attr('checked')==true){	
					  		refresh_graph(1);	
					  		//alert("abc");
					  	}
					  	else{
					  		refresh_graph(0);
					  		//alert("2222123444444");
					  	}
					  });	*/
				 	if (ck=='1'){
				 		
				 		location.href= "/view/data/"+tid+"?d2="+date2;
				 		//alert("abc");
				 	}else{
				 		//alert("1234");
				 		location.href= "/view/data/"+tid+"?pweekday=1&ck=1&d2="+date2;
				 		
				 		
				 	}
					  
				  });
			 
			 /*only view yesterday data */
			 $("[name='onlyshowyester']").bind('click',function(){
					  
					  $("[name='onlyshowyester']").each(function(){
					  	if ($(this).attr('checked')){	
					  		set_default_day(date2)
					  	}
					  	else{
					  		set_default_day('')
					  	}
					  })					  
					  
				  }); 
			  
		  });
		  
	$.ajaxSetup ({  
        cache: false  
     });
    $.fx.speeds._default = 1000;
     var ajax_load = "<img src='/load2.gif' alt='loading...' />"; 
     function load_logstuff(logstuff){
         $("#dialog_content").html(ajax_load).load(logstuff);
         $( "#dialog" ).dialog( "open" );
         return false;
     }
     $(function(){
    	 largeimg();
     });
     function largeimg(){
    	 $('.largeimg').jqzoom({
             zoomType: 'standard',
             lens:true,
             lensWidth:20,
             lensHeight:250,
             zoomWidth:240,
             zoomHeight:350,
             position:'right',
             preloadImages: true,
             alwaysOn:false,
             title:false,
             xscale:12,
             yOffset:25,
             xOffset:3 
         });
     }