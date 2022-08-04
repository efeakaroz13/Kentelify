function blinker(){
    blinkers = document.getElementsByClassName("blinker")
    for (let blink = 0; blink < blinkers.length; blink++) {
        const element = blinkers[blink];
        displaycheck = element.style.display;
        if (displaycheck == "none") {
            blinkers[blink].style.display="";
            
        }
        else{
            blinkers[blink].style.display="none";
        }
        
    }
}
setInterval(blinker,400)

letterlist = []
document.addEventListener('keydown', (e) => {

    console.log(e.code)
    letter = e.code.split("Key")[1];
    
    digit = e.code.split("Digit")[1];

    
    if(letter == undefined){
        
        if(e.code == "ShiftRight"){
            letterlist.length = 0;

            letterlist.push("A2")
        }
        if (e.code == "ShiftLeft"){
            letterlist.length = 0
            letterlist.push("A1")
        }
        if(e.code == "Space"){
            if(letterlist[0] == "A1"){
                letterlist.length = 0;
                navigator.clipboard.readText().then((clipText) => (document.getElementById("query").innerHTML = clipText));
            }
            else{
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+" "
            }
        }
        if (e.code == "Backspace") {
            const query = document.getElementById("query").innerHTML


            const queryarray = query.split('')

            queryarray.pop()


            const newquery = queryarray.join('')
            document.getElementById("query").innerHTML = newquery
        }
        if (e.code =="Enter") {
            input = document.getElementById("query").innerHTML;
            document.getElementById("logs").innerHTML = document.getElementById("logs").innerHTML+"<p>Kentelify:~ admin <a style='color:rgb(52, 52, 254)'>$</a> "+input+"</p>"
            document.getElementById("query").innerHTML = ""
            if(input.trim() == "clear" || input.trim() == "cls" ){
                document.getElementById("logs").innerHTML = ""
            }
            if(input.trim().split("alert(")[1] !=undefined){
                alert(input.trim().split("alert(")[1].replace(")",""))
            }
        }

    }

    else{
        if(letterlist[0] == "A2"){
            letterlist.length=0
            document.getElementById("query").innerHTML = document.getElementById("query").innerHTML + letter;
        }else{
            document.getElementById("query").innerHTML = document.getElementById("query").innerHTML + letter.toLowerCase()
        }
        

    }
    if (digit != undefined) {
        if (digit == "8") {
            if (letterlist[0] == "A2"){
                letterlist.length = 0
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"("
            }else{
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"8"
            }
        }
        if (digit == "7") {
            if (letterlist[0] == "A2"){
                letterlist.length = 0
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"/"
            }else{
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"7"
            }
        }
        if (digit == "9") {
            if (letterlist[0] == "A2"){
                letterlist.length = 0
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+")"
            }else{
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"9"
            }
        }
    }

    
});