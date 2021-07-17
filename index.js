const board = document.querySelectorAll(".parent div");
const score_board = document.querySelector("#score-board");
const less_board = document.querySelector("#less-board");
const flags = Array(9);
const correct = new Map([
    ["q",0],
    ["w",1],
    ["e",2],
    ["a",3],
    ["s",4],
    ["d",5],
    ["z",6],
    ["x",7],
    ["c",8],

    ["Q",0],
    ["W",1],
    ["E",2],
    ["A",3],
    ["S",4],
    ["D",5],
    ["Z",6],
    ["X",7],
    ["C",8],

    ["ㅂ",0],
    ["ㅈ",1],
    ["ㄷ",2],
    ["ㅁ",3],
    ["ㄴ",4],
    ["ㅇ",5],
    ["ㅋ",6],
    ["ㅌ",7],
    ["ㅊ",8] 
]);


let time = 1500;

let score = 0;
let less = 0;

flags.fill(0);


function draw() {
    for(let i=0; i<9; i++) {
        if (flags[i] === 1) {
            board[i].style.backgroundColor = "blue";
        } else {
            board[i].style.backgroundColor = "white";
        }
    }
}

console.log(score_board.innerHTML);
console.log(board);

setInterval(function() {
    for(let i=0; i<9; i++) {
        if(flags[i] === 1) less++;
        flags[i] = 0;
    }
    score_board.innerText = "점수 : " + score;
    less_board.innerText = "놓친 개수 : " + less;
    
    const rand1 = Math.floor(Math.random()*9);
    flags[rand1] = 1;
    
    draw();
}, time);

setInterval(function() {

}, time)

window.addEventListener("keydown", function(e) {
    const keytype = e.key;
    const idx = correct.get(keytype);
    
    if(idx === undefined) return;
    if(flags[idx] === 1) {
        score++;
        flags[idx] = 0;
        
        time -= 100;
        console.log(time);
        draw();
    }
    
})