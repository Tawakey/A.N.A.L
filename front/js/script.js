function Get() {
    let Http = new XMLHttpRequest();
    Http.open("GET", "http://127.0.0.1:8000/");
    //Http.send(null);
    return Http.responseText;
 }
