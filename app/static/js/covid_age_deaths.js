document.addEventListener("DOMContentLoaded", function () {
    var ctxDeaths = document.getElementById('ageDeathsChart');
    var years = JSON.parse(document.getElementById('chart-data').dataset.years);
    var ageDeaths = JSON.parse(document.getElementById('chart-data').dataset.ageDeaths);
    
    var datasets = [];
    var ageGroups = Object.keys(ageDeaths);

    ageGroups.forEach(function (ageGroup) {
        datasets.push({
            label: ageGroup + ' 세대',
            data: ageDeaths[ageGroup],
            fill: false,
            borderColor: getRandomColor(),
            tension: 0.1
        });
    });

    var ageDeathChart = new Chart(ctxDeaths, {
        type: 'line',
        data: {
            labels: years,
            datasets: datasets
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    },
                    gridLines: {
                        display: false  // y축 그리드 제거
                    }
                }],
                xAxes: [{
                    gridLines: {
                        display: false  // x축 그리드 제거
                    }
                }]
            }
        }
    });

    function getRandomColor() {
        var letters = '0123456789ABCDEF';
        var color = '#';
        for (var i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }
});
