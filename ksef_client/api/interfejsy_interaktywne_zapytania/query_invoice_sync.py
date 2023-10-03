import logging
logger = logging.getLogger(__name__)

from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.exception_response import ExceptionResponse
from ...models.query_invoice_request import QueryInvoiceRequest
from ...models.query_invoice_sync_response import QueryInvoiceSyncResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: QueryInvoiceRequest,
    page_size: int,
    page_offset: int,
) -> Dict[str, Any]:
    url = "{}/online/Query/Invoice/Sync".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["PageSize"] = page_size

    params["PageOffset"] = page_offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionResponse, QueryInvoiceSyncResponse]]:
    if response.status_code == 200:
        response_200 = QueryInvoiceSyncResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ExceptionResponse.from_dict(response.json())

        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionResponse, QueryInvoiceSyncResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: QueryInvoiceRequest,
    page_size: int,
    page_offset: int,
) -> Response[Union[ExceptionResponse, QueryInvoiceSyncResponse]]:
    """Zapytanie o faktury

     Zapytanie o faktury

    Args:
        page_size (int):
        page_offset (int):
        json_body (QueryInvoiceRequest):

    Returns:
        Response[Union[ExceptionResponse, QueryInvoiceSyncResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        page_size=page_size,
        page_offset=page_offset,
    )
    logger.debug('query_invoice_sync: %s', kwargs)
    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )
    logger.debug('query_invoice_sync: %s %s', response, response.text)

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: QueryInvoiceRequest,
    page_size: int,
    page_offset: int,
) -> Optional[Union[ExceptionResponse, QueryInvoiceSyncResponse]]:
    """Zapytanie o faktury

     Zapytanie o faktury

    Args:
        page_size (int):
        page_offset (int):
        json_body (QueryInvoiceRequest):

    Returns:
        Response[Union[ExceptionResponse, QueryInvoiceSyncResponse]]
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
    json_body: QueryInvoiceRequest,
    page_size: int,
    page_offset: int,
) -> Response[Union[ExceptionResponse, QueryInvoiceSyncResponse]]:
    """Zapytanie o faktury

     Zapytanie o faktury

    Args:
        page_size (int):
        page_offset (int):
        json_body (QueryInvoiceRequest):

    Returns:
        Response[Union[ExceptionResponse, QueryInvoiceSyncResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        page_size=page_size,
        page_offset=page_offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: QueryInvoiceRequest,
    page_size: int,
    page_offset: int,
) -> Optional[Union[ExceptionResponse, QueryInvoiceSyncResponse]]:
    """Zapytanie o faktury

     Zapytanie o faktury

    Args:
        page_size (int):
        page_offset (int):
        json_body (QueryInvoiceRequest):

    Returns:
        Response[Union[ExceptionResponse, QueryInvoiceSyncResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            page_size=page_size,
            page_offset=page_offset,
        )
    ).parsed
