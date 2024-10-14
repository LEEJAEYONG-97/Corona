// 차트 데이터를 가져오는 함수
function getNoAudienceChartData() {
    const chartDataElement = document.getElementById('chart-data');
    
    // 데이터가 없으면 null 반환
    if (!chartDataElement) {
        return null;
    }

    return {
        organizations: JSON.parse(chartDataElement.dataset.organizations),
        noAttendanceGames: JSON.parse(chartDataElement.dataset.noAttendanceGames)
    };
}

// 조직별 무관중 경기 차트를 생성하는 함수
function createNoAudienceBarChart(ctx, labels, data) {
    return new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels, // 조직 이름 배열
            datasets: [{
                label: '무관중 경기 수',
                data: data, // 무관중 경기 수 데이터
                backgroundColor: 'rgba(54, 162, 235, 0.6)', // 바의 색상
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: '협회별 무관중 경기 수'
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    },
                    scaleLabel: {
                        display: true,
                        labelString: '무관중 경기 수'
                    },
                    gridLines: {
                        display: false  // y축의 눈금선 제거
                    }
                }],
                xAxes: [{
                    gridLines: {
                        display: false  // x축의 눈금선 제거
                    }
                }]
            }
        }
    });
}

// 차트 렌더링 함수
function renderNoAudienceChart() {
    const chartData = getNoAudienceChartData();
    
    if (!chartData) {
        console.error('No chart data found.');
        return;
    }

    const ctx = document.getElementById('noAudienceChart').getContext('2d');
    createNoAudienceBarChart(ctx, chartData.organizations, chartData.noAttendanceGames);
}

// 페이지 로드 시 차트를 렌더링
document.addEventListener('DOMContentLoaded', function () {
    renderNoAudienceChart();
});
