from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import Union
from typing import Optional
from typing import Dict
from ...types import UNSET, Unset
from typing import cast
from ...models.exception_response import ExceptionResponse
from ...models.session_status_response import SessionStatusResponse



def _get_kwargs(
    *,
    page_size: Union[Unset, None, int] = 10,
    page_offset: Union[Unset, None, int] = 0,
    include_details: Union[Unset, None, bool] = True,
    ksef_number_variant: Union[Unset, str] = UNSET,

) -> Dict[str, Any]:
    headers = {}
    if not isinstance(ksef_number_variant, Unset):
        headers["ksef-number-variant"] = ksef_number_variant



    cookies = {}


    params: Dict[str, Any] = {}
    params["PageSize"] = page_size


    params["PageOffset"] = page_offset


    params["IncludeDetails"] = include_details



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
        "method": "get",
        "url": "/online/Session/Status",
        "params": params,
        "headers": headers,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ExceptionResponse, SessionStatusResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SessionStatusResponse.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ExceptionResponse.from_dict(response.json())



        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ExceptionResponse, SessionStatusResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, None, int] = 10,
    page_offset: Union[Unset, None, int] = 0,
    include_details: Union[Unset, None, bool] = True,
    ksef_number_variant: Union[Unset, str] = UNSET,

) -> Response[Union[ExceptionResponse, SessionStatusResponse]]:
    """ Sprawdzenie statusu aktywnej sesji interaktywnej

     Sprawdzenie statusu obecnego przetwarzania interaktywnego

    Args:
        page_size (Union[Unset, None, int]):  Default: 10.
        page_offset (Union[Unset, None, int]):
        include_details (Union[Unset, None, bool]):  Default: True.
        ksef_number_variant (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, SessionStatusResponse]]
     """


    kwargs = _get_kwargs(
        page_size=page_size,
page_offset=page_offset,
include_details=include_details,
ksef_number_variant=ksef_number_variant,

    )

    print("*"*20, "/online/Session/Status")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//online/Session/Status")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, None, int] = 10,
    page_offset: Union[Unset, None, int] = 0,
    include_details: Union[Unset, None, bool] = True,
    ksef_number_variant: Union[Unset, str] = UNSET,

) -> Optional[Union[ExceptionResponse, SessionStatusResponse]]:
    """ Sprawdzenie statusu aktywnej sesji interaktywnej

     Sprawdzenie statusu obecnego przetwarzania interaktywnego

    Args:
        page_size (Union[Unset, None, int]):  Default: 10.
        page_offset (Union[Unset, None, int]):
        include_details (Union[Unset, None, bool]):  Default: True.
        ksef_number_variant (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, SessionStatusResponse]
     """


    return sync_detailed(
        client=client,
page_size=page_size,
page_offset=page_offset,
include_details=include_details,
ksef_number_variant=ksef_number_variant,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, None, int] = 10,
    page_offset: Union[Unset, None, int] = 0,
    include_details: Union[Unset, None, bool] = True,
    ksef_number_variant: Union[Unset, str] = UNSET,

) -> Response[Union[ExceptionResponse, SessionStatusResponse]]:
    """ Sprawdzenie statusu aktywnej sesji interaktywnej

     Sprawdzenie statusu obecnego przetwarzania interaktywnego

    Args:
        page_size (Union[Unset, None, int]):  Default: 10.
        page_offset (Union[Unset, None, int]):
        include_details (Union[Unset, None, bool]):  Default: True.
        ksef_number_variant (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, SessionStatusResponse]]
     """


    kwargs = _get_kwargs(
        page_size=page_size,
page_offset=page_offset,
include_details=include_details,
ksef_number_variant=ksef_number_variant,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, None, int] = 10,
    page_offset: Union[Unset, None, int] = 0,
    include_details: Union[Unset, None, bool] = True,
    ksef_number_variant: Union[Unset, str] = UNSET,

) -> Optional[Union[ExceptionResponse, SessionStatusResponse]]:
    """ Sprawdzenie statusu aktywnej sesji interaktywnej

     Sprawdzenie statusu obecnego przetwarzania interaktywnego

    Args:
        page_size (Union[Unset, None, int]):  Default: 10.
        page_offset (Union[Unset, None, int]):
        include_details (Union[Unset, None, bool]):  Default: True.
        ksef_number_variant (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, SessionStatusResponse]
     """


    return (await asyncio_detailed(
        client=client,
page_size=page_size,
page_offset=page_offset,
include_details=include_details,
ksef_number_variant=ksef_number_variant,

    )).parsed
