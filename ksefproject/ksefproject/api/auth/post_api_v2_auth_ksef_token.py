from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.authentication_init_response import AuthenticationInitResponse
from ...models.exception_response import ExceptionResponse
from ...models.init_token_authentication_request import InitTokenAuthenticationRequest
from typing import cast



def _get_kwargs(
    *,
    body: InitTokenAuthenticationRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/auth/ksef-token",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

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
    body: InitTokenAuthenticationRequest,

) -> Response[Union[AuthenticationInitResponse, ExceptionResponse]]:
    """ Uwierzytelnienie z wykorzystaniem tokena KSeF

     Rozpoczyna operację uwierzytelniania z wykorzystaniem wcześniej wygenerowanego tokena KSeF.

    Token KSeF wraz z timestampem ze wcześniej wygenerowanego challenge'a (w formacie
    ```token|timestamp```) powinien zostać zaszyfrowany dedykowanym do tego celu kluczem publicznym.
    - Timestamp powinien zostać przekazany jako **liczba milisekund od 1 stycznia 1970 roku (Unix
    timestamp)**.
    - Algorytm szyfrowania: **RSA-OAEP (z użyciem SHA-256 jako funkcji skrótu)**.

    Args:
        body (InitTokenAuthenticationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthenticationInitResponse, ExceptionResponse]]
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
    client: Union[AuthenticatedClient, Client],
    body: InitTokenAuthenticationRequest,

) -> Optional[Union[AuthenticationInitResponse, ExceptionResponse]]:
    """ Uwierzytelnienie z wykorzystaniem tokena KSeF

     Rozpoczyna operację uwierzytelniania z wykorzystaniem wcześniej wygenerowanego tokena KSeF.

    Token KSeF wraz z timestampem ze wcześniej wygenerowanego challenge'a (w formacie
    ```token|timestamp```) powinien zostać zaszyfrowany dedykowanym do tego celu kluczem publicznym.
    - Timestamp powinien zostać przekazany jako **liczba milisekund od 1 stycznia 1970 roku (Unix
    timestamp)**.
    - Algorytm szyfrowania: **RSA-OAEP (z użyciem SHA-256 jako funkcji skrótu)**.

    Args:
        body (InitTokenAuthenticationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AuthenticationInitResponse, ExceptionResponse]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: InitTokenAuthenticationRequest,

) -> Response[Union[AuthenticationInitResponse, ExceptionResponse]]:
    """ Uwierzytelnienie z wykorzystaniem tokena KSeF

     Rozpoczyna operację uwierzytelniania z wykorzystaniem wcześniej wygenerowanego tokena KSeF.

    Token KSeF wraz z timestampem ze wcześniej wygenerowanego challenge'a (w formacie
    ```token|timestamp```) powinien zostać zaszyfrowany dedykowanym do tego celu kluczem publicznym.
    - Timestamp powinien zostać przekazany jako **liczba milisekund od 1 stycznia 1970 roku (Unix
    timestamp)**.
    - Algorytm szyfrowania: **RSA-OAEP (z użyciem SHA-256 jako funkcji skrótu)**.

    Args:
        body (InitTokenAuthenticationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthenticationInitResponse, ExceptionResponse]]
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
    client: Union[AuthenticatedClient, Client],
    body: InitTokenAuthenticationRequest,

) -> Optional[Union[AuthenticationInitResponse, ExceptionResponse]]:
    """ Uwierzytelnienie z wykorzystaniem tokena KSeF

     Rozpoczyna operację uwierzytelniania z wykorzystaniem wcześniej wygenerowanego tokena KSeF.

    Token KSeF wraz z timestampem ze wcześniej wygenerowanego challenge'a (w formacie
    ```token|timestamp```) powinien zostać zaszyfrowany dedykowanym do tego celu kluczem publicznym.
    - Timestamp powinien zostać przekazany jako **liczba milisekund od 1 stycznia 1970 roku (Unix
    timestamp)**.
    - Algorytm szyfrowania: **RSA-OAEP (z użyciem SHA-256 jako funkcji skrótu)**.

    Args:
        body (InitTokenAuthenticationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AuthenticationInitResponse, ExceptionResponse]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
