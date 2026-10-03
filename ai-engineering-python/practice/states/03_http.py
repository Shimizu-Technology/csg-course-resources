import io
import json
from urllib.request import Request

def send_supply(value, transport):
    request = Request('https://practice.invalid/supplies', data=json.dumps(value).encode(), headers={'Content-Type':'application/json'})
    with transport(request, timeout=5) as response:
        return json.loads(response.read(1025))

def fake_transport(request, timeout):
    assert request.get_method() == 'POST'
    assert timeout == 5
    assert json.loads(request.data) == {'item':'paper','quantity':3}
    return io.BytesIO(b'{"accepted":true}')

print('MOCK TRANSPORT — NO NETWORK')
print(send_supply({'item':'paper','quantity':3}, fake_transport))
