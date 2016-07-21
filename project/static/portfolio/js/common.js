var percentSize = 0.18;

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

  $target.toggleClass('.grid-item--width2');
  if(w>col+1){
    w=col;
  }else{
    w=col*2;
  }
  $(this).children().animate({width:w});
  $(this).animate({width:w},doMasonry);
});

function doMasonry(){
  $container.imagesLoaded().progress(function(){
    $container.masonry({
      itemSelector:'.grid-item',
      percentPosition:true,
      columnWidth:'.grid-sizer',
      animate:true
    });
  }).done(function(){
    $container.masonry({
      itemSelector:'.grid-item',
      percentPosition:true,
      columnWidth:'.grid-sizer',
      animate:true
    });
  });
}

function onSuccess(data){
  var windowWidth = $container.width();
  var col = windowWidth*percentSize;
  for(var i=0; i<data.imageDict.length; i++){
    var domElement='<div class="grid-item"><img width="'+col+'"src="'+data.imageDict[i]+'"/></div>';
    var $wrap=$(domElement);
    $container.append($wrap).masonry('appended',$wrap).masonry();
  }
  doMasonry();
}

function resizeElements(){
  var windowWidth = $container.width();
  var w = windowWidth*percentSize;
  $(this).children().animate({width:w});
  $(this).animate({width:w});
}

function onResizeWindow(){
  var navBarHeight = $(".navbar").height();
  $("body").css("padding-top", navBarHeight+10);
  console.log(navBarHeight);
  if($container!=null){
    $(".grid-item").each(resizeElements);
    doMasonry();
  }
  randomScaleImage();
}

function randomScaleImage(){
  var $domElements = $(".grid-item");
  if($domElements!=null && $domElements.size()>0){
    var randomIndex = Math.floor(Math.random()*$domElements.size());
    var $target = $domElements.eq(randomIndex);
    var w = $target.width();
    var windowWidth = $container.width();
    var col = windowWidth*percentSize;
    $target.removeClass('.grid-item--width2');
    if(w>col+1){
     w=col;
   }else{
    $target.addClass('.grid-item--width2');
     w=col*2;
   }
   $target.children().animate({width:w});
   $target.animate({width:w},doMasonry);
 }
}

onResizeWindow();

$(window).smartresize(onResizeWindow);

window.setInterval(randomScaleImage, 10000);