var generator = prompt("Enter 1 to generate your own minefield. Enter 2 for a minefield to be randomly generated.")
var answer = parseInt(generator);
var COLS, ROWS, MINES;
var numclicks = 0;
var list_times = [];
var min;

if(answer == 1) {
    var c1 = prompt("Enter columns", "0");
    var r1 = prompt("Enter rows", "0");
    var m1 = prompt("Enter mines", "0");

    COLS = parseInt(c1);
    ROWS = parseInt(r1);
    MINES = parseInt(m1);
} else {
    var diff = prompt("Choose level of difficulty. 1 is Easy, 2 is Medium, 3 is Hard.")
    var difficulty = parseInt(diff);
    
    if(difficulty == 1) {
        ROWS = Math.floor((Math.random() * 15) + 8);
        COLS = Math.floor((Math.random() * 15) + 8);
        MINES = Math.floor((Math.random() * Math.ceil(COLS*ROWS*0.15)) + 1);
    } else if(difficulty == 2) {
        ROWS = Math.floor((Math.random() * 22) + 15);
        COLS = Math.floor((Math.random() * 22) + 15);
        MINES = Math.floor((Math.random() * Math.ceil(COLS*ROWS*0.25)) + Math.ceil(COLS*ROWS*0.15));
    } else {
        ROWS = Math.floor((Math.random() * 30) + 22);
        COLS = Math.floor((Math.random() * 40) + 22);
        MINES = Math.floor((Math.random() * Math.ceil(COLS*ROWS*0.45)) + Math.ceil(COLS*ROWS*0.30));
    }
}

if(COLS < 8) {
    COLS = 8;
} else if(COLS > 40) {
    COLS = 40;
}

if(ROWS < 8) {
    ROWS = 8;
} else if(ROWS > 30) {
    ROWS = 30;
}

var AREA = ROWS * COLS;

if(MINES < 1) {
    MINES = 1;
} else if(MINES >= AREA) {
    MINES = AREA - 1;
}

var board = [];
var state = [];
var STATE_CLOSED = 0,
    STATE_FLAGGED = 1,
    STATE_OPENED = 2;
var BLOCK_MINE = -1;
var playing = true;

function inBounds(x, y) {
    return x >= 0 && y >= 0
        && x < COLS && y < ROWS;
}

function countMinesAround(x, y) {
    var count = 0;
    for (var dx = -1; dx <= 1; ++dx) {
        for (var dy = -1; dy <= 1; ++dy) {
            if (dx == 0 && dy == 0) {
                continue;
            }
            var yy = y + dy,
                xx = x + dx;
            if (inBounds(xx, yy)) {
                if (board[yy][xx] == BLOCK_MINE) {
                    count++;
                }
            }
        }
    }
    return count;
}

function init() {
    decMine(MINES);
    
    for (var y = 0; y < ROWS; ++y) {
        board.push([]);
        state.push([]);
        for (var x = 0; x < COLS; ++x) {
            board[y].push(0);
            state[y].push(STATE_CLOSED);
        }
    }

    for (var mine = 0; mine < MINES; ++mine) {
        var x, y;
        do {
            x = Math.floor(Math.random() * COLS),
            y = Math.floor(Math.random() * ROWS);
        } while (board[y][x] == BLOCK_MINE);

        board[y][x] = BLOCK_MINE;
    }

    for (var y = 0; y < ROWS; ++y) {
        for (var x = 0; x < COLS; ++x) {
            if (board[y][x] != BLOCK_MINE) {
                board[y][x] = countMinesAround(x, y);
            }
        }
    }
    

}

var time = 0;
var timer1;
function timer() {
    if(playing == true) {
        var timer1 = setTimeout(function() {
        var timerDiv = document.getElementById("seconds");
        time++;
        timerDiv.innerHTML = time;
        timer();
        },1000);
    } else {
        clearTimeout(timer1);
    }
}

function openBlock(x, y) {
    numclicks++;
    
    if(numclicks == 1) {
        timer();
    }
    
    if (!playing) {
        return;
    }
    if (state[y][x] == STATE_FLAGGED) {
        return;
    }

    if (board[y][x] == BLOCK_MINE) {
        playing = false;
        revealBoard(false);
        timer();
        document.getElementById("game-status").innerHTML = 
            "<br> <h2 style='text-align: center;'>GAMEOVER <img src='deademoji.png' height='40' width='40'></h2>";
        return;
    }

    state[y][x] = STATE_OPENED;
    if (board[y][x] == 0) {
        for (var dx = -1; dx <= 1; ++dx) {
            for (var dy = -1; dy <= 1; ++dy) {
                var xx = x + dx,
                    yy = y + dy;
                if (inBounds(xx, yy)) {
                    if (state[yy][xx] != STATE_OPENED) {
                        openBlock(xx, yy);
                    }
                }
            }
        }
    }

    if (checkVictory()) {
        MINES = 0;
        decMine(MINES);
        document.getElementById("game-status").innerHTML = 
            "<br> <h2 style='text-align: center;'>YOU ARE VICTORIUS <img src='smiley.png' height='40' width='40'></h2>";
        playing = false;
        timer();
        list_times.push(time);
        min = Math.min.apply(null, list_times);
        
        if(time == min) {
            document.getElementById("high-score").innerHTML = 
                "You have a new personal best time of &nbsp;&nbsp;" + min + "&nbsp;&nbsp; seconds";
        } else {
            document.getElementById("high-score").innerHTML = 
                "Your best time is &nbsp;&nbsp;" + min + "&nbsp;&nbsp; seconds";
        }
        
        revealBoard(true);
    }
}

function checkVictory() {
    for (var y = 0; y < ROWS; ++y) {
        for (var x = 0; x < COLS; ++x) {
            if (board[y][x] != BLOCK_MINE) {
                if (state[y][x] != STATE_OPENED) {
                    return false;
                }
            }
        }
    }
    return true;
}

function flagBlock(x, y) {
    
    //console.log(MINES);
    if (state[y][x] == STATE_OPENED) {
        return;
    }
    
    if (state[y][x] == STATE_FLAGGED) {
        MINES++;
        decMine(MINES);
    } else {
        if(MINES <= -1) {
            return;
        }
        MINES--;
        decMine(MINES);
    }

    state[y][x] = 1 - state[y][x];
    
    if(checkVictory() == false && MINES==-1) {
        alert("Are you sure you flagged all the mines at the correct location?");
    }
}

function decMine(mines) {
    document.getElementById("minesleft").innerHTML = mines;
}

function revealBoard(victorious) {
    for (var y = 0; y < ROWS; ++y) {
        for (var x = 0; x < COLS; ++x) {
            if (board[y][x] == BLOCK_MINE && victorious) {
                state[y][x] = STATE_FLAGGED;
                continue;
            }
            state[y][x] = STATE_OPENED;
        }
    }
}

init();
