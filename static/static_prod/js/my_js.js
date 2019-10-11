maudio({
    obj:'audio',
    fastStep:10
})

$('audio').on('abort',function(){
  console.log('abort')
})

$('audio').on('canplay',function(){
  console.log('canplay')
})

$('audio').on('canplaythrough',function(){
  console.log('canplaythrough')
})

$('audio').on('durationchange',function(){
  console.log('durationchange')
})

$('audio').on('emptied',function(){
  console.log('emptied')
})

$('audio').on('ended',function(){
  console.log('ended')
})

$('audio').on('error',function(){
  console.log('error')
})

$('audio').on('loadeddata',function(){
  console.log('loadeddata')
})

$('audio').on('loadedmetadata',function(){
  console.log('loadedmetadata')
})

$('audio').on('loadstart',function(){
  console.log('loadstart')
})

$('audio').on('pause',function(){
  console.log('pause')
})

$('audio').on('play',function(){
  console.log('play')
})

$('audio').on('playing',function(){
  console.log('playing')
})

$('audio').on('progress',function(){
  console.log('progress')
})

$('audio').on('ratechange',function(){
  console.log('ratechange')
})

$('audio').on('seeked',function(){
  console.log('seeked')
})

$('audio').on('seeking',function(){
  console.log('seeking')
})

$('audio').on('stalled',function(){
  console.log('stalled')
})

$('audio').on('suspend',function(){
  console.log('suspend')
})

$('audio').on('timeupdate',function(){
  console.log('timeupdate')
});


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getCookie1(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



function like() {
    var like = $(this);
    var type = like.data('type');
    var pk = like.data('id');
    var action = like.data('action');
    var dislike = like.next();
    like.removeClass('btn-flickr');
    like.addClass('btn-info ');

    $.ajax({
        url : "/api/" + type + "/" + pk + "/" + action + "/",
        type : 'POST',
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        data : {'obj' : pk},
        success : function (json) {
            like.find("[data-count='like']").text(json.like_count);
            dislike.find("[data-count='dislike']").text(json.dislike_count);
        }
});

return false;
}


function dislike()
{
    var dislike = $(this);
    var type = dislike.data('type');
    var pk = dislike.data('id');
    var action = dislike.data('action');
    var like = dislike.prev();

    $.ajax({
        url : "/api/" + type +"/" + pk + "/" + action + "/",
        type : 'POST',
        headers: { "X-CSRFToken": getCookie1("csrftoken") },
        data : { 'obj' : pk },

        success : function (json) {
            dislike.find("[data-count='dislike']").text(json.dislike_count);
            like.find("[data-count='like']").text(json.like_count);
        }
    });

    return false;
}

// Подключение обработчиков
$(function() {
    $('[data-action="like"]').click(like);
    $('[data-action="dislike"]').click(dislike);
});


var url = window.location.href;
var filepath = url.lastIndexOf("/") + 1;
var matchThis = url.substr(filepath);
$('#pagination1').find("a[href*='"+matchThis+"']").parent().addClass('active');

