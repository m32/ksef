from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.exception_response import ExceptionResponse
from ...models.get_payment_identifier_reference_numbers_response import GetPaymentIdentifierReferenceNumbersResponse
from ...types import Response


def _get_kwargs(
    payment_identifier: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/online/Payment/Identifier/GetReferenceNumbers/{PaymentIdentifier}".format(
        client.base_url, PaymentIdentifier=payment_identifier
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
) -> Optional[Union[Any, ExceptionResponse, GetPaymentIdentifierReferenceNumbersResponse]]:
    if response.status_code == 200:
        response_200 = GetPaymentIdentifierReferenceNumbersResponse.from_dict(response.json())

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
) -> Response[Union[Any, ExceptionResponse, GetPaymentIdentifierReferenceNumbersResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    payment_identifier: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ExceptionResponse, GetPaymentIdentifierReferenceNumbersResponse]]:
    """Pobranie listy faktur dla identyfikatora platnosci

     Pobranie listy faktur dla identyfikatora platnosci

    Args:
        payment_identifier (str):

    Returns:
        Response[Union[Any, ExceptionResponse, GetPaymentIdentifierReferenceNumbersResponse]]
    """

    kwargs = _get_kwargs(
        payment_identifier=payment_identifier,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    payment_identifier: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ExceptionResponse, GetPaymentIdentifierReferenceNumbersResponse]]:
    """Pobranie listy faktur dla identyfikatora platnosci

     Pobranie listy faktur dla identyfikatora platnosci

    Args:
        payment_identifier (str):

    Returns:
        Response[Union[Any, ExceptionResponse, GetPaymentIdentifierReferenceNumbersResponse]]
    """

    return sync_detailed(
        payment_identifier=payment_identifier,
        client=client,
    ).parsed


async def asyncio_detailed(
    payment_identifier: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ExceptionResponse, GetPaymentIdentifierReferenceNumbersResponse]]:
    """Pobranie listy faktur dla identyfikatora platnosci

     Pobranie listy faktur dla identyfikatora platnosci

    Args:
        payment_identifier (str):

    Returns:
        Response[Union[Any, ExceptionResponse, GetPaymentIdentifierReferenceNumbersResponse]]
    """

    kwargs = _get_kwargs(
        payment_identifier=payment_identifier,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    payment_identifier: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ExceptionResponse, GetPaymentIdentifierReferenceNumbersResponse]]:
    """Pobranie listy faktur dla identyfikatora platnosci

     Pobranie listy faktur dla identyfikatora platnosci

    Args:
        payment_identifier (str):

    Returns:
        Response[Union[Any, ExceptionResponse, GetPaymentIdentifierReferenceNumbersResponse]]
    """

    return (
        await asyncio_detailed(
            payment_identifier=payment_identifier,
            client=client,
        )
    ).parsed
