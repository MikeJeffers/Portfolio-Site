var percentSize = 0.18;
var doOnce = true;
var LOADING_GIF = "";
var $container=$('#masonry-grid');

$container.masonry({
 itemSelector:'.grid-item',
 percentPosition:true,
 columnWidth:'.grid-sizer',
 animate:true
});

$container.on('click','.grid-item',function(){
  var $target = $(this);
  var w = $target.width();
  var windowWidth = $container.width();
  var col = windowWidth*percentSize;

  $target.removeClass('.grid-item--width2');
  if(w>col*1.1){
    w=col;
  }else{
    $target.addClass('.grid-item--width2');
    w=col*2;
  }
  $(this).children().animate({width:w});
  $(this).animate({width:w},doSimpleMasonry);
});

function loadingGifURL(url){
  LOADING_GIF = "url("+url+")";
}

function beginLoad(){
  $(".loading-figure").css("background-image", LOADING_GIF).css("height", "40px");
}

function doneLoad(){
  $(".loading-figure").css("background-image", "none").css("height", "0px");
}

function doSimpleMasonry(){
  $container.masonry({
    itemSelector:'.grid-item',
    percentPosition:true,
    columnWidth:'.grid-sizer',
    animate:true
  });
}

function doMasonry(){
  $("div.grid-item").each(eachWrapper);
  $container.imagesLoaded().done(function(instance){
    if(Array.isArray(instance.images)){
      for(let i=0; i<instance.images.length; i++){
        var img = $(instance.images[i].img);
        var parent = img.parent("div");
        divLoaded(parent);
      }
    }
    doneLoad();
    $container.masonry({
      itemSelector:'.grid-item',
      percentPosition:true,
      columnWidth:'.grid-sizer',
      animate:true
    });
  });
}

function eachWrapper(index, element){
  loadingDiv($(element));
}

function loadingDiv(gridItem){
  gridItem.children("img").css("opacity", "0");
}

function divLoaded(gridItem){
  gridItem.addClass('z-depth');
  gridItem.children("img").css("opacity", "1");
}

function onSuccess(data){
  var windowWidth = $container.width();
  var col = windowWidth*percentSize;
  for(var i=0; i<data.imageDict.length; i++){
    var domElement='<div class="grid-item"><img width="'+col+'"src="'+data.imageDict[i]+'"/></div>';
    var $wrap=$(domElement);
    loadingDiv($wrap);
    $container.append($wrap).masonry('appended',$wrap).masonry();
  }
  doMasonry();
}

function resizeElements(){
  var windowWidth = $container.width();
  var w = windowWidth*percentSize;
  $(this).removeClass('.grid-item--width2');
  $(this).children().animate({width:w-3});
  $(this).animate({width:w-3});
}

function onResizeWindow(){
  var navBarHeight = $(".navbar").height();
  $("body").css("padding-top", navBarHeight+10);
  if($container!=null){
    $(".grid-item").each(resizeElements);
    doSimpleMasonry();
  }
  randomScaleImage();
}

function randomScaleImage(){
  var $domElements = $(".grid-item, .grid-item--width2");
  if($domElements!=null && $domElements.size()>0){
    var randomIndex = Math.floor(Math.random()*$domElements.size());
    var $target = $domElements.eq(randomIndex);
    var w = $target.width();
    var windowWidth = $container.width();
    var col = windowWidth*percentSize;
    $target.removeClass('.grid-item--width2');
    if(w>col*1.1){
      w=col;
    }else{
      $target.addClass('.grid-item--width2');
      w=col*2;
    }
    $target.children().animate({width:w});
    $target.animate({width:w},doSimpleMasonry);
  }
}

onResizeWindow();

$(window).smartresize(onResizeWindow);

window.setInterval(randomScaleImage, 10000);