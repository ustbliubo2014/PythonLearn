
from tornado.ioloop import IOLoop
from tornado.httpclient import HTTPRequest
from tornado.httpclient import AsyncHTTPClient
from tornado.httputil import HTTPHeaders
import base64
import re
AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")

#url = "http://cn.vuejs.org/js/vue.min.js"
url = "http://megaface.cs.washington.edu/dataset/download/content/MegaFace_dataset.zip"

fd = open("MegaFace_dataset.zip","w")

def handle_req(resp):
    print "----------in-----"
    print resp.code
    if resp.code<500:
        print resp.headers['Content-Range']
        g =re.search(r'.*?(\d+)-.*?',resp.headers['Content-Range'])
        seek = g.group(1)
        fd.seek(int(seek))
        fd.write(resp.body)
    print "--------end------"


def handle_request(resp):
    length = int(resp.headers['Content-Length'])
    size = length/10000
    req_args = []
    for i in range(0,length,size):
        if (i+size)<length:
            headers = HTTPHeaders({"Range":"bytes=%s-%s" % (i,i+size),"Connection":"Keep-Alive","Content-Type":"application/zip","User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)"})
        else:
            headers = HTTPHeaders({"Range":"bytes=%s-" % i,"Connection":"Keep-Alive","Content-Type":"application/zip","User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)"})
        req_args.append(headers)

    for i in req_args:
        req = HTTPRequest(url,method="GET",headers=i,auth_username='mousie.aries@gmail.com',auth_password='pL7qra|E74',connect_timeout =6000,request_timeout =6000)
        http_client.fetch(req,handle_req)

header= HTTPHeaders({"Content-Type":"application/zip","User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)"})
request = HTTPRequest(url=url,method="HEAD",headers=header,auth_username='mousie.aries@gmail.com',auth_password='pL7qra|E74')
http_client =  AsyncHTTPClient()
http_client.fetch(request,handle_request)
try:
    IOLoop.current().start()
except (KeyboardInterrupt, SystemExit):
    fd.close()
    IOLoop.current().stop()



