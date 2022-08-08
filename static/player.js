var playButton = document.querySelector('#play-button');
var firstSong = new 
Audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3');
var trackList = [firstSong];

function currentSong() {
    for(var i=0; i<trackList.length; i++) {
        var songID = document.querySelector('#stateicon');
        if (trackList[i].paused) {
            songID.className = 'fas fa-pause'; // Notice how we set className
            trackList[i].play();
        } else {
            songID.className = 'fas fa-play'; // Notice how we set className
            trackList[i].pause();
        }
    }
}