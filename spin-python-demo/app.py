from spin_http import Response


def handle_request(request):

    return Response(200,
                    {"content-type": "text/plain"},
                    bytes("Hello from the Python SDK", "utf-8"))
