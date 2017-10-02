
function userTrack() {
        var x = "User-agent header sent: " + navigator.userAgent;
        document.getElementById("user_agent").innerHTML = x;
}
window.onload = userTrack
