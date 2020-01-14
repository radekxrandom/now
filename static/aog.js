$(document).ready(function() {
document.addEventListener('contextmenu', event => event.preventDefault());

//var a1 = $('#audio')
var a1 = document.getElementById('audio');
a1.setAttribute("src","static/1.wav");
//a1.attr("src","static/1.wav");
var a2 = document.getElementById('audio1');
a2.setAttribute("src","static/2.wav");
//var a2 = $('#audio1')
//a2.attr("src","static/2.wav");
function pl(){
a1.play();
a1.addEventListener('ended', () => {
    console.log('dull');
    // done playing
    a2.play();
    a2.addEventListener('ended', () => {
      console.log('dwa');
        localStorage.commonfunc = '1';
      window.location.replace("http://127.0.0.1:8000/");

  });
});
}
setTimeout(pl,2000);
})
