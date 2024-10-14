// 협회별 월별 관중수 데이터를 가져오는 함수
function getAssociationChartData() {
    const chartDataElement = document.getElementById('chart-data');
    const months = JSON.parse(chartDataElement.dataset.monthsAttendance); // 월 데이터 가져오기
    const monthlyAttendanceByAssociation = JSON.parse(chartDataElement.dataset.monthlyAttendanceByAssociation);

    // NaN 값을 0으로 변환
    for (let association in monthlyAttendanceByAssociation) {
        monthlyAttendanceByAssociation[association] = monthlyAttendanceByAssociation[association].map(value => {
            return isNaN(value) ? 0 : value;
        });
    }

    return { months, monthlyAttendanceByAssociation };
}

// 협회별 월별 관중수 차트를 생성하는 함수
function renderAssociationCharts() {
    const { months, monthlyAttendanceByAssociation } = getAssociationChartData();

    // 각 협회별로 차트를 생성
    const associations = ['KBL', 'WKBL', 'KBO', 'KLEAGUE', 'KOVO'];
    associations.forEach(association => {
        const ctx = document.getElementById(`${association}Chart`).getContext('2d');

        new Chart(ctx, {
            type: 'line',
            data: {
                labels: months, // x축에 월 데이터를 넣음
                datasets: [{
                    label: `${association} 관중수`,
                    data: monthlyAttendanceByAssociation[association],
                    borderColor: getRandomColor(),
                    fill: false
                }]
            },
            options: {
                responsive: true,
                title: {
                    display: true,
                    text: `${association} 월별 관중수`
                },
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
    });
}

// 랜덤 색상을 생성하는 함수
function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

// 페이지 로드 시 차트를 렌더링
document.addEventListener('DOMContentLoaded', function () {
    renderAssociationCharts();
});
