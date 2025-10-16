from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from ...models.test_data_permissions_grant_request import TestDataPermissionsGrantRequest
from typing import cast



def _get_kwargs(
    *,
    body: TestDataPermissionsGrantRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/testdata/permissions",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400

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
    *,
    client: Union[AuthenticatedClient, Client],
    body: TestDataPermissionsGrantRequest,

) -> Response[Union[Any, ExceptionResponse]]:
    """ Nadanie uprawnień testowemu podmiotowi/osobie fizycznej

     Nadawanie uprawnień testowemu podmiotowi lub osobie fizycznej, a także w ich kontekście.

    Args:
        body (TestDataPermissionsGrantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse]]
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
    body: TestDataPermissionsGrantRequest,

) -> Optional[Union[Any, ExceptionResponse]]:
    """ Nadanie uprawnień testowemu podmiotowi/osobie fizycznej

     Nadawanie uprawnień testowemu podmiotowi lub osobie fizycznej, a także w ich kontekście.

    Args:
        body (TestDataPermissionsGrantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TestDataPermissionsGrantRequest,

) -> Response[Union[Any, ExceptionResponse]]:
    """ Nadanie uprawnień testowemu podmiotowi/osobie fizycznej

     Nadawanie uprawnień testowemu podmiotowi lub osobie fizycznej, a także w ich kontekście.

    Args:
        body (TestDataPermissionsGrantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse]]
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
    body: TestDataPermissionsGrantRequest,

) -> Optional[Union[Any, ExceptionResponse]]:
    """ Nadanie uprawnień testowemu podmiotowi/osobie fizycznej

     Nadawanie uprawnień testowemu podmiotowi lub osobie fizycznej, a także w ich kontekście.

    Args:
        body (TestDataPermissionsGrantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
