from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from ...models.revoke_certificate_request import RevokeCertificateRequest
from typing import cast



def _get_kwargs(
    certificate_serial_number: str,
    *,
    body: RevokeCertificateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/certificates/{certificate_serial_number}/revoke".format(certificate_serial_number=certificate_serial_number,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    certificate_serial_number: str,
    *,
    client: AuthenticatedClient,
    body: RevokeCertificateRequest,

) -> Response[Union[Any, ExceptionResponse]]:
    """ Unieważnienie certyfikatu

     Unieważnia certyfikat o podanym numerze seryjnym.

    Args:
        certificate_serial_number (str):
        body (RevokeCertificateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse]]
     """


    kwargs = _get_kwargs(
        certificate_serial_number=certificate_serial_number,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    certificate_serial_number: str,
    *,
    client: AuthenticatedClient,
    body: RevokeCertificateRequest,

) -> Optional[Union[Any, ExceptionResponse]]:
    """ Unieważnienie certyfikatu

     Unieważnia certyfikat o podanym numerze seryjnym.

    Args:
        certificate_serial_number (str):
        body (RevokeCertificateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse]
     """


    return sync_detailed(
        certificate_serial_number=certificate_serial_number,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    certificate_serial_number: str,
    *,
    client: AuthenticatedClient,
    body: RevokeCertificateRequest,

) -> Response[Union[Any, ExceptionResponse]]:
    """ Unieważnienie certyfikatu

     Unieważnia certyfikat o podanym numerze seryjnym.

    Args:
        certificate_serial_number (str):
        body (RevokeCertificateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse]]
     """


    kwargs = _get_kwargs(
        certificate_serial_number=certificate_serial_number,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    certificate_serial_number: str,
    *,
    client: AuthenticatedClient,
    body: RevokeCertificateRequest,

) -> Optional[Union[Any, ExceptionResponse]]:
    """ Unieważnienie certyfikatu

     Unieważnia certyfikat o podanym numerze seryjnym.

    Args:
        certificate_serial_number (str):
        body (RevokeCertificateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse]
     """


    return (await asyncio_detailed(
        certificate_serial_number=certificate_serial_number,
client=client,
body=body,

    )).parsed
