import json

from kivy.network.urlrequest import UrlRequest


class HttpClient:
    def get_pizzas(self, on_complete, on_error, on_failure):
        url = "https://belaudguillaume.pythonanywhere.com/api/GetPizzas"
        pizzas_dict = []

        def data_received(req, result):
            data = json.loads(result)
            for pizza in data:
                pizzas_dict.append(pizza['fields'])
            print("data_received")
            if on_complete:
                on_complete(pizzas_dict)

        def data_error(req, error):
            if on_error:
                on_error(str(error))

        def data_failure(req, failure):
            if on_failure:
                on_failure(str(req.resp_status))

        req = UrlRequest(url, on_success=data_received, on_error=data_error, on_failure=data_failure)