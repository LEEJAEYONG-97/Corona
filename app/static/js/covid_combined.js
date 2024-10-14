document.addEventListener("DOMContentLoaded", function () {
    var ctx = document.getElementById("combinedChart");

    if (ctx) {
        var months = JSON.parse(document.getElementById('chart-data').dataset.months);
        var casesData = JSON.parse(document.getElementById('chart-data').dataset.monthlyCases);
        var deathsData = JSON.parse(document.getElementById('chart-data').dataset.monthlyDeaths);

        var combinedChart = new Chart(ctx, {
            type: 'line', // 선형 차트
            data: {
                labels: months,
                datasets: [{
                    label: "확진자 수",
                    lineTension: 0.3,
                    backgroundColor: "rgba(75,192,192,0.2)",
                    borderColor: "rgba(75,192,192,1)",
                    pointRadius: 5,
                    pointBackgroundColor: "rgba(75,192,192,1)",
                    pointBorderColor: "rgba(255,255,255,0.8)",
                    pointHoverRadius: 5,
                    pointHoverBackgroundColor: "rgba(75,192,192,1)",
                    pointHitRadius: 50,
                    pointBorderWidth: 2,
                    data: casesData,
                    yAxisID: 'y-axis-cases' // 왼쪽 Y축
                },
                {
                    label: "사망자 수",
                    lineTension: 0.3,
                    backgroundColor: "rgba(255,99,132,0.2)",
                    borderColor: "rgba(255,99,132,1)",
                    pointRadius: 5,
                    pointBackgroundColor: "rgba(255,99,132,1)",
                    pointBorderColor: "rgba(255,255,255,0.8)",
                    pointHoverRadius: 5,
                    pointHoverBackgroundColor: "rgba(255,99,132,1)",
                    pointHitRadius: 50,
                    pointBorderWidth: 2,
                    data: deathsData,
                    yAxisID: 'y-axis-deaths' // 오른쪽 Y축
                }]
            },
            options: {
                scales: {
                    xAxes: [{
                        time: {
                            unit: 'date'
                        },
                        gridLines: {
                            display: false
                        },
                        ticks: {
                            maxTicksLimit: 7
                        }
                    }],
                    yAxes: [{
                        id: 'y-axis-cases', // 왼쪽 Y축
                        type: 'linear',
                        position: 'left',
                        ticks: {
                            beginAtZero: true
                        },
                        scaleLabel: {
                            display: true,
                            labelString: '확진자 수'
                        },
                        gridLines: {
                            display: false
                        }
                    }, {
                        id: 'y-axis-deaths', // 오른쪽 Y축
                        type: 'linear',
                        position: 'right',
                        ticks: {
                            beginAtZero: true
                        },
                        scaleLabel: {
                            display: true,
                            labelString: '사망자 수'
                        },
                        gridLines: {
                            drawOnChartArea: false // 오른쪽 축의 격자선을 그리지 않음
                        }
                    }]
                },
                legend: {
                    display: true
                }
            }
        });
    }
});
