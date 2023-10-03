from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.authorisation_challenge_request import AuthorisationChallengeRequest
from ...models.authorisation_challenge_response import AuthorisationChallengeResponse
from ...models.exception_response import ExceptionResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: AuthorisationChallengeRequest,
) -> Dict[str, Any]:
    url = "{}/online/Session/AuthorisationChallenge".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[AuthorisationChallengeResponse, ExceptionResponse]]:
    if response.status_code == 201:
        response_201 = AuthorisationChallengeResponse.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[AuthorisationChallengeResponse, ExceptionResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: AuthorisationChallengeRequest,
) -> Response[Union[AuthorisationChallengeResponse, ExceptionResponse]]:
    """Inicjalizacja mechanizmu uwierzytelnienia i autoryzacji

     Inicjalizacja mechanizmu uwierzytelnienia i autoryzacji.

    Args:
        json_body (AuthorisationChallengeRequest):

    Returns:
        Response[Union[AuthorisationChallengeResponse, ExceptionResponse]]
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
    client: Client,
    json_body: AuthorisationChallengeRequest,
) -> Optional[Union[AuthorisationChallengeResponse, ExceptionResponse]]:
    """Inicjalizacja mechanizmu uwierzytelnienia i autoryzacji

     Inicjalizacja mechanizmu uwierzytelnienia i autoryzacji.

    Args:
        json_body (AuthorisationChallengeRequest):

    Returns:
        Response[Union[AuthorisationChallengeResponse, ExceptionResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: AuthorisationChallengeRequest,
) -> Response[Union[AuthorisationChallengeResponse, ExceptionResponse]]:
    """Inicjalizacja mechanizmu uwierzytelnienia i autoryzacji

     Inicjalizacja mechanizmu uwierzytelnienia i autoryzacji.

    Args:
        json_body (AuthorisationChallengeRequest):

    Returns:
        Response[Union[AuthorisationChallengeResponse, ExceptionResponse]]
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
    client: Client,
    json_body: AuthorisationChallengeRequest,
) -> Optional[Union[AuthorisationChallengeResponse, ExceptionResponse]]:
    """Inicjalizacja mechanizmu uwierzytelnienia i autoryzacji

     Inicjalizacja mechanizmu uwierzytelnienia i autoryzacji.

    Args:
        json_body (AuthorisationChallengeRequest):

    Returns:
        Response[Union[AuthorisationChallengeResponse, ExceptionResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
