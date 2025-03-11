// characters bar chart
let mycoolchart;
fetch("exports/characters_transformed.json")
.then(response => response.json())
.then(data => {

    var sign = document.getElementById("sign").value;
    var number_val = document.getElementById("numberValue").value;
    var id = [];
    var names = [];
    var episode_count = [];
    var counts = data['no_ep'];
    
    for (const val in counts) {
        if (Number(`${counts[val]}`) >= Number(number_val)) {
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

    const ctx = document.getElementById('myChart');
    mycoolchart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: names,
        datasets: [{
        label: '# of Episodes',
        data: episode_count,
        borderWidth: 1
        }]
    },
    options: {
        scales: {
        y: {
            beginAtZero: true
        }
        }
    }
    });

    document.addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            // Code to execute when Enter is pressed
            console.log("enter");
        }
    });
 
});