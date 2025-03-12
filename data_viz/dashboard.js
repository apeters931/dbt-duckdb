// characters bar chart
var sign = document.getElementById("sign").value;
var number_val = document.getElementById("numberValue").value;
var barChart;

fetch("../exports/characters_transformed.json")
.then(response => response.json())
.then(data => {

    var filtereddata = get_data(data,sign,number_val)[0]

    const ctx = document.getElementById("barchart").getContext("2d");

    const config = {
        type: "bar",
        data: filtereddata,
        options: {
            responsive: true,
            scales: {
                x: {
                    grid: {
                        display: false,
                    },
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    };

    barChart = new Chart(ctx, config);

    barChart.data.datasets = filtereddata.datasets;
    barChart.update();

    document.getElementById("filterButton").onclick = function() {
        barChart.destroy();
        const newVal = document.getElementById("numberValue").value;
        const newSign = document.getElementById("sign").value;
        var newdata = get_data(data,newSign,newVal)[0];
        var names = get_data(data,newSign,newVal)[1];
        barChart = new Chart(ctx, config);
        barChart.data.labels = newdata.labels;
        barChart.data.datasets = newdata.datasets;
        barChart.update();
    }
 
});

 function get_data(data, s, n) {
    var id = [];
    var names = [];
    var episode_count = [];

    var counts = data['no_ep'];

    for (const val in counts) {
        if (s == 'greaterThan' && Number(`${counts[val]}`) >= Number(n)) {
            id.push(val);
        }
        else if (s == 'lessThan' && Number(`${counts[val]}`) <= Number(n)) {
            id.push(val);
        }
    }

    for (const key in data) {
        const obj = data[key]
        for (const value in obj) {
            if (key == 'name' && id.includes(value)) {
                names.push(`${obj[value]}`)
            }
            else if (key == 'no_ep' && id.includes(value)) {
                episode_count.push(`${obj[value]}`) 
            }
        }
    }

    const chartdata = {
        labels: names,
        datasets: [
            {
                label: '# of Episodes',
                data: episode_count,
                backgroundColor: "rgba(75, 192, 192, 0.6)",
            },
        ],
    };

    return [chartdata,names]
 }
