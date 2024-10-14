document.addEventListener("DOMContentLoaded", function () {
    var ctx = document.getElementById('ageLineChart').getContext('2d');
    
    // 차트 데이터를 가져옴
    var months = JSON.parse(document.getElementById('chart-data').dataset.months);
    var ageGroups = JSON.parse(document.getElementById('chart-data').dataset.ageGroups);

    // 연령 그룹별 데이터
    var datasets = Object.keys(ageGroups).map(function (ageGroup) {
        return {
            label: ageGroup + '세',
            data: ageGroups[ageGroup],
            fill: false,
            borderColor: getRandomColor(),
            tension: 0.1
        };
    });

    // 라인 차트 생성
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: months,  // 월별 레이블
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
            },
            legend: {
                display: true
            }
        }
    });

    // 랜덤 색상 생성 함수
    function getRandomColor() {
        var letters = '0123456789ABCDEF';
        var color = '#';
        for (var i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }
});
