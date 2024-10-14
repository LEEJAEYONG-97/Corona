// DOM에서 데이터를 가져오는 함수
function getChartData() {
    const chartDataElement = document.getElementById('chart-data');
    return {
        monthsCovid: JSON.parse(chartDataElement.dataset.monthsCovid),
        cases: JSON.parse(chartDataElement.dataset.cases),
        monthsAttendance: JSON.parse(chartDataElement.dataset.monthsAttendance),
        attendance: JSON.parse(chartDataElement.dataset.attendance)
    };
}

// 차트를 생성하는 함수 (COVID-19는 Line, 관중수는 Bar)
function createCovidAttendanceChart(ctx, monthsCovid, cases, monthsAttendance, attendance) {
    return new Chart(ctx, {
        type: 'bar', // 기본 타입은 bar (관중수)
        data: {
            labels: monthsCovid, // 월별 레이블 (COVID 데이터 기준)
            datasets: [
                {
                    type: 'line', // COVID-19 데이터는 Line 차트
                    label: '확진자 수',
                    data: cases, // 월별 확진자 수 데이터
                    borderColor: 'rgba(255, 99, 132, 1)',
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderWidth: 2,
                    yAxisID: 'y-axis-covid' // Line 차트는 왼쪽 Y축
                },
                {
                    label: '관중 수',
                    data: attendance, // 월별 관중수 데이터
                    backgroundColor: 'rgba(54, 162, 235, 0.6)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1,
                    yAxisID: 'y-axis-attendance' // Bar 차트는 오른쪽 Y축
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                yAxes: [
                    {
                        id: 'y-axis-covid',
                        type: 'linear',
                        position: 'left',
                        ticks: {
                            beginAtZero: true,
                            callback: function(value) { return value + '명'; }
                        },
                        scaleLabel: {
                            display: true,
                            labelString: '확진자 수'
                        },
                        gridLines: {
                            display: false  // y축의 눈금선 제거
                        }
                    },
                    {
                        id: 'y-axis-attendance',
                        type: 'linear',
                        position: 'right',
                        ticks: {
                            beginAtZero: true,
                            callback: function(value) { return value + '명'; }
                        },
                        scaleLabel: {
                            display: true,
                            labelString: '관중 수'
                        },
                        gridLines: {
                            display: false  // y축의 눈금선 제거
                        }
                    }
                ],
                xAxes: [{
                    gridLines: {
                        display: false  // x축의 눈금선 제거
                    }
                }]
            }
        }
    });
}

// 차트 렌더링
document.addEventListener('DOMContentLoaded', function () {
    const { monthsCovid, cases, monthsAttendance, attendance } = getChartData();
    const ctx = document.getElementById('covidAttendanceChart').getContext('2d');
    createCovidAttendanceChart(ctx, monthsCovid, cases, monthsAttendance, attendance);
});
