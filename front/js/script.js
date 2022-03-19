google.charts.load('current', { 'packages': ['corechart'] });
google.charts.setOnLoadCallback(drawChart);

function Get() {
    let Http = new XMLHttpRequest();
    Http.open("GET", "http://127.0.0.1:8000/DAILY/USD/EUR/");
    //Http.send(null);
    Http.responseType = 'json';
    return Http.json_data;
 }

 function build_data() {
    var json_obj = JSON.parse(Get());
    console.log(json_obj);
    return json_obj;
 }

    function drawChart() {
        let json_data = build_data();
        let title = json_data['Meta Data']['2. From Symbol'] + json_data['Meta Data']['3. To Symbol'];
        let data = new google.visualization.DataTable();
        data.addColumn('date', 'Day');
        data.addColumn('number', 'Open');
        data.addColumn('number', 'High');
        data.addColumn('number', 'Low');
        data.addColumn('number', 'Close');
        let prices = json_data['Time Series FX (Daily)'];
        Object.entries(prices).forEach(([key, value]) => {
            data.addRow([new Date(key), parseFloat(value['1. open']), parseFloat(value['2. high']), parseFloat(value['3. low']), parseFloat(value['4. close'])]);
        });

        let options = {
            legend: 'none'
        }

        let chart = new google.visualization.CandlestickChart(document.getElementById('chart'));
        chart.draw(data, options);
      }