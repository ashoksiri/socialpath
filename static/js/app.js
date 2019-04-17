function get_pages(token) {
    if(!$('#fb-pages').attr('data-loaded')){
       $.get({
        url : 'https://graph.facebook.com/v2.10/me/accounts?access_token='+token,
        method : 'GET',
        success : function (response) {
            var dom = "";
            for (var i = 0; i < response.data.length ; i++) {
                console.log(response.data[i]);
                dom += "<li><a href='#'onclick=\"get_posts('"+response.data[i].id+"','"+response.data[i].access_token+"')\"><i class=\"fas fa-list-alt\"></i>"+response.data[i].name +"</a></li>"
            }
            $('#fb-pages').attr('data-loaded',true);
            $('#fb-pages').append(dom);

    }

    })
    }
}


function get_posts(pageid,token) {
    if(!$('#facebook-posts').attr('data-loaded')){
       $.get({
        url : 'https://graph.facebook.com/v2.10/'+pageid+'/posts?access_token='+token,
        method : 'GET',
        success : function (response) {
            var dom =
                "<div class=\"card\">\n" +
                "   <div class=\"card-header\">\n" +
                "       <strong class=\"card-title\">Card with Label\n" +
                "           <small>\n" +
                "               <span class=\"badge badge-danger float-right mt-1\">49</span>\n" +
                "           </small>\n" +
                "       </strong>\n" +
                "    </div>\n" +
                "    <div class=\"card-body\">\n" +
                "    <p class=\"card-text\">Some quick example text to build on the card title and make up the bulk of the card's\n" +
                "                                            content.\n" +
                "     </p>\n" +
                "     </div>\n" +
                "</div>";
            for (var i = 0; i < response.data.length ; i++) {
                console.log(response.data[i]);
                dom += "<li><a href='#'><i class=\"fas fa-list-alt\"></i>"+response.data[i].name +"</a></li>"
            }
            //$('#facebook-posts').attr('data-loaded',true);
            //$('#facebook-posts').append(dom);

    }

    })
    }
}