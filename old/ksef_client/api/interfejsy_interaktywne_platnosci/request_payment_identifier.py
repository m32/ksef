from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.exception_response import ExceptionResponse
from ...models.request_payment_identifier_request import RequestPaymentIdentifierRequest
from ...models.request_payment_identifier_response import RequestPaymentIdentifierResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RequestPaymentIdentifierRequest,
) -> Dict[str, Any]:
    url = "{}/online/Payment/Identifier/Request".format(client.base_url)

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, ExceptionResponse, RequestPaymentIdentifierResponse]]:
    if response.status_code == 201:
        response_201 = RequestPaymentIdentifierResponse.from_dict(response.json())

        return response_201
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


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, ExceptionResponse, RequestPaymentIdentifierResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RequestPaymentIdentifierRequest,
) -> Response[Union[Any, ExceptionResponse, RequestPaymentIdentifierResponse]]:
    """Wygenerowanie identyfikatora platnosci

     Wygenerowanie identyfikatora platnosci

    Args:
        json_body (RequestPaymentIdentifierRequest):

    Returns:
        Response[Union[Any, ExceptionResponse, RequestPaymentIdentifierResponse]]
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
    json_body: RequestPaymentIdentifierRequest,
) -> Optional[Union[Any, ExceptionResponse, RequestPaymentIdentifierResponse]]:
    """Wygenerowanie identyfikatora platnosci

     Wygenerowanie identyfikatora platnosci

    Args:
        json_body (RequestPaymentIdentifierRequest):

    Returns:
        Response[Union[Any, ExceptionResponse, RequestPaymentIdentifierResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RequestPaymentIdentifierRequest,
) -> Response[Union[Any, ExceptionResponse, RequestPaymentIdentifierResponse]]:
    """Wygenerowanie identyfikatora platnosci

     Wygenerowanie identyfikatora platnosci

    Args:
        json_body (RequestPaymentIdentifierRequest):

    Returns:
        Response[Union[Any, ExceptionResponse, RequestPaymentIdentifierResponse]]
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
    json_body: RequestPaymentIdentifierRequest,
) -> Optional[Union[Any, ExceptionResponse, RequestPaymentIdentifierResponse]]:
    """Wygenerowanie identyfikatora platnosci

     Wygenerowanie identyfikatora platnosci

    Args:
        json_body (RequestPaymentIdentifierRequest):

    Returns:
        Response[Union[Any, ExceptionResponse, RequestPaymentIdentifierResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
