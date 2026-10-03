"""HTTP/JSON/testing prerequisite check. MOCK transport; never opens a socket."""
import io
import json
import unittest
from urllib.request import Request

def parse_ack(raw):
    value=json.loads(raw)
    if not isinstance(value,dict) or set(value)!={'accepted'} or type(value['accepted']) is not bool:
        raise ValueError('Expected exactly one boolean accepted field')
    return value

def submit_supply(value,transport):
    request=Request('https://practice.invalid/supplies',data=json.dumps(value).encode(),headers={'Content-Type':'application/json'})
    with transport(request,timeout=5) as response:
        raw=response.read(1025)
        if len(raw)>1024:raise ValueError('Response too large')
    return parse_ack(raw)

class BridgeTest(unittest.TestCase):
    def test_mock_post(self):
        def send(request,timeout):
            self.assertEqual(request.get_method(),'POST');self.assertEqual(timeout,5)
            self.assertEqual(json.loads(request.data),{'item':'paper','quantity':3})
            return io.BytesIO(b'{"accepted":true}')
        self.assertEqual(submit_supply({'item':'paper','quantity':3},send),{'accepted':True})
    def test_untrusted_response(self):
        for raw in (b'[]',b'{"accepted":"true"}',b'{"accepted":true,"execute":"something"}',b'broken'):
            with self.subTest(raw=raw),self.assertRaises(ValueError):parse_ack(raw)
    def test_body_bound_and_timeout(self):
        with self.assertRaises(ValueError):submit_supply({},lambda *a,**k:io.BytesIO(b' '*1025))
        def timeout(*a,**k):raise TimeoutError('fixture timeout')
        with self.assertRaises(TimeoutError):submit_supply({},timeout)

if __name__=='__main__':unittest.main(verbosity=2)
