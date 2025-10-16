from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.authentication_init_response import AuthenticationInitResponse
from ...models.exception_response import ExceptionResponse
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    body: str,
    verify_certificate_chain: Union[Unset, bool] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["verifyCertificateChain"] = verify_certificate_chain


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/auth/xades-signature",
        "params": params,
    }

    _kwargs["content"] = body.payload

    headers["Content-Type"] = "application/xml"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[AuthenticationInitResponse, ExceptionResponse]]:
    if response.status_code == 202:
        response_202 = AuthenticationInitResponse.from_dict(response.json())



        return response_202

    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[AuthenticationInitResponse, ExceptionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: str,
    verify_certificate_chain: Union[Unset, bool] = UNSET,

) -> Response[Union[AuthenticationInitResponse, ExceptionResponse]]:
    """ Uwierzytelnienie z wykorzystaniem podpisu XAdES

     Rozpoczyna operację uwierzytelniania za pomocą dokumentu XML podpisanego podpisem elektronicznym
    XAdES.

    > Więcej informacji:
    > - [Przygotowanie dokumentu XML](https://github.com/CIRFMF/ksef-
    docs/blob/main/uwierzytelnianie.md#1-przygotowanie-dokumentu-xml-authtokenrequest)
    > - [Podpis dokumentu XML](https://github.com/CIRFMF/ksef-
    docs/blob/main/uwierzytelnianie.md#2-podpisanie-dokumentu-xades)
    > - [Schemat XSD](/docs/v2/schemas/authv2.xsd)

    Args:
        verify_certificate_chain (Union[Unset, bool]):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthenticationInitResponse, ExceptionResponse]]
     """


    kwargs = _get_kwargs(
        body=body,
verify_certificate_chain=verify_certificate_chain,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: str,
    verify_certificate_chain: Union[Unset, bool] = UNSET,

) -> Optional[Union[AuthenticationInitResponse, ExceptionResponse]]:
    """ Uwierzytelnienie z wykorzystaniem podpisu XAdES

     Rozpoczyna operację uwierzytelniania za pomocą dokumentu XML podpisanego podpisem elektronicznym
    XAdES.

    > Więcej informacji:
    > - [Przygotowanie dokumentu XML](https://github.com/CIRFMF/ksef-
    docs/blob/main/uwierzytelnianie.md#1-przygotowanie-dokumentu-xml-authtokenrequest)
    > - [Podpis dokumentu XML](https://github.com/CIRFMF/ksef-
    docs/blob/main/uwierzytelnianie.md#2-podpisanie-dokumentu-xades)
    > - [Schemat XSD](/docs/v2/schemas/authv2.xsd)

    Args:
        verify_certificate_chain (Union[Unset, bool]):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AuthenticationInitResponse, ExceptionResponse]
     """


    return sync_detailed(
        client=client,
body=body,
verify_certificate_chain=verify_certificate_chain,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: str,
    verify_certificate_chain: Union[Unset, bool] = UNSET,

) -> Response[Union[AuthenticationInitResponse, ExceptionResponse]]:
    """ Uwierzytelnienie z wykorzystaniem podpisu XAdES

     Rozpoczyna operację uwierzytelniania za pomocą dokumentu XML podpisanego podpisem elektronicznym
    XAdES.

    > Więcej informacji:
    > - [Przygotowanie dokumentu XML](https://github.com/CIRFMF/ksef-
    docs/blob/main/uwierzytelnianie.md#1-przygotowanie-dokumentu-xml-authtokenrequest)
    > - [Podpis dokumentu XML](https://github.com/CIRFMF/ksef-
    docs/blob/main/uwierzytelnianie.md#2-podpisanie-dokumentu-xades)
    > - [Schemat XSD](/docs/v2/schemas/authv2.xsd)

    Args:
        verify_certificate_chain (Union[Unset, bool]):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthenticationInitResponse, ExceptionResponse]]
     """


    kwargs = _get_kwargs(
        body=body,
verify_certificate_chain=verify_certificate_chain,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: str,
    verify_certificate_chain: Union[Unset, bool] = UNSET,

) -> Optional[Union[AuthenticationInitResponse, ExceptionResponse]]:
    """ Uwierzytelnienie z wykorzystaniem podpisu XAdES

     Rozpoczyna operację uwierzytelniania za pomocą dokumentu XML podpisanego podpisem elektronicznym
    XAdES.

    > Więcej informacji:
    > - [Przygotowanie dokumentu XML](https://github.com/CIRFMF/ksef-
    docs/blob/main/uwierzytelnianie.md#1-przygotowanie-dokumentu-xml-authtokenrequest)
    > - [Podpis dokumentu XML](https://github.com/CIRFMF/ksef-
    docs/blob/main/uwierzytelnianie.md#2-podpisanie-dokumentu-xades)
    > - [Schemat XSD](/docs/v2/schemas/authv2.xsd)

    Args:
        verify_certificate_chain (Union[Unset, bool]):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AuthenticationInitResponse, ExceptionResponse]
     """


    return (await asyncio_detailed(
        client=client,
body=body,
verify_certificate_chain=verify_certificate_chain,

    )).parsed
