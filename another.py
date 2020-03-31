import mitmproxy
from mitmproxy.models import HTTPResponse
from netlib.http import Headers

def response(flow):
    flow.response.headers["newheader"] = "foo"
    print("YES")
