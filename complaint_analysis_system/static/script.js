// BAR CHART — Complaints by Category

var bar = document.getElementById("barChart");

if (bar) {

    new Chart(bar, {
        type: "bar",

        data: {

            labels: [
                "Billing",
                "Delivery",
                "Product",
                "Service",
                "Refund",
                "Technical"
            ],

            datasets: [

                {
                    label: "Complaints",

                    data: [
                        12,
                        19,
                        8,
                        5,
                        14,
                        9
                    ]
                }

            ]
        }

    });

}


// PIE CHART — Sentiment

var pie = document.getElementById("pieChart");

if (pie) {

    new Chart(pie, {
        type: "pie",

        data: {

            labels: [
                "Positive",
                "Negative",
                "Neutral"
            ],

            datasets: [

                {
                    data: [
                        25,
                        55,
                        20
                    ]
                }

            ]
        }

    });

}


// LINE CHART — Monthly Trend

var line = document.getElementById("lineChart");

if (line) {

    new Chart(line, {
        type: "line",

        data: {

            labels: [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun"
            ],

            datasets: [

                {
                    label: "Monthly Complaints",

                    data: [
                        5,
                        10,
                        7,
                        12,
                        9,
                        15
                    ]
                }

            ]
        }

    });

}