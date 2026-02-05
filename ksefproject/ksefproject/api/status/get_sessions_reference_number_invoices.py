from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from ...models.session_invoices_response import SessionInvoicesResponse
from ...models.too_many_requests_response import TooManyRequestsResponse
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    reference_number: str,
    *,
    page_size: Union[Unset, int] = 10,
    x_continuation_token: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_continuation_token, Unset):
        headers["x-continuation-token"] = x_continuation_token



    

    params: dict[str, Any] = {}

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sessions/{reference_number}/invoices".format(reference_number=reference_number,),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, SessionInvoicesResponse, TooManyRequestsResponse]]:
    if response.status_code == 200:
        response_200 = SessionInvoicesResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 429:
        response_429 = TooManyRequestsResponse.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, SessionInvoicesResponse, TooManyRequestsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    reference_number: str,
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, int] = 10,
    x_continuation_token: Union[Unset, str] = UNSET,

) -> Response[Union[Any, ExceptionResponse, SessionInvoicesResponse, TooManyRequestsResponse]]:
    """ Pobranie faktur sesji

     Zwraca listę faktur przesłanych w sesji wraz z ich statusami, oraz informacje na temat ilości
    poprawnie i niepoprawnie przetworzonych faktur.

    **Wymagane uprawnienia**: `InvoiceWrite`, `Introspection`, `PefInvoiceWrite`,
    `EnforcementOperations`.

    Args:
        reference_number (str): Numer referencyjny.
        page_size (Union[Unset, int]):  Default: 10.
        x_continuation_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, SessionInvoicesResponse, TooManyRequestsResponse]]
     """


    kwargs = _get_kwargs(
        reference_number=reference_number,
page_size=page_size,
x_continuation_token=x_continuation_token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    reference_number: str,
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, int] = 10,
    x_continuation_token: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, ExceptionResponse, SessionInvoicesResponse, TooManyRequestsResponse]]:
    """ Pobranie faktur sesji

     Zwraca listę faktur przesłanych w sesji wraz z ich statusami, oraz informacje na temat ilości
    poprawnie i niepoprawnie przetworzonych faktur.

    **Wymagane uprawnienia**: `InvoiceWrite`, `Introspection`, `PefInvoiceWrite`,
    `EnforcementOperations`.

    Args:
        reference_number (str): Numer referencyjny.
        page_size (Union[Unset, int]):  Default: 10.
        x_continuation_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, SessionInvoicesResponse, TooManyRequestsResponse]
     """


    return sync_detailed(
        reference_number=reference_number,
client=client,
page_size=page_size,
x_continuation_token=x_continuation_token,

    ).parsed

async def asyncio_detailed(
    reference_number: str,
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, int] = 10,
    x_continuation_token: Union[Unset, str] = UNSET,

) -> Response[Union[Any, ExceptionResponse, SessionInvoicesResponse, TooManyRequestsResponse]]:
    """ Pobranie faktur sesji

     Zwraca listę faktur przesłanych w sesji wraz z ich statusami, oraz informacje na temat ilości
    poprawnie i niepoprawnie przetworzonych faktur.

    **Wymagane uprawnienia**: `InvoiceWrite`, `Introspection`, `PefInvoiceWrite`,
    `EnforcementOperations`.

    Args:
        reference_number (str): Numer referencyjny.
        page_size (Union[Unset, int]):  Default: 10.
        x_continuation_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, SessionInvoicesResponse, TooManyRequestsResponse]]
     """


    kwargs = _get_kwargs(
        reference_number=reference_number,
page_size=page_size,
x_continuation_token=x_continuation_token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    reference_number: str,
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, int] = 10,
    x_continuation_token: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, ExceptionResponse, SessionInvoicesResponse, TooManyRequestsResponse]]:
    """ Pobranie faktur sesji

     Zwraca listę faktur przesłanych w sesji wraz z ich statusami, oraz informacje na temat ilości
    poprawnie i niepoprawnie przetworzonych faktur.

    **Wymagane uprawnienia**: `InvoiceWrite`, `Introspection`, `PefInvoiceWrite`,
    `EnforcementOperations`.

    Args:
        reference_number (str): Numer referencyjny.
        page_size (Union[Unset, int]):  Default: 10.
        x_continuation_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, SessionInvoicesResponse, TooManyRequestsResponse]
     """


    return (await asyncio_detailed(
        reference_number=reference_number,
client=client,
page_size=page_size,
x_continuation_token=x_continuation_token,

    )).parsed
