// DOM에서 데이터를 가져오는 함수
function getChartData() {
    const chartDataElement = document.getElementById('chart-data');
    return {
        regionCityConfirmed: JSON.parse(chartDataElement.dataset.regionCityConfirmed),
        regionCityDeaths: JSON.parse(chartDataElement.dataset.regionCityDeaths)
    };
}

// 차트를 생성하는 함수 (Y축 2개 추가)
function createBarChart(ctx, labels, confirmedData, deathsData, regionTitle) {
    return new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,  // 도시 이름 배열
            datasets: [
                {
                    label: '확진자 수',
                    data: confirmedData,  // 확진자 데이터 배열
                    backgroundColor: 'rgba(75, 192, 192, 0.6)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                    yAxisID: 'yConfirmed',  // 확진자용 Y축 설정
                },
                {
                    label: '사망자 수',
                    data: deathsData,  // 사망자 데이터 배열
                    backgroundColor: 'rgba(255, 99, 132, 0.6)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1,
                    yAxisID: 'yDeaths',  // 사망자용 Y축 설정
                }
            ]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: `${regionTitle} 확진자/사망자 차트`
            },
            scales: {
                yAxes: [
                    {
                        id: 'yConfirmed',  // 왼쪽 Y축 (확진자)
                        position: 'left',
                        ticks: {
                            beginAtZero: true,
                            callback: function(value) { return value.toLocaleString(); }  // 숫자 형식
                        },
                        scaleLabel: {
                            display: true,
                            labelString: '확진자 수'
                        },
                        gridLines: {
                            display: false  // y축 그리드 제거
                        }
                    },
                    {
                        id: 'yDeaths',  // 오른쪽 Y축 (사망자)
                        position: 'right',
                        ticks: {
                            beginAtZero: true,
                            callback: function(value) { return value.toLocaleString(); }  // 숫자 형식
                        },
                        scaleLabel: {
                            display: true,
                            labelString: '사망자 수'
                        },
                        gridLines: {
                            display: false  // y축 그리드 제거
                        }
                    }
                ],
                xAxes: [{
                    ticks: {
                        autoSkip: false,  // 도시 이름이 잘리지 않도록 설정
                    },
                    gridLines: {
                        display: false  // x축 그리드 제거
                    }
                }]
            }
        }
    });
}

// 차트 데이터를 활용해 차트 생성
function renderRegionCharts() {
    const { regionCityConfirmed, regionCityDeaths } = getChartData();

    // 권역별 차트 생성 (수도권, 충청권, 영남권, 호남권)
    createBarChart(
        document.getElementById('seoulRegionChart').getContext('2d'),
        Object.keys(regionCityConfirmed['수도권']),
        Object.values(regionCityConfirmed['수도권']),
        Object.values(regionCityDeaths['수도권']),
        '수도권'
    );

    createBarChart(
        document.getElementById('chungcheongRegionChart').getContext('2d'),
        Object.keys(regionCityConfirmed['충청권']),
        Object.values(regionCityConfirmed['충청권']),
        Object.values(regionCityDeaths['충청권']),
        '충청권'
    );

    createBarChart(
        document.getElementById('yeongnamRegionChart').getContext('2d'),
        Object.keys(regionCityConfirmed['영남권']),
        Object.values(regionCityConfirmed['영남권']),
        Object.values(regionCityDeaths['영남권']),
        '영남권'
    );

    createBarChart(
        document.getElementById('honamRegionChart').getContext('2d'),
        Object.keys(regionCityConfirmed['호남권']),
        Object.values(regionCityConfirmed['호남권']),
        Object.values(regionCityDeaths['호남권']),
        '호남권'
    );
}

// 페이지가 로드되면 차트 렌더링
document.addEventListener('DOMContentLoaded', function () {
    renderRegionCharts();
});
