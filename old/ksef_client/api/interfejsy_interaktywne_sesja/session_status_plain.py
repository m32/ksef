from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.exception_response import ExceptionResponse
from ...models.session_status_response import SessionStatusResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    page_size: int,
    page_offset: int,
    include_details: bool,
) -> Dict[str, Any]:
    url = "{}/online/Session/Status".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["PageSize"] = page_size
    params["PageOffset"] = page_offset
    params["IncludeDetails"] = True

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionResponse, SessionStatusResponse]]:
    if response.status_code == 200:
        response_200 = SessionStatusResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ExceptionResponse.from_dict(response.json())

        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionResponse, SessionStatusResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page_size: int,
    page_offset: int,
    include_details: bool,
) -> Response[Union[ExceptionResponse, SessionStatusResponse]]:
    """Sprawdzenie statusu aktywnej sesji interaktywnej

     Sprawdzenie statusu obecnego przetwarzania interaktywnego

    Args:
        page_size (int):
        page_offset (int):

    Returns:
        Response[Union[ExceptionResponse, SessionStatusResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        page_offset=page_offset,
        include_details=include_details,
    )
    print('session_status_plain', kwargs)
    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )
    print('session_status_plain', response, response.text)

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page_size: int,
    page_offset: int,
    include_details: bool,
) -> Optional[Union[ExceptionResponse, SessionStatusResponse]]:
    """Sprawdzenie statusu aktywnej sesji interaktywnej

     Sprawdzenie statusu obecnego przetwarzania interaktywnego

    Args:
        page_size (int):
        page_offset (int):

    Returns:
        Response[Union[ExceptionResponse, SessionStatusResponse]]
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        page_offset=page_offset,
        include_details=include_details,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page_size: int,
    page_offset: int,
    include_details: bool,
) -> Response[Union[ExceptionResponse, SessionStatusResponse]]:
    """Sprawdzenie statusu aktywnej sesji interaktywnej

     Sprawdzenie statusu obecnego przetwarzania interaktywnego

    Args:
        page_size (int):
        page_offset (int):

    Returns:
        Response[Union[ExceptionResponse, SessionStatusResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        page_offset=page_offset,
        include_details=include_details,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page_size: int,
    page_offset: int,
    include_details: bool,
) -> Optional[Union[ExceptionResponse, SessionStatusResponse]]:
    """Sprawdzenie statusu aktywnej sesji interaktywnej

     Sprawdzenie statusu obecnego przetwarzania interaktywnego

    Args:
        page_size (int):
        page_offset (int):

    Returns:
        Response[Union[ExceptionResponse, SessionStatusResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            page_offset=page_offset,
            include_details=include_details,
        )
    ).parsed
