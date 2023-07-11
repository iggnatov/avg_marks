$.ajax({
    url: 'http://127.0.0.1:8000/avgs/api/avgs',         /* Куда отправить запрос */
    method: 'get',              /* Метод запроса (post или get) */
    dataType: 'json',           /* Тип данных в ответе (xml, json, script, html). */
    data: {text: 'Текст'},      /* Данные передаваемые в массиве */
    success: function(data){    /* функция которая будет выполнена после успешного запроса.  */
	     console.log(data);     /* В переменной data содержится ответ от index.php. */
    }
});