#!/usr/bin/env python
# encoding: utf8
#
# Copyright © Burak Arslan <burak at arskom dot com dot tr>,
#             Arskom Ltd. http://www.arskom.com.tr
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#    2. Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#    3. Neither the name of the owner nor the names of its contributors may be
#       used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
from spyne.application import Application
from spyne.decorator import rpc
from spyne.protocol.soap import Soap11
from spyne.service import ServiceBase
from spyne.model.complex import Array, Unicode
from spyne.model.primitive import Integer, String
from spyne.server.django import DjangoApplication
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class Support:

    def get_support(self, request):
        html = "<html><body>Example of a supports page</body></html>"

        return HttpResponse(html)


class QuickBooksService(ServiceBase):

    @rpc(Unicode, Unicode, _returns=Array(Unicode))
    def authenticate(ctx, strUserName, strPassword):
        print('authenticate() has been called')
        results = []
        results.append('{57F3B9B1-86F1-4fcc-B1EE-566DE1813D20}')
        results.append('')
        results.append('')

        print(strUserName)
        print(strPassword)
        print(results)
        return results

    @rpc(Unicode, _returns=Unicode)
    def clientVersion(ctx, strVersion):
        print('clientVersion()')
        print(strVersion)
        return ""

    @rpc(Unicode, _returns=Unicode)
    def closeConnection(ctx, ticket):
        print('closeConnection()')
        print(ticket)
        return 'closeConnection() called on WS'

    @rpc(Unicode, Unicode, Unicode, _returns=Unicode)
    def connectionError(ctx, ticket, hresult, message):
        print('connectionError')
        print(ticket)
        print(hresult)
        print(message)
        return 'done'

    @rpc(Unicode, _returns=Unicode)
    def getLastError(ctx, ticket):
        print('lastError()')
        print(ticket)
        return 'Deu Ruim'

    @rpc(Unicode, Unicode, Unicode, Unicode, _returns=Integer)
    def receiveResponseXML(ctx, ticket, response, hresult, message):
        print('receiveResponseXML()')
        print("ticket=" + ticket)
        print("response=" + response)
        if hresult:
            print("hresult=" + hresult)
            print("message=" + message)
        return 100

    @rpc(Unicode, Unicode, Unicode, Unicode, Integer, Integer, _returns=String)
    def sendRequestXML(ctx, ticket, strHCPResponse, strCompanyFileName, qbXMLCountry, qbXMLMajorVers,
                       qbXMLMinorVers):
        print('sendRequestXML() has been called')

        xml = b'<?xml version=\'1.0\' encoding=\'UTF-8\'?>\n<?qbxml version="13.0"?><QBXML><QBXMLMsgsRq onError="continueOnError"><BillAddRq><BillAdd defMacro="MACROTYPE"><VendorRef><FullName></FullName></VendorRef><TxnDate>2019-07-01</TxnDate><RefNumber>14329256</RefNumber><Memo>786953421</Memo><ExpenseLineAdd><AccountRef></FullName></AccountRef><Amount>,10</Amount></ExpenseLineAdd></BillAdd></BillAddRq><BillAddRq><BillAdd><VendorRef><FullName></FullName></VendorRef><TxnDate>2019-07-01</TxnDate><RefNumber>14329256</RefNumber><Memo>786953421</Memo><ExpenseLineAdd><AccountRef><FullName></FullName></AccountRef><Amount>,10</Amount></ExpenseLineAdd></BillAdd></BillAddRq></QBXMLMsgsRq></QBXML>'

        xml2 = "<?xml version=\"1.0\"?>" + \
                "<?qbxml version=\"13.0\"?>" + \
                    "<QBXML>" + \
                        "<QBXMLMsgsRq onError=\"stopOnError\">" + \
                            "<InvoiceAddRq>" + \
                                "<InvoiceAdd>" + \
                                    "<CustomerRef>" + \
                                        "<FullName></FullName>" + \
                                    "</CustomerRef>" + \
                                    "<TxnDate>2019-06-30</TxnDate>" + \
                                    "<RefNumber></RefNumber>" + \
                                    "<InvoiceLineAdd defMacro=\"MACROTYPE\">" + \
                                        "<ItemRef>" + \
                                            "<FullName></FullName>" + \
                                        "</ItemRef>" + \
                                        "<Desc>123456789</Desc>" + \
                                        "<Amount>2</Amount>" + \
                                    "</InvoiceLineAdd>" + \
                                "</InvoiceAdd>" + \
                            "</InvoiceAddRq>" + \
                        "</QBXMLMsgsRq>" + \
                    "</QBXML>"

        return None

    @rpc(Unicode, Unicode, _returns=Unicode)
    def interactiveUrl(ctx, ticket, sessionID):
        print('interactiveUrl')
        print(ticket)
        print(sessionID)
        return 'http://localhost/test'

    @rpc(Unicode, _returns=Unicode)
    def interactiveDone(ctx, ticket):
        print('interactiveDone()')
        print(ticket)
        return 'Done'

    @rpc(Unicode, Unicode, _returns=Unicode)
    def interactiveRejected(ctx, ticket, reason):
        print('interactiveRejected()')
        print(ticket)
        print(reason)
        return 'Interactive mode rejected'


app = Application([QuickBooksService],
                  'http://developer.intuit.com/',
                  in_protocol=Soap11(validator='lxml'),
                  out_protocol=Soap11())

qb_service = csrf_exempt(DjangoApplication(app))