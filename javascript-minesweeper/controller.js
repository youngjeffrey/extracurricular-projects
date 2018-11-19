var MOUSE_LEFT = 1,
    MOUSE_RIGHT = 3;

canvas.addEventListener('click', function(e) {
    var x = e.clientX - canvas.offsetLeft,
        y = e.clientY - canvas.offsetTop;

    // hit test
    var modelCoordinates = viewToModel(x, y);

/*    switch (e.which) {
        case MOUSE_LEFT:
            openBlock(modelCoordinates.x, modelCoordinates.y);
            break;
        case MOUSE_RIGHT:
            flagBlock(modelCoordinates.x, modelCoordinates.y);
    }*/
    
    if(e.shiftKey) {
        //decMine();
        flagBlock(modelCoordinates.x, modelCoordinates.y);
    } else {
        openBlock(modelCoordinates.x, modelCoordinates.y);
        //break;
    }

    render();

    return false;
});

function letsPlay() {
    init();
    render();
}

canvas.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    return false;
}, false);