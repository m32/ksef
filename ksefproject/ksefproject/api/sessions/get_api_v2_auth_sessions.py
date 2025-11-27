from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.authentication_list_response import AuthenticationListResponse
from ...models.exception_response import ExceptionResponse
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
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
        "url": "/api/v2/auth/sessions",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, AuthenticationListResponse, ExceptionResponse]]:
    if response.status_code == 200:
        response_200 = AuthenticationListResponse.from_dict(response.json())



        return response_200

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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, AuthenticationListResponse, ExceptionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, int] = 10,
    x_continuation_token: Union[Unset, str] = UNSET,

) -> Response[Union[Any, AuthenticationListResponse, ExceptionResponse]]:
    """ Pobranie listy aktywnych sesji

     Zwraca listę aktywnych sesji uwierzytelnienia.

    **Sortowanie:**

    - startDate (Desc)


    Args:
        page_size (Union[Unset, int]):  Default: 10.
        x_continuation_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AuthenticationListResponse, ExceptionResponse]]
     """


    kwargs = _get_kwargs(
        page_size=page_size,
x_continuation_token=x_continuation_token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, int] = 10,
    x_continuation_token: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, AuthenticationListResponse, ExceptionResponse]]:
    """ Pobranie listy aktywnych sesji

     Zwraca listę aktywnych sesji uwierzytelnienia.

    **Sortowanie:**

    - startDate (Desc)


    Args:
        page_size (Union[Unset, int]):  Default: 10.
        x_continuation_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AuthenticationListResponse, ExceptionResponse]
     """


    return sync_detailed(
        client=client,
page_size=page_size,
x_continuation_token=x_continuation_token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, int] = 10,
    x_continuation_token: Union[Unset, str] = UNSET,

) -> Response[Union[Any, AuthenticationListResponse, ExceptionResponse]]:
    """ Pobranie listy aktywnych sesji

     Zwraca listę aktywnych sesji uwierzytelnienia.

    **Sortowanie:**

    - startDate (Desc)


    Args:
        page_size (Union[Unset, int]):  Default: 10.
        x_continuation_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AuthenticationListResponse, ExceptionResponse]]
     """


    kwargs = _get_kwargs(
        page_size=page_size,
x_continuation_token=x_continuation_token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, int] = 10,
    x_continuation_token: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, AuthenticationListResponse, ExceptionResponse]]:
    """ Pobranie listy aktywnych sesji

     Zwraca listę aktywnych sesji uwierzytelnienia.

    **Sortowanie:**

    - startDate (Desc)


    Args:
        page_size (Union[Unset, int]):  Default: 10.
        x_continuation_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AuthenticationListResponse, ExceptionResponse]
     """


    return (await asyncio_detailed(
        client=client,
page_size=page_size,
x_continuation_token=x_continuation_token,

    )).parsed
