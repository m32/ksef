from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.query_sync_credentials_accounting_response_main import QuerySyncCredentialsAccountingResponseMain
from typing import Dict
from typing import cast
from ...models.exception_response import ExceptionResponse
from ...models.query_sync_accounting_credentials_request import QuerySyncAccountingCredentialsRequest



def _get_kwargs(
    *,
    json_body: QuerySyncAccountingCredentialsRequest,
    page_size: int,
    page_offset: int,

) -> Dict[str, Any]:
    

    cookies = {}


    params: Dict[str, Any] = {}
    params["PageSize"] = page_size


    params["PageOffset"] = page_offset



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    json_json_body = json_body.to_dict()



    

    return {
        "method": "post",
        "url": "/online/Query/Credential/Accounting/Sync",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ExceptionResponse, QuerySyncCredentialsAccountingResponseMain]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = QuerySyncCredentialsAccountingResponseMain.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ExceptionResponse, QuerySyncCredentialsAccountingResponseMain]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: QuerySyncAccountingCredentialsRequest,
    page_size: int,
    page_offset: int,

) -> Response[Union[ExceptionResponse, QuerySyncCredentialsAccountingResponseMain]]:
    """ Zapytanie o poświadczenia nadane przez biuro rachunkowe

     Zapytanie o poświadczenia nadane przez biuro rachunkowe

    Args:
        page_size (int):
        page_offset (int):
        json_body (QuerySyncAccountingCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, QuerySyncCredentialsAccountingResponseMain]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,
page_size=page_size,
page_offset=page_offset,

    )

    print("*"*20, "/online/Query/Credential/Accounting/Sync")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//online/Query/Credential/Accounting/Sync")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    json_body: QuerySyncAccountingCredentialsRequest,
    page_size: int,
    page_offset: int,

) -> Optional[Union[ExceptionResponse, QuerySyncCredentialsAccountingResponseMain]]:
    """ Zapytanie o poświadczenia nadane przez biuro rachunkowe

     Zapytanie o poświadczenia nadane przez biuro rachunkowe

    Args:
        page_size (int):
        page_offset (int):
        json_body (QuerySyncAccountingCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, QuerySyncCredentialsAccountingResponseMain]
     """


    return sync_detailed(
        client=client,
json_body=json_body,
page_size=page_size,
page_offset=page_offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: QuerySyncAccountingCredentialsRequest,
    page_size: int,
    page_offset: int,

) -> Response[Union[ExceptionResponse, QuerySyncCredentialsAccountingResponseMain]]:
    """ Zapytanie o poświadczenia nadane przez biuro rachunkowe

     Zapytanie o poświadczenia nadane przez biuro rachunkowe

    Args:
        page_size (int):
        page_offset (int):
        json_body (QuerySyncAccountingCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, QuerySyncCredentialsAccountingResponseMain]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,
page_size=page_size,
page_offset=page_offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: QuerySyncAccountingCredentialsRequest,
    page_size: int,
    page_offset: int,

) -> Optional[Union[ExceptionResponse, QuerySyncCredentialsAccountingResponseMain]]:
    """ Zapytanie o poświadczenia nadane przez biuro rachunkowe

     Zapytanie o poświadczenia nadane przez biuro rachunkowe

    Args:
        page_size (int):
        page_offset (int):
        json_body (QuerySyncAccountingCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, QuerySyncCredentialsAccountingResponseMain]
     """


    return (await asyncio_detailed(
        client=client,
json_body=json_body,
page_size=page_size,
page_offset=page_offset,

    )).parsed
