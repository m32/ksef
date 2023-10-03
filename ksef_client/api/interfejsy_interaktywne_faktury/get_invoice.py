import logging
logger = logging.getLogger(__name__)

from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.exception_response import ExceptionResponse
from ...models.get_invoice_response_200 import GetInvoiceResponse200
from ...types import Response


def _get_kwargs(
    k_se_f_reference_number: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/online/Invoice/Get/{KSeFReferenceNumber}".format(
        client.base_url, KSeFReferenceNumber=k_se_f_reference_number
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, GetInvoiceResponse200]]:
    if response.status_code == 200:
        response_200 = GetInvoiceResponse200.from_dict(response.content)

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ExceptionResponse, GetInvoiceResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    k_se_f_reference_number: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ExceptionResponse, GetInvoiceResponse200]]:
    """Pobranie faktury

     Pobranie faktury

    Args:
        k_se_f_reference_number (str):

    Returns:
        Response[Union[Any, ExceptionResponse, GetInvoiceResponse200]]
    """

    kwargs = _get_kwargs(
        k_se_f_reference_number=k_se_f_reference_number,
        client=client,
    )
    logger.debug('get_invoice: %s', kwargs)
    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )
    logger.debug('get_invoice: %s %s', response, response.content)

    return _build_response(response=response)


def sync(
    k_se_f_reference_number: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ExceptionResponse, GetInvoiceResponse200]]:
    """Pobranie faktury

     Pobranie faktury

    Args:
        k_se_f_reference_number (str):

    Returns:
        Response[Union[Any, ExceptionResponse, GetInvoiceResponse200]]
    """

    return sync_detailed(
        k_se_f_reference_number=k_se_f_reference_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    k_se_f_reference_number: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ExceptionResponse, GetInvoiceResponse200]]:
    """Pobranie faktury

     Pobranie faktury

    Args:
        k_se_f_reference_number (str):

    Returns:
        Response[Union[Any, ExceptionResponse, GetInvoiceResponse200]]
    """

    kwargs = _get_kwargs(
        k_se_f_reference_number=k_se_f_reference_number,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    k_se_f_reference_number: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ExceptionResponse, GetInvoiceResponse200]]:
    """Pobranie faktury

     Pobranie faktury

    Args:
        k_se_f_reference_number (str):

    Returns:
        Response[Union[Any, ExceptionResponse, GetInvoiceResponse200]]
    """

    return (
        await asyncio_detailed(
            k_se_f_reference_number=k_se_f_reference_number,
            client=client,
        )
    ).parsed
