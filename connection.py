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

from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode, String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class QuickBooksService(ServiceBase):
    @rpc(String, _returns=Iterable(String))
    def serverVersion(self, ticket):
        print('serverVersion()')
        print(ticket)
        return '1.0'


    @rpc(String, Integer, _returns=Iterable(Unicode))
    def authenticate(self, strUserName, strPassword):
        print('authenticate()')
        list = []
        results.append('{bcf30422-afd1-43ac-b3bc-a7482c504dda}')
        results.append('your_user')
        results.append('your_psswd')
        results.append('300')

        print(strUserName)
        print(strPassword)
        print(list)
        return list

    @rpc(Unicode, _returns=Iterable(Unicode))
    def clientVersion(self, strVersion):
        print('clientVersion()')
        print(strVersion)
        return '2.2.0.93'

    @rpc(Unicode, _returns=Iterable(Unicode))
    def closeConnection(self, ticket):
        print('closeConnection()')
        print(ticket)
        return 'closeConnection() called on WS'

    @rpc(Unicode, Integer, Integer, _returns=Iterable(Unicode))
    def connectionError(self, ticket, hresult, message):
        print('connectionError')
        print(ticket)
        print(hresult)
        print(message)
        return 'done'

    @rpc(Unicode, _returns=Iterable(Unicode))
    def getLastError(self, ticket):
        print('lastError()')
        print(ticket)
        return 'Problems foo bar'

    @rpc(Unicode, Integer, Integer, Integer, _returns=Iterable(Unicode))
    def receiveResponseXML(self, ticket, response, hresult, message):
        print('receiveResponseXML()')
        print("ticket=" + ticket)
        print("response=" + response)
        if hresult:
            print("hresult=" + hresult)
            print("message=" + message)
        return 100

    @rpc(Unicode, Integer, Integer, Integer, Integer, Integer, _returns=Iterable(Unicode))
    def sendRequestXML(self, ticket, strHCPResponse, strCompanyFileName, qbXMLCountry, qbXMLMajorVers, qbXMLMinorVers):
        print('sendRequestXML()')
        print(strHCPResponse)
        xml = "<?xml version=\"1.0\" ?>" + \
              "<?qbxml version=\"2.0\"?>" + \
              "<QBXML>" + \
              "<QBXMLMsgsRq onError=\"stopOnError\">" + \
              "<ItemQueryRq></ItemQueryRq>" + \
              "</QBXMLMsgsRq>" + \
              "</QBXML>"
        return xml

    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def interactiveUrl(self, ticket, sessionID):
        print('interactiveUrl')
        print(ticket)
        print(sessionID)
        return 'http://localhost/test'

    @rpc(Unicode, _returns=Iterable(Unicode))
    def interactiveDone(self, ticket):
        print('interactiveDone()')
        print(ticket)
        return 'Done'

    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def interactiveRejected(self, ticket, reason):
        print('interactiveRejected()')
        print(ticket)
        print(reason)
        return 'Message to show'


application = Application([QuickBooksService], 'projetoQB.appConexao.connection.QuickBooksService',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()