#!/usr/bin/env vpython3
response = b'''{"timestamp":"2023-10-17T13:13:25.855Z","referenceNumber":"20231017-SE-E3F263BDDE-71CFFB64BA-0D","sessionToken":\
{"token":"d19b294b2b394b326158fd78ce786f292e2a4b887093f95fdade2ac82e11dcbd","context":{"contextIdentifier":{"type":"onip","identifier":"111\
1111111"},"contextName":{"fullName":"CN_1111111111"},"credentialsRoleList":[{"type":"token","roleType":"invoice_read","roleDescription":"m3\
2pl","startTimestamp":"2023-10-17T11:38:35.086Z"},{"type":"token","roleType":"invoice_write","roleDescription":"m32pl","startTimestamp":"20\
23-10-17T11:38:35.086Z"},{"type":"granted","roleType":"self_invoicing","roleDescription":"testowy samofakturuj\xc4\x85cy CN1 firmy CN7","st\
artTimestamp":"2021-12-13T03:19:50.288Z","roleGrantorIdentifier":{"type":"onip","identifier":"7777777777"}},{"type":"granted","roleType":"s\
elf_invoicing","roleDescription":"enova365 Wersja Demonstracyjna","startTimestamp":"2023-04-13T08:22:07.910Z","roleGrantorIdentifier":{"typ\
e":"onip","identifier":"9570981264"}},{"type":"granted","roleType":"self_invoicing","roleDescription":"abcdef","startTimestamp":"2022-06-09\
T09:21:33.041Z","roleGrantorIdentifier":{"type":"onip","identifier":"1111111113"}},{"type":"granted","roleType":"tax_representative","roleD\
escription":"jedynki biurem dw\xc3\xb3jek","startTimestamp":"2022-08-24T12:46:19.435Z","roleGrantorIdentifier":{"type":"onip","identifier":\
"2222222222"}},{"type":"granted","roleType":"self_invoicing","roleDescription":"sprawdzanieNadania","startTimestamp":"2022-07-27T08:27:18.6\
90Z","roleGrantorIdentifier":{"type":"onip","identifier":"8232003298"}},{"type":"granted","roleType":"self_invoicing","roleDescription":"mm\
, mo","startTimestamp":"2022-11-30T11:21:14.858Z","roleGrantorIdentifier":{"type":"onip","identifier":"8132775328"}},{"type":"granted","rol\
eType":"self_invoicing","roleDescription":"qweasd","startTimestamp":"2022-08-23T10:16:25.178Z","roleGrantorIdentifier":{"type":"onip","iden\
tifier":"5272669657"}},{"type":"granted","roleType":"self_invoicing","roleDescription":"XXX sp. z o.o.","startTimestamp":"2023-08-11T15:13:\
19.613Z","roleGrantorIdentifier":{"type":"onip","identifier":"9999999999"}},{"type":"granted","roleType":"self_invoicing","roleDescription"\
:"aaaaaa","startTimestamp":"2023-01-26T12:19:49.838Z","roleGrantorIdentifier":{"type":"onip","identifier":"1163601488"}},{"type":"granted",\
"roleType":"self_invoicing","roleDescription":"APIK SP. Z O.O.","startTimestamp":"2022-10-21T12:32:55.142Z","roleGrantorIdentifier":{"type"\
:"onip","identifier":"6442996318"}},{"type":"granted","roleType":"self_invoicing","roleDescription":"gazsystem","startTimestamp":"2022-12-0\
1T10:30:00.435Z","roleGrantorIdentifier":{"type":"onip","identifier":"4444444444"}},{"type":"granted","roleType":"self_invoicing","roleDesc\
ription":"Samofakturowanie Wysylka","startTimestamp":"2023-02-24T11:23:06.704Z","roleGrantorIdentifier":{"type":"onip","identifier":"453909\
2841"}},{"type":"granted","roleType":"tax_representative","roleDescription":"Biuro Sp. z o.o.","startTimestamp":"2023-03-28T14:45:49.572Z",\
"roleGrantorIdentifier":{"type":"onip","identifier":"5272767250"}},{"type":"granted","roleType":"tax_representative","roleDescription":"Tes\
t Ma\xc5\x82opolski","startTimestamp":"2023-09-12T09:54:00.866Z","roleGrantorIdentifier":{"type":"onip","identifier":"3795195859"}},{"type"\
:"granted","roleType":"self_invoicing","roleDescription":"asdadsasda","startTimestamp":"2023-09-04T09:24:25.912Z","roleGrantorIdentifier":{\
"type":"onip","identifier":"5331310470"}},{"type":"granted","roleType":"self_invoicing","roleDescription":"test1","startTimestamp":"2023-09\
-22T13:58:45.779Z","roleGrantorIdentifier":{"type":"onip","identifier":"7010390331"}},{"type":"granted","roleType":"tax_representative","ro\
leDescription":"TEST1","startTimestamp":"2023-09-22T13:59:09.116Z","roleGrantorIdentifier":{"type":"onip","identifier":"7010390331"}},{"typ\
e":"granted","roleType":"tax_representative","roleDescription":"qwe44","startTimestamp":"2023-09-28T08:43:15.633Z","roleGrantorIdentifier":\
{"type":"onip","identifier":"9999999999"}},{"type":"granted","roleType":"self_invoicing","roleDescription":"abcde","startTimestamp":"2023-0\
9-13T14:53:48.891Z","roleGrantorIdentifier":{"type":"onip","identifier":"2222222222"}},{"type":"granted","roleType":"self_invoicing","roleD\
escription":"TestTest","startTimestamp":"2023-05-17T11:33:52.880Z","roleGrantorIdentifier":{"type":"onip","identifier":"8133132041"}},{"typ\
e":"granted","roleType":"self_invoicing","roleDescription":"teset","startTimestamp":"2023-09-13T08:46:00.585Z","roleGrantorIdentifier":{"ty\
pe":"onip","identifier":"5252800079"}},{"type":"granted","roleType":"self_invoicing","roleDescription":"przykladowy","startTimestamp":"2023\
-06-13T15:06:35.756Z","roleGrantorIdentifier":{"type":"onip","identifier":"1181477610"}},{"type":"granted","roleType":"self_invoicing","rol\
eDescription":"LS TEST sp. z o.o.","startTimestamp":"2023-06-27T09:41:39.966Z","roleGrantorIdentifier":{"type":"onip","identifier":"9450000\
157"}},{"type":"granted","roleType":"self_invoicing","roleDescription":"enova","startTimestamp":"2023-07-05T10:59:36.785Z","roleGrantorIden\
tifier":{"type":"onip","identifier":"9512417713"}},{"type":"granted","roleType":"self_invoicing","roleDescription":"aaaaaa","startTimestamp\
":"2023-10-15T20:03:03.510Z","roleGrantorIdentifier":{"type":"onip","identifier":"2222333223"}}]}}}'''
from ksef.online.api.sesja import init_token
from ksef.online.models.init_session_response import InitSessionResponse

import json
response = json.loads(response.decode())
response_201 = InitSessionResponse.from_dict(response)
