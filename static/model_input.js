function updateScore(){
  const user_string = document.getElementById('input').value;
  const recs = document.getElementById('output');

  var data = {
    'description': user_string,
  };

  $.ajax({
    type: 'POST',
    contentType: "application/json; charset=utf-8",
    url: '/predict',
    async: true,
    data: JSON.stringify({
      data : data
    }),
    success: (response) => {
      var rec_output = response
      recs.textContent = response.join("\n");
    },
    error: (response) => {
      outcome.textContent = 'Something went wrong. That sinking feeling :( ';
    }
  })
}
