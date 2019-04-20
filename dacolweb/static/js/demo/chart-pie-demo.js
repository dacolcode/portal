// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

//paleta colores gráficos
var backgroundColorPaleta = ['#4e73df', '#36b9cc', '#76E8D5', '#1cc88a', '#78ff5b', '#A3FF8F', '#ffff80', '#E8DB76', '#f6c23e', '#FFC382','#E2C7FF', '#7158CC', '#FF7AB3'];
var hoverBackgroundColorPaleta = ['#2e59d9','#2e59d9','#2e59d9','#2e59d9','#2e59d9','#2e59d9','#2e59d9','#2e59d9','#2e59d9','#2e59d9','#2e59d9','#2e59d9'];

//ajustes para móviles
var mostrarLeyenda = true;
if ($(window).width() < 768) {
      mostrarLeyenda = false;
};

$.ajax({url: "/consultar_categorias", success: function(result){

    datos = result.categorias;
    console.log(datos);

    // Torta de categorias
    var ctx = document.getElementById("categorias");
    var myPieChart = new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: result.categorias,
        datasets: [{
          data: result.valores,
          backgroundColor: backgroundColorPaleta,
          hoverBackgroundColor: hoverBackgroundColorPaleta,
          hoverBorderColor: "rgba(234, 236, 244, 1)",
        }],
      },
      options: {
        maintainAspectRatio: false,
        tooltips: {
          backgroundColor: "rgb(255,255,255)",
          bodyFontColor: "#858796",
          borderColor: '#dddfeb',
          borderWidth: 1,
          xPadding: 15,
          yPadding: 15,
          displayColors: false,
          caretPadding: 10,
        },
        legend: {
          display: mostrarLeyenda,
          position: 'right'
        },
        cutoutPercentage: 20,
      },
    });


  }});

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Direct", "Referral", "Social"],
    datasets: [{
      data: [55, 30, 15],
      backgroundColor: backgroundColorPaleta,
      hoverBackgroundColor: hoverBackgroundColorPaleta,
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});
