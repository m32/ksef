from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.exception_response import ExceptionResponse
from ...models.query_invoice_async_status_response import QueryInvoiceAsyncStatusResponse
from ...types import Response


def _get_kwargs(
    query_element_reference_number: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/online/Query/Invoice/Async/Status/{QueryElementReferenceNumber}".format(
        client.base_url, QueryElementReferenceNumber=query_element_reference_number
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]:
    if response.status_code == 200:
        response_200 = QueryInvoiceAsyncStatusResponse.from_dict(response.json())

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


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    query_element_reference_number: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]:
    """Sprawdzenie statusu zapytania o faktury

     Sprawdzenie statusu zapytania o faktury

    Args:
        query_element_reference_number (str):

    Returns:
        Response[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]
    """

    kwargs = _get_kwargs(
        query_element_reference_number=query_element_reference_number,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    query_element_reference_number: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]:
    """Sprawdzenie statusu zapytania o faktury

     Sprawdzenie statusu zapytania o faktury

    Args:
        query_element_reference_number (str):

    Returns:
        Response[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]
    """

    return sync_detailed(
        query_element_reference_number=query_element_reference_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    query_element_reference_number: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]:
    """Sprawdzenie statusu zapytania o faktury

     Sprawdzenie statusu zapytania o faktury

    Args:
        query_element_reference_number (str):

    Returns:
        Response[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]
    """

    kwargs = _get_kwargs(
        query_element_reference_number=query_element_reference_number,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    query_element_reference_number: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]:
    """Sprawdzenie statusu zapytania o faktury

     Sprawdzenie statusu zapytania o faktury

    Args:
        query_element_reference_number (str):

    Returns:
        Response[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]
    """

    return (
        await asyncio_detailed(
            query_element_reference_number=query_element_reference_number,
            client=client,
        )
    ).parsed
