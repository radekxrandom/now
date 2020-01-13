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
        $('#bpo').on( "click", function(e) {
            localStorage.butBlock = 0;
        });
    }
    else if (localStorage.butBlock == '3'){
      localStorage.butBlock = 0;
        $('#bteraz').css('filter', 'none');
        $('#bteraz').on( "click", function(e) {
            e.preventDefault();
        });
    }


$('#addline').on( "click", function(e) {
    console.log('pach');
    var w = $(this).siblings().length;
    w++;
    var html = ''+
    '<form method=\'POST\'>'+
    '<input type=\'text\' id=\'pd\'  name=\'engline\' />'+
    '<input type=\'text\' id=\'pd\' name=\'plline\' />'+
    '<input style=\'display:none;\' value='+w+' name=\'numline\' />'+
    '<button type="submit" class="btn btn-primary" name=\'edit_main\' >save line</button>'+
    '</form>'
    $(this).before(html);
});
$('#addline1').on( "click", function(e) {
    console.log('pach');
    var w = $(this).siblings().length;
    w++;
    var html = ''+
    '<form method=\'POST\'>'+
    '<input type=\'text\' id=\'pd\'  name=\'engline\' />'+
    '<input type=\'text\' id=\'pd\' name=\'plline\' />'+
    '<input style=\'display:none;\' value='+w+' name=\'numline\' />'+
    '<button type="submit" class="btn btn-primary" name=\'edit_przed\' >save line</button>'+
    '</form>'
    $(this).before(html);
});
$('#addline2').on( "click", function(e) {
    console.log('pach');
    var w = $(this).siblings().length;
    w++;
    var html = ''+
    '<form method=\'POST\'>'+
    '<input type=\'text\' id=\'pd\'  name=\'engline\' />'+
    '<input type=\'text\' id=\'pd\' name=\'plline\' />'+
    '<input style=\'display:none;\' value='+w+' name=\'numline\' />'+
    '<button type="submit" class="btn btn-primary" name=\'edit_po\' >save line</button>'+
    '</form>'
    $(this).before(html);
});
$('#addline3').on( "click", function(e) {
    console.log('pach');
    var w = $(this).siblings().length;
    w++;
    var html = ''+
    '<form method=\'POST\'>'+
    '<input type=\'text\' id=\'pd\'  name=\'engline\' />'+
    '<input type=\'text\' id=\'pd\' name=\'plline\' />'+
    '<input style=\'display:none;\' value='+w+' name=\'numline\' />'+
    '<button type="submit" class="btn btn-primary" name=\'edit_getinfo\' >save line</button>'+
    '</form>'
    $(this).before(html);
});
})
