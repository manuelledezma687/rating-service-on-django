google.maps.event.addDomListener(window, 'load', initialize);

    function initialize() {

      var pick_up = document.getElementById('pick_up');

      var autocomplete = new google.maps.places.Autocomplete(pick_up);

      var destiny = document.getElementById('destiny');

      var autocomplete = new google.maps.places.Autocomplete(destiny);

}
