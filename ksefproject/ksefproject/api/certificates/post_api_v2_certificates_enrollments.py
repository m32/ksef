from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.enroll_certificate_request import EnrollCertificateRequest
from ...models.enroll_certificate_response import EnrollCertificateResponse
from ...models.exception_response import ExceptionResponse
from typing import cast



def _get_kwargs(
    *,
    body: EnrollCertificateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/certificates/enrollments",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, EnrollCertificateResponse, ExceptionResponse]]:
    if response.status_code == 202:
        response_202 = EnrollCertificateResponse.from_dict(response.json())



        return response_202

    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, EnrollCertificateResponse, ExceptionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: EnrollCertificateRequest,

) -> Response[Union[Any, EnrollCertificateResponse, ExceptionResponse]]:
    """ Wysyłka wniosku certyfikacyjnego

     Przyjmuje wniosek certyfikacyjny i rozpoczyna jego przetwarzanie.

    Dozwolone typy kluczy prywatnych:
    - RSA (OID: 1.2.840.113549.1.1.1), długość klucza równa 2048 bitów,
    - EC (klucze oparte na krzywych eliptycznych, OID: 1.2.840.10045.2.1), krzywa NIST P-256 (secp256r1)

    Zalecane jest stosowanie kluczy EC.

    Dozwolone algorytmy podpisu:
    - RSA PKCS#1 v1.5,
    - RSA PSS,
    - ECDSA (format podpisu zgodny z RFC 3279)

    Dozwolone funkcje skrótu użyte do podpisu CSR:
    - SHA1,
    - SHA256,
    - SHA384,
    - SHA512

    > Więcej informacji:
    > - [Wysłanie wniosku certyfikacyjnego](https://github.com/CIRFMF/ksef-docs/blob/main/certyfikaty-
    KSeF.md#4-wys%C5%82anie-wniosku-certyfikacyjnego)

    Args:
        body (EnrollCertificateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EnrollCertificateResponse, ExceptionResponse]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: EnrollCertificateRequest,

) -> Optional[Union[Any, EnrollCertificateResponse, ExceptionResponse]]:
    """ Wysyłka wniosku certyfikacyjnego

     Przyjmuje wniosek certyfikacyjny i rozpoczyna jego przetwarzanie.

    Dozwolone typy kluczy prywatnych:
    - RSA (OID: 1.2.840.113549.1.1.1), długość klucza równa 2048 bitów,
    - EC (klucze oparte na krzywych eliptycznych, OID: 1.2.840.10045.2.1), krzywa NIST P-256 (secp256r1)

    Zalecane jest stosowanie kluczy EC.

    Dozwolone algorytmy podpisu:
    - RSA PKCS#1 v1.5,
    - RSA PSS,
    - ECDSA (format podpisu zgodny z RFC 3279)

    Dozwolone funkcje skrótu użyte do podpisu CSR:
    - SHA1,
    - SHA256,
    - SHA384,
    - SHA512

    > Więcej informacji:
    > - [Wysłanie wniosku certyfikacyjnego](https://github.com/CIRFMF/ksef-docs/blob/main/certyfikaty-
    KSeF.md#4-wys%C5%82anie-wniosku-certyfikacyjnego)

    Args:
        body (EnrollCertificateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EnrollCertificateResponse, ExceptionResponse]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: EnrollCertificateRequest,

) -> Response[Union[Any, EnrollCertificateResponse, ExceptionResponse]]:
    """ Wysyłka wniosku certyfikacyjnego

     Przyjmuje wniosek certyfikacyjny i rozpoczyna jego przetwarzanie.

    Dozwolone typy kluczy prywatnych:
    - RSA (OID: 1.2.840.113549.1.1.1), długość klucza równa 2048 bitów,
    - EC (klucze oparte na krzywych eliptycznych, OID: 1.2.840.10045.2.1), krzywa NIST P-256 (secp256r1)

    Zalecane jest stosowanie kluczy EC.

    Dozwolone algorytmy podpisu:
    - RSA PKCS#1 v1.5,
    - RSA PSS,
    - ECDSA (format podpisu zgodny z RFC 3279)

    Dozwolone funkcje skrótu użyte do podpisu CSR:
    - SHA1,
    - SHA256,
    - SHA384,
    - SHA512

    > Więcej informacji:
    > - [Wysłanie wniosku certyfikacyjnego](https://github.com/CIRFMF/ksef-docs/blob/main/certyfikaty-
    KSeF.md#4-wys%C5%82anie-wniosku-certyfikacyjnego)

    Args:
        body (EnrollCertificateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EnrollCertificateResponse, ExceptionResponse]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: EnrollCertificateRequest,

) -> Optional[Union[Any, EnrollCertificateResponse, ExceptionResponse]]:
    """ Wysyłka wniosku certyfikacyjnego

     Przyjmuje wniosek certyfikacyjny i rozpoczyna jego przetwarzanie.

    Dozwolone typy kluczy prywatnych:
    - RSA (OID: 1.2.840.113549.1.1.1), długość klucza równa 2048 bitów,
    - EC (klucze oparte na krzywych eliptycznych, OID: 1.2.840.10045.2.1), krzywa NIST P-256 (secp256r1)

    Zalecane jest stosowanie kluczy EC.

    Dozwolone algorytmy podpisu:
    - RSA PKCS#1 v1.5,
    - RSA PSS,
    - ECDSA (format podpisu zgodny z RFC 3279)

    Dozwolone funkcje skrótu użyte do podpisu CSR:
    - SHA1,
    - SHA256,
    - SHA384,
    - SHA512

    > Więcej informacji:
    > - [Wysłanie wniosku certyfikacyjnego](https://github.com/CIRFMF/ksef-docs/blob/main/certyfikaty-
    KSeF.md#4-wys%C5%82anie-wniosku-certyfikacyjnego)

    Args:
        body (EnrollCertificateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EnrollCertificateResponse, ExceptionResponse]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
