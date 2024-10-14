document.addEventListener("DOMContentLoaded", function () {
    var ctx = document.getElementById('genderPieChart').getContext('2d');
    var male = parseInt(document.getElementById('chart-data').dataset.male);
    var female = parseInt(document.getElementById('chart-data').dataset.female);

    var total = male + female;

    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['남성', '여성'],
            datasets: [{
                data: [male, female],
                backgroundColor: ['#36A2EB', '#FF6384'],
            }]
        },
        options: {
            plugins: {
                datalabels: {
                    formatter: (value, ctx) => {
                        let percentage = (value / total * 100).toFixed(2) + '%';
                        return value + ' (' + percentage + ')';  // 값과 비율을 동시에 표시
                    },
                    color: '#fff',
                    font: {
                        weight: 'bold',
                        size: 14
                    },
                    align: 'end',  // 텍스트를 그래프 영역에 맞게 위치
                    anchor: 'end'
                }
            }
        }
    });
});
