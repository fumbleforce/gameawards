
            
            $('#move').bind('click', function()
            {
                var position = $('#nav-page-container').position();                
                if(position.top == 0)
                {
                    $('#nav-page-container').attr('class', '').addClass('hideDown');
                }
                else
                {
                    $('#nav-page-container').attr('class', '').addClass('hideUp');
                }
            });
            
