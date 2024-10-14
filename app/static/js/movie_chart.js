// 차트 데이터를 가져오는 함수
function getMovieChartData() {
    const chartDataElement = document.getElementById('chart-data');
    const yearlyDataCount = JSON.parse(chartDataElement.dataset.yearlyDataCount); // 개봉 영화 편수
    const yearlyScreenCount = JSON.parse(chartDataElement.dataset.yearlyScreenCount); // 상영관 수

    // 2019년부터 2023년까지의 데이터를 필터링
    const filteredYears = ['2019', '2020', '2021', '2022', '2023'];
    const filteredDataCount = {};
    const filteredScreenCount = {};

    filteredYears.forEach(year => {
        if (yearlyDataCount[year] !== undefined && yearlyScreenCount[year] !== undefined) {
            filteredDataCount[year] = yearlyDataCount[year];
            filteredScreenCount[year] = yearlyScreenCount[year];
        }
    });

    return { filteredDataCount, filteredScreenCount };
}

// 연도별 개봉 영화 편수 및 스크린 수 차트를 생성하는 함수
function renderYearlyDataChart() {
    const { filteredDataCount, filteredScreenCount } = getMovieChartData();
    const ctx = document.getElementById('yearlyDataChart').getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(filteredDataCount),  // x축은 연도 (필터링된 연도만 표시)
            datasets: [
                {
                    label: '개봉 영화 편수',
                    data: Object.values(filteredDataCount),  // 개봉 영화 편수 데이터
                    backgroundColor: 'rgba(54, 162, 235, 0.6)',  // 파란색 바
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1,
                    yAxisID: 'y-left',  // 왼쪽 y축
                    type: 'bar'  // 바 차트
                },
                {
                    label: '상영관 수',
                    data: Object.values(filteredScreenCount),  // 상영관 수 데이터
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',  // 빨간색 바
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1,
                    yAxisID: 'y-right',  // 오른쪽 y축
                    type: 'line'  // 선 차트
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                yAxes: [
                    {
                        id: 'y-left',
                        position: 'left',
                        ticks: {
                            beginAtZero: true
                        },
                        scaleLabel: {
                            display: true,
                            labelString: '개봉 영화 편수'
                        },
                        gridLines: {
                            display: false  // 왼쪽 y축의 눈금선 제거
                        }
                    },
                    {
                        id: 'y-right',
                        position: 'right',
                        ticks: {
                            beginAtZero: true
                        },
                        scaleLabel: {
                            display: true,
                            labelString: '상영관 수'
                        },
                        gridLines: {
                            display: false  // 오른쪽 y축의 눈금선 제거
                        }
                    }
                ],
                xAxes: [{
                    gridLines: {
                        display: false  // x축의 눈금선 제거
                    }
                }]
            },
            title: {
                display: true,
                text: '연도별 개봉 영화 편수 및 상영관 수 (2019-2023)'
            }
        }
    });
}

// 페이지 로드 시 차트를 렌더링
document.addEventListener('DOMContentLoaded', function () {
    renderYearlyDataChart();
});
