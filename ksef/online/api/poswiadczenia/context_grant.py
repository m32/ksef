from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.grant_context_credentials_request import GrantContextCredentialsRequest
from ...models.status_credentials_response import StatusCredentialsResponse
from typing import Dict
from ...models.exception_response import ExceptionResponse
from typing import cast



def _get_kwargs(
    *,
    json_body: GrantContextCredentialsRequest,

) -> Dict[str, Any]:
    

    cookies = {}


    

    json_json_body = json_body.to_dict()



    

    return {
        "method": "post",
        "url": "/online/Credentials/ContextGrant",
        "json": json_json_body,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, StatusCredentialsResponse]]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = StatusCredentialsResponse.from_dict(response.json())



        return response_202
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ExceptionResponse.from_dict(response.json())



        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, StatusCredentialsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: GrantContextCredentialsRequest,

) -> Response[Union[Any, ExceptionResponse, StatusCredentialsResponse]]:
    """ Nadanie poświadczeń kontekstowych

     Nadanie poświadczeń kontekstowych

    Args:
        json_body (GrantContextCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, StatusCredentialsResponse]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,

    )

    print("*"*20, "/online/Credentials/ContextGrant")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//online/Credentials/ContextGrant")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    json_body: GrantContextCredentialsRequest,

) -> Optional[Union[Any, ExceptionResponse, StatusCredentialsResponse]]:
    """ Nadanie poświadczeń kontekstowych

     Nadanie poświadczeń kontekstowych

    Args:
        json_body (GrantContextCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, StatusCredentialsResponse]
     """


    return sync_detailed(
        client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: GrantContextCredentialsRequest,

) -> Response[Union[Any, ExceptionResponse, StatusCredentialsResponse]]:
    """ Nadanie poświadczeń kontekstowych

     Nadanie poświadczeń kontekstowych

    Args:
        json_body (GrantContextCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, StatusCredentialsResponse]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: GrantContextCredentialsRequest,

) -> Optional[Union[Any, ExceptionResponse, StatusCredentialsResponse]]:
    """ Nadanie poświadczeń kontekstowych

     Nadanie poświadczeń kontekstowych

    Args:
        json_body (GrantContextCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, StatusCredentialsResponse]
     """


    return (await asyncio_detailed(
        client=client,
json_body=json_body,

    )).parsed
