$(document).ready(function() { 
    if(!localStorage.butBlock){
        localStorage.butBlock = 0;
    }
    if (localStorage.butBlock == '0'){
        $('#bteraz').css('background-color', 'grey !important');
        $('#bpo').css('background-color', 'grey !important');
        $('#bteraz').on( "click", function(e) {
            e.preventDefault();    
        });
        $('#bpo').on( "click", function(e) {
            e.preventDefault();    
        });
    }
    else if (localStorage.butBlock =='1'){
        $('#bpo').css('background-color', 'grey !important');
        $('#bprzed').css('background-color', 'grey !important');
        $('#bprzed').on( "click", function(e) {
            e.preventDefault();    
        });
        $('#bpo').on( "click", function(e) {
            e.preventDefault();    
        });
    }
    else if (localStorage.butBlock == '2'){
        $('#bprzed').css('background-color', 'grey !important');
        $('#bteraz').css('background-color', 'grey !important');
        $('#bprzed').on( "click", function(e) {
            e.preventDefault();    
        });
        $('#bteraz').on( "click", function(e) {
            e.preventDefault();    
        });
    }




})