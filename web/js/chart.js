var labels = [
    '一月',
    '二月',
    '三月',
    '四月',
    '五月',
    '六月',
];

var data = {
    labels: labels,
    datasets: [{
        label: '销售图表',
        backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgb(255, 99, 132)',
        data: [0, 10, 5, 2, 20, 30, 45],
    }]
};

var config = {
    type: 'line',
    data,
    options: {}
};

document.querySelectorAll(".myChart").forEach(element => {
    new Chart(element, config);
});