import logging
logger = logging.getLogger(__name__)

from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.exception_response import ExceptionResponse
from ...models.send_invoice_request import SendInvoiceRequest
from ...models.send_invoice_response import SendInvoiceResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: SendInvoiceRequest,
) -> Dict[str, Any]:
    url = "{}/online/Invoice/Send".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionResponse, SendInvoiceResponse]]:
    if response.status_code == 202:
        response_202 = SendInvoiceResponse.from_dict(response.json())

        return response_202
    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ExceptionResponse.from_dict(response.json())

        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionResponse, SendInvoiceResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: SendInvoiceRequest,
) -> Response[Union[ExceptionResponse, SendInvoiceResponse]]:
    """Wysyłka faktury

     Wysyłka faktury

    Args:
        json_body (SendInvoiceRequest):

    Returns:
        Response[Union[ExceptionResponse, SendInvoiceResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )
    logger.debug('send_invoice: %s', kwargs)

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )
    logger.debug('send_invoice: %s %s', response, response.content)

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: SendInvoiceRequest,
) -> Optional[Union[ExceptionResponse, SendInvoiceResponse]]:
    """Wysyłka faktury

     Wysyłka faktury

    Args:
        json_body (SendInvoiceRequest):

    Returns:
        Response[Union[ExceptionResponse, SendInvoiceResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: SendInvoiceRequest,
) -> Response[Union[ExceptionResponse, SendInvoiceResponse]]:
    """Wysyłka faktury

     Wysyłka faktury

    Args:
        json_body (SendInvoiceRequest):

    Returns:
        Response[Union[ExceptionResponse, SendInvoiceResponse]]
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
    json_body: SendInvoiceRequest,
) -> Optional[Union[ExceptionResponse, SendInvoiceResponse]]:
    """Wysyłka faktury

     Wysyłka faktury

    Args:
        json_body (SendInvoiceRequest):

    Returns:
        Response[Union[ExceptionResponse, SendInvoiceResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed