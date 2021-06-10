import requests
import ipinfo
import json
import os
import time
import threading
import multiprocessing

class RequestsApi:

    def secuencial( ip ):
        try:
            print(ip)
            access_token = 'f6b1ac315300cc'
            handler = ipinfo.getHandler(access_token)
            details = handler.getDetails(ip)

            return details.all
        except:
            return False

    def paralelo( q, ips ):
        #print(ips)
        try:
            output = []
            access_token = 'f6b1ac315300cc'
            handler = ipinfo.getHandler(access_token)
            for ip in ips:
                #print(ip)
                details = handler.getDetails(ip)
                output.append(details.all)

            q.put( output )
            #return output
        except:
            return False


    @staticmethod
    def getIpInformationSecuencial( ips ):
        try:

            output = []
            access_token = 'f6b1ac315300cc'
            handler = ipinfo.getHandler(access_token)
            for ip in ips:
                #print(ip)
                details = handler.getDetails(ip)
                output.append(details.all)
            #
            #
            #ip_address = '181.199.123.174'
            #

            #


            return output
            #return True
        except:
            return False


    @staticmethod
    async def getIpInformationAsync( ips ):
        try:
            output = []
            access_token = 'f6b1ac315300cc'
            handler = ipinfo.getHandlerAsync(access_token)

            for ip in ips:
                details = await handler.getDetails(ip)
                output.append(details.all)

            return output
        except:
            return False
