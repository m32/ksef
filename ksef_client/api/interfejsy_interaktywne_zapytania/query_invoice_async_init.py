from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.exception_response import ExceptionResponse
from ...models.query_invoice_async_init_response import QueryInvoiceAsyncInitResponse
from ...models.query_invoice_request import QueryInvoiceRequest
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: QueryInvoiceRequest,
) -> Dict[str, Any]:
    url = "{}/online/Query/Invoice/Async/Init".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]:
    if response.status_code == 202:
        response_202 = QueryInvoiceAsyncInitResponse.from_dict(response.json())

        return response_202
    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ExceptionResponse.from_dict(response.json())

        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]:
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
) -> Response[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]:
    """Inicjalizacja zapytania o faktury

     Inicjalizacja zapytania o faktury

    Args:
        json_body (QueryInvoiceRequest):

    Returns:
        Response[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]
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
    json_body: QueryInvoiceRequest,
) -> Optional[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]:
    """Inicjalizacja zapytania o faktury

     Inicjalizacja zapytania o faktury

    Args:
        json_body (QueryInvoiceRequest):

    Returns:
        Response[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: QueryInvoiceRequest,
) -> Response[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]:
    """Inicjalizacja zapytania o faktury

     Inicjalizacja zapytania o faktury

    Args:
        json_body (QueryInvoiceRequest):

    Returns:
        Response[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]
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
    json_body: QueryInvoiceRequest,
) -> Optional[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]:
    """Inicjalizacja zapytania o faktury

     Inicjalizacja zapytania o faktury

    Args:
        json_body (QueryInvoiceRequest):

    Returns:
        Response[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
