from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import Union
from typing import Optional
from ...models.session_status_response import SessionStatusResponse
from typing import Dict
from ...models.exception_response import ExceptionResponse
from typing import cast
from ...types import UNSET, Unset



def _get_kwargs(
    reference_number: str,
    *,
    page_size: Union[Unset, None, int] = 10,
    page_offset: Union[Unset, None, int] = 0,
    include_details: Union[Unset, None, bool] = True,

) -> Dict[str, Any]:
    

    cookies = {}


    params: Dict[str, Any] = {}
    params["PageSize"] = page_size


    params["PageOffset"] = page_offset


    params["IncludeDetails"] = include_details



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
        "method": "get",
        "url": "/online/Session/Status/{ReferenceNumber}".format(ReferenceNumber=reference_number,),
        "params": params,
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
    reference_number: str,
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, None, int] = 10,
    page_offset: Union[Unset, None, int] = 0,
    include_details: Union[Unset, None, bool] = True,

) -> Response[Union[ExceptionResponse, SessionStatusResponse]]:
    """ Sprawdzenie statusu sesji ogólnej

     Sprawdzenie statusu przetwarzania na podstawie numeru referencyjnego

    Args:
        reference_number (str):
        page_size (Union[Unset, None, int]):  Default: 10.
        page_offset (Union[Unset, None, int]):
        include_details (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, SessionStatusResponse]]
     """


    kwargs = _get_kwargs(
        reference_number=reference_number,
page_size=page_size,
page_offset=page_offset,
include_details=include_details,

    )

    print("*"*20, "/online/Session/Status/{ReferenceNumber}")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//online/Session/Status/{ReferenceNumber}")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    reference_number: str,
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, None, int] = 10,
    page_offset: Union[Unset, None, int] = 0,
    include_details: Union[Unset, None, bool] = True,

) -> Optional[Union[ExceptionResponse, SessionStatusResponse]]:
    """ Sprawdzenie statusu sesji ogólnej

     Sprawdzenie statusu przetwarzania na podstawie numeru referencyjnego

    Args:
        reference_number (str):
        page_size (Union[Unset, None, int]):  Default: 10.
        page_offset (Union[Unset, None, int]):
        include_details (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, SessionStatusResponse]
     """


    return sync_detailed(
        reference_number=reference_number,
client=client,
page_size=page_size,
page_offset=page_offset,
include_details=include_details,

    ).parsed

async def asyncio_detailed(
    reference_number: str,
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, None, int] = 10,
    page_offset: Union[Unset, None, int] = 0,
    include_details: Union[Unset, None, bool] = True,

) -> Response[Union[ExceptionResponse, SessionStatusResponse]]:
    """ Sprawdzenie statusu sesji ogólnej

     Sprawdzenie statusu przetwarzania na podstawie numeru referencyjnego

    Args:
        reference_number (str):
        page_size (Union[Unset, None, int]):  Default: 10.
        page_offset (Union[Unset, None, int]):
        include_details (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, SessionStatusResponse]]
     """


    kwargs = _get_kwargs(
        reference_number=reference_number,
page_size=page_size,
page_offset=page_offset,
include_details=include_details,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    reference_number: str,
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, None, int] = 10,
    page_offset: Union[Unset, None, int] = 0,
    include_details: Union[Unset, None, bool] = True,

) -> Optional[Union[ExceptionResponse, SessionStatusResponse]]:
    """ Sprawdzenie statusu sesji ogólnej

     Sprawdzenie statusu przetwarzania na podstawie numeru referencyjnego

    Args:
        reference_number (str):
        page_size (Union[Unset, None, int]):  Default: 10.
        page_offset (Union[Unset, None, int]):
        include_details (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, SessionStatusResponse]
     """


    return (await asyncio_detailed(
        reference_number=reference_number,
client=client,
page_size=page_size,
page_offset=page_offset,
include_details=include_details,

    )).parsed
