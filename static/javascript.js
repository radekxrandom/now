$(document).ready(function() {
    if(!localStorage.butBlock){
        localStorage.butBlock = 0;
    }
    if (localStorage.butBlock == '0'){
        $('#bteraz').css('filter', 'none');
        $('#bpo').css('filter', 'none');
        $('#bteraz').on( "click", function(e) {
            e.preventDefault();
        });
        $('#bpo').on( "click", function(e) {
            e.preventDefault();
        });
        $('#bprzed').on( "click", function(e) {
            localStorage.butBlock = 1;
        });
    }
    else if (localStorage.butBlock =='1'){
        $('#bpo').css('filter', 'none');
        $('#bprzed').css('filter', 'none');
        $('#bprzed').on( "click", function(e) {
            e.preventDefault();
        });
        $('#bpo').on( "click", function(e) {
            e.preventDefault();
        });
        $('#bteraz').on( "click", function(e) {
            localStorage.butBlock = 2;
        });
    }
    else if (localStorage.butBlock == '2'){
        $('#bprzed').css('filter', 'none');
        $('#bteraz').css('filter', 'none');
        $('#bprzed').on( "click", function(e) {
            e.preventDefault();
        });
        $('#bteraz').on( "click", function(e) {
            e.preventDefault();
        });
        $('#bprzed').on( "click", function(e) {
            localStorage.butBlock = 3;
        });
    }
    else if (localStorage.butBlock == '3'){
        $('#bteraz').css('filter', 'none');
        $('#bteraz').on( "click", function(e) {
            e.preventDefault();
        });
    }


})
