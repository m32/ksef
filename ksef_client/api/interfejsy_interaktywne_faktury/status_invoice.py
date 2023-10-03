from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.exception_response import ExceptionResponse
from ...models.status_invoice_response import StatusInvoiceResponse
from ...types import Response


def _get_kwargs(
    invoice_element_reference_number: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/online/Invoice/Status/{InvoiceElementReferenceNumber}".format(
        client.base_url, InvoiceElementReferenceNumber=invoice_element_reference_number
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, StatusInvoiceResponse]]:
    if response.status_code == 200:
        response_200 = StatusInvoiceResponse.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ExceptionResponse, StatusInvoiceResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    invoice_element_reference_number: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ExceptionResponse, StatusInvoiceResponse]]:
    """Sprawdzenie statusu wysłanej faktury

     Sprawdzenie statusu wysłanej faktury

    Args:
        invoice_element_reference_number (str):

    Returns:
        Response[Union[Any, ExceptionResponse, StatusInvoiceResponse]]
    """

    kwargs = _get_kwargs(
        invoice_element_reference_number=invoice_element_reference_number,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    invoice_element_reference_number: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ExceptionResponse, StatusInvoiceResponse]]:
    """Sprawdzenie statusu wysłanej faktury

     Sprawdzenie statusu wysłanej faktury

    Args:
        invoice_element_reference_number (str):

    Returns:
        Response[Union[Any, ExceptionResponse, StatusInvoiceResponse]]
    """

    return sync_detailed(
        invoice_element_reference_number=invoice_element_reference_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    invoice_element_reference_number: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ExceptionResponse, StatusInvoiceResponse]]:
    """Sprawdzenie statusu wysłanej faktury

     Sprawdzenie statusu wysłanej faktury

    Args:
        invoice_element_reference_number (str):

    Returns:
        Response[Union[Any, ExceptionResponse, StatusInvoiceResponse]]
    """

    kwargs = _get_kwargs(
        invoice_element_reference_number=invoice_element_reference_number,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    invoice_element_reference_number: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ExceptionResponse, StatusInvoiceResponse]]:
    """Sprawdzenie statusu wysłanej faktury

     Sprawdzenie statusu wysłanej faktury

    Args:
        invoice_element_reference_number (str):

    Returns:
        Response[Union[Any, ExceptionResponse, StatusInvoiceResponse]]
    """

    return (
        await asyncio_detailed(
            invoice_element_reference_number=invoice_element_reference_number,
            client=client,
        )
    ).parsed
