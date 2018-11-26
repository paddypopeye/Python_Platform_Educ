(function(){
    if(window.myBookmarklet!==undefined){
        myBookmarklet();
    }
    else{
        document.body.appendChild(document.createElement('script')).src='http://192.168.10.10:9999/static/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999);
    }
})();