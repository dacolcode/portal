// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable( {
    } );
  $('#dataTableCategorias').DataTable( {
        "order": [[ 1, "desc" ]],
        "lengthMenu": [[-1, 10, 15, 20], ["Todos", 10, 15, 20]]
    } );
});
