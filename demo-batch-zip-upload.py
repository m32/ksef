#!/usr/bin/env vpython3
import os
import sys
import getopt
import logging
import logging.config
import configparser


logging.basicConfig(level=logging.INFO)
with open("logging.ini", "rt") as fp:
    ini = configparser.ConfigParser()
    ini.read_file(fp)
    logging.config.fileConfig(ini)

from ksef.batch import Client, AuthenticatedClient, models, types, errors, api

class KSEFError(Exception):
    def __init__(self, rc, parsed):
        self.rc = rc
        self.parsed = parsed
        try:
            errors = parsed.exception.exception_detail_list
            krc = errors[0].exception_code
            kmsg = errors[0].exception_description
        except:
            krc = -1
            kmsg = 'unparsable'
            import traceback; traceback.print_exc()
        self.krc = krc
        self.kmsg = kmsg

    def __str__(self):
        return 'KSEFError: rc={} msg={}'.format(self.krc, self.kmsg)

    __repr__ = __str__

class Main:
    def __init__(self, server, user):
        self.server = server
        self.user = user
        self.config = configparser.ConfigParser()
        self.config.read('ksef.ini')

        self.headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
        }
        self.client = Client(
            base_url=self.config.get(server, 'api'),
            headers=self.headers
        )

    def upload(self, filexml):
        data = open('{}.xades'.format(filexml), 'rb').read()
        content = types.Content(data)
        response = api.wysylka.init.sync_detailed(
            client=self.client,
            content=content
        )
        if response.status_code != 201:
            raise KSEFError(response.status_code, response.parsed)
        parsed = response.parsed
        #{
        #    "timestamp":"2023-11-11T22:18:59.328Z",
        #    "referenceNumber":"20231111-SE-50B1D5640C-E17B10C97B-06",
        #    "packageSignature":{
        #        "packageName":"ksefbatch.zip",
        #        "packagePartSignatureList":[
        #            {
        #                "ordinalNumber":1,
        #                "partFileName":"ksefbatch.zip-enc-1",
        #                "url":"https://ksef-demo.mf.gov.pl/api/batch/Upload/20231111-SE-50B1D5640C-E17B10C97B-06/20231111-EA-BDC53F0706-1E048BFE7E-9F",
        #                "method":"PUT",
        #                "headerEntryList":[
        #                    {"key":"Content-SHA256","value":"x2Ulp6LIn9SfkX573Gkmjmm6WZ/joaOoKWX2k/zFdA8="},
        #                    {"key":"X-TargetSrv-Name","value":"srvTRMFB"}
        #                ]
        #            },
        #            {"ordinalNumber":2,"partFileName":"ksefbatch.zip-enc-2","url":"https://ksef-demo.mf.gov.pl/api/batch/Upload/20231111-SE-50B1D5640C-E17B10C97B-06/20231111-EA-A30E8FA156-51154DF91B-B2","method":"PUT","headerEntryList":[{"key":"Content-SHA256","value":"Qf0JIvDcv5pvdy7CvIP80x0Gndl3uHCLLr3LPQmEY7A="},{"key":"X-TargetSrv-Name","value":"srvTRMFB"}]},
        #            {"ordinalNumber":3,"partFileName":"ksefbatch.zip-enc-3","url":"https://ksef-demo.mf.gov.pl/api/batch/Upload/20231111-SE-50B1D5640C-E17B10C97B-06/20231111-EA-69EB6058C1-84544ADF3F-EF","method":"PUT","headerEntryList":[{"key":"Content-SHA256","value":"zEczZK6kXVGJBIZ1OxHbeC6IMOIlEnQ932LLk7N8HKM="},{"key":"X-TargetSrv-Name","value":"srvTRMFB"}]},
        #            {"ordinalNumber":4,"partFileName":"ksefbatch.zip-enc-4","url":"https://ksef-demo.mf.gov.pl/api/batch/Upload/20231111-SE-50B1D5640C-E17B10C97B-06/20231111-EA-09DA3245BD-11B2D53153-B1","method":"PUT","headerEntryList":[{"key":"Content-SHA256","value":"dJQPeVthNcj0whg5Hcthgn++JZ9uKnHmA5QjmXxNoWQ="},{"key":"X-TargetSrv-Name","value":"srvTRMFB"}]}
        #        ]
        #    }
        #}

        for pkg in parsed.package_signature.package_part_signature_list:
            data = open(pkg.part_file_name, 'rb').read()
            content = types.Content(data)
            headers = {}
            for hdr in pkg.header_entry_list:
                headers[hdr.key] = hdr.value
            response = api.wysylka.upload.sync_detailed(
                client=self.client,
                reference_number=parsed.reference_number,
                part_name=pkg.url.split('/')[-1],
                content=content,
                headers=headers,
            )
            # TODO - dlaczego 200 jak w dokumentacji jest 201 ?
            if response.status_code != 200:
                raise KSEFError(response.status_code, response.parsed)

        json_body = models.FinishRequest(
            reference_number=parsed.reference_number,
        )
        response = api.wysylka.finish.sync_detailed(
            client=self.client,
            json_body=json_body,
        )
        if response.status_code != 200:
            raise KSEFError(response.status_code, response.parsed)

        with open('upo-{}.csv'.format(self.user), 'at') as fp:
            fp.write('{}|{}\n'.format(
                parsed.reference_number, ''
            ))

def main():
    server = 'ksef-demo'
    user = 'user'
    opts, args = getopt.getopt(sys.argv[1:], '', [
        'server=',
        'user=',
    ])
    for o, a in opts:
        if o == '--server':
            server = a
        elif o == '--user':
            user = a
    cls = Main(server, user)
    try:
        cls.upload(args[0])
    except EOFError as e:
        print(e)

main()
