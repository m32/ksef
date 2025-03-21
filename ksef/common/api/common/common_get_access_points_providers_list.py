from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.access_points_providers_list_response import AccessPointsProvidersListResponse
from typing import Dict
from typing import cast
from ...models.exception_response import ExceptionResponse



def _get_kwargs(
    *,
    page_size: int,
    page_offset: int,

) -> Dict[str, Any]:
    

    cookies = {}


    params: Dict[str, Any] = {}
    params["PageSize"] = page_size


    params["PageOffset"] = page_offset



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
        "method": "get",
        "url": "/common/accessPointsProvidersList",
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[AccessPointsProvidersListResponse, Any, ExceptionResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AccessPointsProvidersListResponse.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[AccessPointsProvidersListResponse, Any, ExceptionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: int,
    page_offset: int,

) -> Response[Union[AccessPointsProvidersListResponse, Any, ExceptionResponse]]:
    """ Interfejs wspólny pobrania listy Dostawców usług Peppol zarejestrowanych w KSeF

     Pobieranie listy Dostawców usług Peppol

    Args:
        page_size (int):
        page_offset (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccessPointsProvidersListResponse, Any, ExceptionResponse]]
     """


    kwargs = _get_kwargs(
        page_size=page_size,
page_offset=page_offset,

    )

    print("*"*20, "/common/accessPointsProvidersList")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//common/accessPointsProvidersList")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: int,
    page_offset: int,

) -> Optional[Union[AccessPointsProvidersListResponse, Any, ExceptionResponse]]:
    """ Interfejs wspólny pobrania listy Dostawców usług Peppol zarejestrowanych w KSeF

     Pobieranie listy Dostawców usług Peppol

    Args:
        page_size (int):
        page_offset (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccessPointsProvidersListResponse, Any, ExceptionResponse]
     """


    return sync_detailed(
        client=client,
page_size=page_size,
page_offset=page_offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: int,
    page_offset: int,

) -> Response[Union[AccessPointsProvidersListResponse, Any, ExceptionResponse]]:
    """ Interfejs wspólny pobrania listy Dostawców usług Peppol zarejestrowanych w KSeF

     Pobieranie listy Dostawców usług Peppol

    Args:
        page_size (int):
        page_offset (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccessPointsProvidersListResponse, Any, ExceptionResponse]]
     """


    kwargs = _get_kwargs(
        page_size=page_size,
page_offset=page_offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: int,
    page_offset: int,

) -> Optional[Union[AccessPointsProvidersListResponse, Any, ExceptionResponse]]:
    """ Interfejs wspólny pobrania listy Dostawców usług Peppol zarejestrowanych w KSeF

     Pobieranie listy Dostawców usług Peppol

    Args:
        page_size (int):
        page_offset (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccessPointsProvidersListResponse, Any, ExceptionResponse]
     """


    return (await asyncio_detailed(
        client=client,
page_size=page_size,
page_offset=page_offset,

    )).parsed
