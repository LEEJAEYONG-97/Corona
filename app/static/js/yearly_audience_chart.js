// 연도별 관객수 데이터를 가져오는 함수
function getAudienceChartData() {
    const chartDataElement = document.getElementById('chart-data');
    const years = JSON.parse(chartDataElement.dataset.years);
    const audienceCounts = JSON.parse(chartDataElement.dataset.audienceCounts);

    // 2019 ~ 2023년 데이터만 필터링
    const filteredYears = [];
    const filteredAudienceCounts = [];
    
    years.forEach((year, index) => {
        if (year >= 2019 && year <= 2023) {
            filteredYears.push(year);
            filteredAudienceCounts.push(audienceCounts[index]);
        }
    });

    return { filteredYears, filteredAudienceCounts };
}

// 차트를 렌더링하는 함수
function renderAudienceChart() {
    const { filteredYears, filteredAudienceCounts } = getAudienceChartData();
    const ctx = document.getElementById('audienceChart').getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: filteredYears,  // 2019 ~ 2023년만 사용
            datasets: [{
                label: '연도별 관객수',
                data: filteredAudienceCounts,
                backgroundColor: 'rgba(54, 162, 235, 0.7)',  // 파란색 배경 (투명도 추가)
                borderColor: 'rgba(54, 162, 235, 1)',         // 파란색 테두리
                borderWidth: 1,  // 테두리 두께
            }]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: '연도별 관객수 (2019~2023)'
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    },
                    gridLines: {
                        display: false  // x축의 눈금선 제거
                    }
                }],
                xAxes: [{
                    gridLines: {
                        display: false
                    }
                }]
            }
        }
    });
}

// 페이지가 로드되면 차트 렌더링
document.addEventListener('DOMContentLoaded', function () {
    renderAudienceChart();
});
