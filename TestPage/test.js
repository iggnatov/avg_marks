$(document).ready(function() {
    $("button").click(function(){
        console.log('Hello, World!');
        inputSpecValue = document.getElementById('inputSpec').value;
        inputMarkValue = document.getElementById('inputMark').value;
        console.log('inputSpecValue: ', inputSpecValue, 'inputMarkValue: ', inputMarkValue);

        $.ajax({
            url: 'http://194.58.111.243/avgs/api/avgs?spec_code=' + inputSpecValue + '&mark=' + inputMarkValue,
            method: 'get',              /* Метод запроса (post или get) */
            dataType: 'json',           /* Тип данных в ответе (xml, json, script, html). */
//            data: {text: 'Текст'},      /* Данные передаваемые в массиве */
            success: function(data){    /* функция которая будет выполнена после успешного запроса.  */
                console.log(data);     /* В переменной data содержится ответ от index.php. */
            }
        });
    })
})
