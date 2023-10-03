from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.exception_response import ExceptionResponse
from ...models.generate_token_request import GenerateTokenRequest
from ...models.generate_token_response import GenerateTokenResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: GenerateTokenRequest,
) -> Dict[str, Any]:
    url = "{}/online/Credentials/GenerateToken".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, GenerateTokenResponse]]:
    if response.status_code == 200:
        response_200 = GenerateTokenResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ExceptionResponse.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ExceptionResponse, GenerateTokenResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: GenerateTokenRequest,
) -> Response[Union[Any, ExceptionResponse, GenerateTokenResponse]]:
    """Generowanie tokena autoryzacyjnego

     Generowanie tokena autoryzacyjnego

    Args:
        json_body (GenerateTokenRequest):

    Returns:
        Response[Union[Any, ExceptionResponse, GenerateTokenResponse]]
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
    json_body: GenerateTokenRequest,
) -> Optional[Union[Any, ExceptionResponse, GenerateTokenResponse]]:
    """Generowanie tokena autoryzacyjnego

     Generowanie tokena autoryzacyjnego

    Args:
        json_body (GenerateTokenRequest):

    Returns:
        Response[Union[Any, ExceptionResponse, GenerateTokenResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: GenerateTokenRequest,
) -> Response[Union[Any, ExceptionResponse, GenerateTokenResponse]]:
    """Generowanie tokena autoryzacyjnego

     Generowanie tokena autoryzacyjnego

    Args:
        json_body (GenerateTokenRequest):

    Returns:
        Response[Union[Any, ExceptionResponse, GenerateTokenResponse]]
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
    json_body: GenerateTokenRequest,
) -> Optional[Union[Any, ExceptionResponse, GenerateTokenResponse]]:
    """Generowanie tokena autoryzacyjnego

     Generowanie tokena autoryzacyjnego

    Args:
        json_body (GenerateTokenRequest):

    Returns:
        Response[Union[Any, ExceptionResponse, GenerateTokenResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
