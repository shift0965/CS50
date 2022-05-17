function changeText(){
    let heading = document.querySelector("H1");
    if (heading.innerHTML==="Hello World!")
        heading.innerHTML="Good bye!";
    else
        heading.innerHTML="Hello World!";
}

let count = 1;
function counter(){
    count ++;
    let number = document.querySelector("H3");
    number.innerHTML = count;

    if(count %10 === 0){
        alert(`${count} is dividible by 10`);
    }
}
document.addEventListener('DOMContentLoaded', function (){
    document.getElementById("button2").onclick = counter;
});

