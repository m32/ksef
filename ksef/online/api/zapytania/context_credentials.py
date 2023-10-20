from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.query_sync_credentials_response import QuerySyncCredentialsResponse
from typing import Union
from typing import Dict
from typing import Optional
from ...models.exception_response import ExceptionResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    context_nip: Union[Unset, None, str] = UNSET,
    source_identifier: Union[Unset, None, str] = UNSET,
    target_identifier: Union[Unset, None, str] = UNSET,

) -> Dict[str, Any]:
    

    cookies = {}


    params: Dict[str, Any] = {}
    params["contextNip"] = context_nip


    params["sourceIdentifier"] = source_identifier


    params["targetIdentifier"] = target_identifier



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
        "method": "get",
        "url": "/online/Query/Credential/Context/Sync",
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ExceptionResponse, QuerySyncCredentialsResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = QuerySyncCredentialsResponse.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ExceptionResponse, QuerySyncCredentialsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    context_nip: Union[Unset, None, str] = UNSET,
    source_identifier: Union[Unset, None, str] = UNSET,
    target_identifier: Union[Unset, None, str] = UNSET,

) -> Response[Union[ExceptionResponse, QuerySyncCredentialsResponse]]:
    """ Zapytanie o poświadczenia nadane przez jednostkę nadrzędną

     Zapytanie o poświadczenia nadane przez jednostkę nadrzędną

    Args:
        context_nip (Union[Unset, None, str]):
        source_identifier (Union[Unset, None, str]):
        target_identifier (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, QuerySyncCredentialsResponse]]
     """


    kwargs = _get_kwargs(
        context_nip=context_nip,
source_identifier=source_identifier,
target_identifier=target_identifier,

    )

    print("*"*20, "/online/Query/Credential/Context/Sync")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//online/Query/Credential/Context/Sync")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    context_nip: Union[Unset, None, str] = UNSET,
    source_identifier: Union[Unset, None, str] = UNSET,
    target_identifier: Union[Unset, None, str] = UNSET,

) -> Optional[Union[ExceptionResponse, QuerySyncCredentialsResponse]]:
    """ Zapytanie o poświadczenia nadane przez jednostkę nadrzędną

     Zapytanie o poświadczenia nadane przez jednostkę nadrzędną

    Args:
        context_nip (Union[Unset, None, str]):
        source_identifier (Union[Unset, None, str]):
        target_identifier (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, QuerySyncCredentialsResponse]
     """


    return sync_detailed(
        client=client,
context_nip=context_nip,
source_identifier=source_identifier,
target_identifier=target_identifier,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    context_nip: Union[Unset, None, str] = UNSET,
    source_identifier: Union[Unset, None, str] = UNSET,
    target_identifier: Union[Unset, None, str] = UNSET,

) -> Response[Union[ExceptionResponse, QuerySyncCredentialsResponse]]:
    """ Zapytanie o poświadczenia nadane przez jednostkę nadrzędną

     Zapytanie o poświadczenia nadane przez jednostkę nadrzędną

    Args:
        context_nip (Union[Unset, None, str]):
        source_identifier (Union[Unset, None, str]):
        target_identifier (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, QuerySyncCredentialsResponse]]
     """


    kwargs = _get_kwargs(
        context_nip=context_nip,
source_identifier=source_identifier,
target_identifier=target_identifier,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    context_nip: Union[Unset, None, str] = UNSET,
    source_identifier: Union[Unset, None, str] = UNSET,
    target_identifier: Union[Unset, None, str] = UNSET,

) -> Optional[Union[ExceptionResponse, QuerySyncCredentialsResponse]]:
    """ Zapytanie o poświadczenia nadane przez jednostkę nadrzędną

     Zapytanie o poświadczenia nadane przez jednostkę nadrzędną

    Args:
        context_nip (Union[Unset, None, str]):
        source_identifier (Union[Unset, None, str]):
        target_identifier (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, QuerySyncCredentialsResponse]
     """


    return (await asyncio_detailed(
        client=client,
context_nip=context_nip,
source_identifier=source_identifier,
target_identifier=target_identifier,

    )).parsed
