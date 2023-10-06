from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.exception_response import ExceptionResponse
from ...models.terminate_session_response import TerminateSessionResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/online/Session/Terminate".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionResponse, TerminateSessionResponse]]:
    if response.status_code == 200:
        response_200 = TerminateSessionResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ExceptionResponse.from_dict(response.json())

        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionResponse, TerminateSessionResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ExceptionResponse, TerminateSessionResponse]]:
    """Wymuszenie zamknięcia sesji

     Wymuszenie zamknięcia sesji interaktywnej

    Returns:
        Response[Union[ExceptionResponse, TerminateSessionResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ExceptionResponse, TerminateSessionResponse]]:
    """Wymuszenie zamknięcia sesji

     Wymuszenie zamknięcia sesji interaktywnej

    Returns:
        Response[Union[ExceptionResponse, TerminateSessionResponse]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ExceptionResponse, TerminateSessionResponse]]:
    """Wymuszenie zamknięcia sesji

     Wymuszenie zamknięcia sesji interaktywnej

    Returns:
        Response[Union[ExceptionResponse, TerminateSessionResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ExceptionResponse, TerminateSessionResponse]]:
    """Wymuszenie zamknięcia sesji

     Wymuszenie zamknięcia sesji interaktywnej

    Returns:
        Response[Union[ExceptionResponse, TerminateSessionResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
