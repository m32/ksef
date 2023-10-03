from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.exception_response import ExceptionResponse
from ...models.query_sync_credentials_request import QuerySyncCredentialsRequest
from ...models.query_sync_credentials_response import QuerySyncCredentialsResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: QuerySyncCredentialsRequest,
) -> Dict[str, Any]:
    url = "{}/online/Query/Credential/Sync".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionResponse, QuerySyncCredentialsResponse]]:
    if response.status_code == 200:
        response_200 = QuerySyncCredentialsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ExceptionResponse.from_dict(response.json())

        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionResponse, QuerySyncCredentialsResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: QuerySyncCredentialsRequest,
) -> Response[Union[ExceptionResponse, QuerySyncCredentialsResponse]]:
    """Zapytanie o poswiadczenia

     Zapytanie o poswiadczenia

    Args:
        json_body (QuerySyncCredentialsRequest):

    Returns:
        Response[Union[ExceptionResponse, QuerySyncCredentialsResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: QuerySyncCredentialsRequest,
) -> Optional[Union[ExceptionResponse, QuerySyncCredentialsResponse]]:
    """Zapytanie o poswiadczenia

     Zapytanie o poswiadczenia

    Args:
        json_body (QuerySyncCredentialsRequest):

    Returns:
        Response[Union[ExceptionResponse, QuerySyncCredentialsResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: QuerySyncCredentialsRequest,
) -> Response[Union[ExceptionResponse, QuerySyncCredentialsResponse]]:
    """Zapytanie o poswiadczenia

     Zapytanie o poswiadczenia

    Args:
        json_body (QuerySyncCredentialsRequest):

    Returns:
        Response[Union[ExceptionResponse, QuerySyncCredentialsResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: QuerySyncCredentialsRequest,
) -> Optional[Union[ExceptionResponse, QuerySyncCredentialsResponse]]:
    """Zapytanie o poswiadczenia

     Zapytanie o poswiadczenia

    Args:
        json_body (QuerySyncCredentialsRequest):

    Returns:
        Response[Union[ExceptionResponse, QuerySyncCredentialsResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
