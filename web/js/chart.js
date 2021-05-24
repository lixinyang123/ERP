function randomColor() {
    let colors = ["red", "yellow", "blue", "green", "pink", "orange", "grey", "purple", "orangered"];
    let index = Math.round(Math.random() * (colors.length - 1));
    return colors[index];
}

async function showCharts() {
    let sales = (await (await fetch(api + "/sale/index?page=1")).json()).sales;
    let purchases = (await (await fetch(api + "/purchase/index?page=1")).json()).purchases;
    showMoney(sales, purchases);
    showProduct(sales);
    showUser(sales);
}

function getDates(sales, purchases) {
    let labels = [];
    sales.forEach(sale => {
        let time = sale.time.substring(0, 10);
        if(labels.indexOf(time) < 0)
            labels.push(time);
    });

    purchases.forEach(purchase => {
        let time = purchase.time.substring(0, 10);
        if(labels.indexOf(time) < 0)
            labels.push(time);
    });
    return labels.reverse();
}

function getPayment(purchaseOperations) {
    let payment = 0;
    purchaseOperations.forEach(operation => {
        payment += operation.product.price * operation.num;
    });
    return payment;
}

function getPurchaseData(purchases, labels) {
    purchases = purchases.reverse();
    let datas = [];
    for(let i=0; i<labels.length; i++)
        datas.push(0);
    
    for(let i=0; i<purchases.length; i++) {
        let purchase = purchases[i];
        let time = purchase.time.substring(0, 10);

        if(!purchase.state)
            continue;

        let index = labels.indexOf(time);
        if(index >= 0)
            datas[index] += getPayment(purchase.purchaseOperations);
    }

    return {
        label: "支出",
        backgroundColor: "green",
        borderColor: "green",
        data: datas,
    };
}

function getAmounted(checkOuts) {
    let amounted = 0;
    checkOuts.forEach(checkOut => {
        amounted += checkOut.amount;
    });
    return amounted;
}

function getSaleData(sales, labels) {
    sales = sales.reverse();
    let datas = [];
    for(let i=0; i<labels.length; i++)
        datas.push(0);

    for(let i=0; i<sales.length; i++) {
        let sale = sales[i];
        let time = sale.time.substring(0, 10);
        
        let index = labels.indexOf(time);
        if(index >= 0)
            datas[index] += getAmounted(sale.checkOuts);
    }

    return {
        label: "销售",
        backgroundColor: "red",
        borderColor: "red",
        data: datas,
    };
}

function showMoney(sales, purchases) {

    let dates = getDates(sales, purchases);

    let config = {
        type: "line",
        data: {
            labels: dates,
            datasets: [
                getPurchaseData(purchases, dates),
                getSaleData(sales, dates)
            ]
        }
    };

    new Chart(document.querySelector("#money"), config);
}

function showProduct(sales) {

    let labels = [];
    let datas = [];
    let backgroundColors = [];

    sales.forEach(sale => {
        
        for (let i = 0; i < sale.saleOperations.length; i++) {
            let operation = sale.saleOperations[i];
            let index = labels.indexOf(operation.product.name);

            if(index < 0) {
                labels.push(operation.product.name);
                datas.push(operation.num);
                backgroundColors.push(randomColor());
            }
            else {
                datas[index] += operation.num;
            }
        }

    });

    let config = {
        type: "doughnut",
        data: {
            labels: labels,
            datasets: [{
                label: "产品销售状况",
                data: datas,
                backgroundColor: backgroundColors,
                hoverOffset: 4
            }]
        },
    };

    new Chart(document.querySelector("#product"), config);
}

function showUser(sales) {

    let labels = [];
    let datas = [];
    let backgroundColors = [];

    for(let i=0; i<sales.length; i++) {
        let sale = sales[i];
        let index = labels.indexOf(sale.user.name);

        if(index < 0) {
            labels.push(sale.user.name);
            datas.push(getAmounted(sale.checkOuts));
            backgroundColors.push(randomColor());
        }
        else {
            datas[index] += getAmounted(sale.checkOuts);
        }
    }

    let config = {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "用户消费情况",
                data: datas,
                backgroundColor: backgroundColors,
                hoverOffset: 4
            }]
        },
    };

    new Chart(document.querySelector("#user"), config);
}

showCharts();