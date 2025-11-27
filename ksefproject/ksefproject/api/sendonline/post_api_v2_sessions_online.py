from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from ...models.open_online_session_request import OpenOnlineSessionRequest
from ...models.open_online_session_response import OpenOnlineSessionResponse
from typing import cast



def _get_kwargs(
    *,
    body: OpenOnlineSessionRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/sessions/online",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, OpenOnlineSessionResponse]]:
    if response.status_code == 201:
        response_201 = OpenOnlineSessionResponse.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, OpenOnlineSessionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: OpenOnlineSessionRequest,

) -> Response[Union[Any, ExceptionResponse, OpenOnlineSessionResponse]]:
    """ Otwarcie sesji interaktywnej

     Otwiera sesję do wysyłki pojedynczych faktur. Należy przekazać schemat wysyłanych faktur oraz
    informacje o kluczu używanym do szyfrowania.

    > Więcej informacji:
    > - [Otwarcie sesji interaktywnej](https://github.com/CIRFMF/ksef-docs/blob/main/sesja-
    interaktywna.md#1-otwarcie-sesji)
    > - [Klucz publiczny Ministersta Finansów](/docs/v2/index.html#tag/Certyfikaty-klucza-publicznego)

    **Wymagane uprawnienia**: `InvoiceWrite`, `PefInvoiceWrite`.

    Args:
        body (OpenOnlineSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, OpenOnlineSessionResponse]]
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
    body: OpenOnlineSessionRequest,

) -> Optional[Union[Any, ExceptionResponse, OpenOnlineSessionResponse]]:
    """ Otwarcie sesji interaktywnej

     Otwiera sesję do wysyłki pojedynczych faktur. Należy przekazać schemat wysyłanych faktur oraz
    informacje o kluczu używanym do szyfrowania.

    > Więcej informacji:
    > - [Otwarcie sesji interaktywnej](https://github.com/CIRFMF/ksef-docs/blob/main/sesja-
    interaktywna.md#1-otwarcie-sesji)
    > - [Klucz publiczny Ministersta Finansów](/docs/v2/index.html#tag/Certyfikaty-klucza-publicznego)

    **Wymagane uprawnienia**: `InvoiceWrite`, `PefInvoiceWrite`.

    Args:
        body (OpenOnlineSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, OpenOnlineSessionResponse]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: OpenOnlineSessionRequest,

) -> Response[Union[Any, ExceptionResponse, OpenOnlineSessionResponse]]:
    """ Otwarcie sesji interaktywnej

     Otwiera sesję do wysyłki pojedynczych faktur. Należy przekazać schemat wysyłanych faktur oraz
    informacje o kluczu używanym do szyfrowania.

    > Więcej informacji:
    > - [Otwarcie sesji interaktywnej](https://github.com/CIRFMF/ksef-docs/blob/main/sesja-
    interaktywna.md#1-otwarcie-sesji)
    > - [Klucz publiczny Ministersta Finansów](/docs/v2/index.html#tag/Certyfikaty-klucza-publicznego)

    **Wymagane uprawnienia**: `InvoiceWrite`, `PefInvoiceWrite`.

    Args:
        body (OpenOnlineSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, OpenOnlineSessionResponse]]
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
    body: OpenOnlineSessionRequest,

) -> Optional[Union[Any, ExceptionResponse, OpenOnlineSessionResponse]]:
    """ Otwarcie sesji interaktywnej

     Otwiera sesję do wysyłki pojedynczych faktur. Należy przekazać schemat wysyłanych faktur oraz
    informacje o kluczu używanym do szyfrowania.

    > Więcej informacji:
    > - [Otwarcie sesji interaktywnej](https://github.com/CIRFMF/ksef-docs/blob/main/sesja-
    interaktywna.md#1-otwarcie-sesji)
    > - [Klucz publiczny Ministersta Finansów](/docs/v2/index.html#tag/Certyfikaty-klucza-publicznego)

    **Wymagane uprawnienia**: `InvoiceWrite`, `PefInvoiceWrite`.

    Args:
        body (OpenOnlineSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, OpenOnlineSessionResponse]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
