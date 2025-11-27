from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.certificate_enrollment_status_response import CertificateEnrollmentStatusResponse
from ...models.exception_response import ExceptionResponse
from typing import cast



def _get_kwargs(
    reference_number: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/certificates/enrollments/{reference_number}".format(reference_number=reference_number,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, CertificateEnrollmentStatusResponse, ExceptionResponse]]:
    if response.status_code == 200:
        response_200 = CertificateEnrollmentStatusResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, CertificateEnrollmentStatusResponse, ExceptionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    reference_number: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, CertificateEnrollmentStatusResponse, ExceptionResponse]]:
    """ Pobranie statusu przetwarzania wniosku certyfikacyjnego

     Zwraca informacje o statusie wniosku certyfikacyjnego.

    Args:
        reference_number (str): Numer referencyjny.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CertificateEnrollmentStatusResponse, ExceptionResponse]]
     """


    kwargs = _get_kwargs(
        reference_number=reference_number,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    reference_number: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, CertificateEnrollmentStatusResponse, ExceptionResponse]]:
    """ Pobranie statusu przetwarzania wniosku certyfikacyjnego

     Zwraca informacje o statusie wniosku certyfikacyjnego.

    Args:
        reference_number (str): Numer referencyjny.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CertificateEnrollmentStatusResponse, ExceptionResponse]
     """


    return sync_detailed(
        reference_number=reference_number,
client=client,

    ).parsed

async def asyncio_detailed(
    reference_number: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, CertificateEnrollmentStatusResponse, ExceptionResponse]]:
    """ Pobranie statusu przetwarzania wniosku certyfikacyjnego

     Zwraca informacje o statusie wniosku certyfikacyjnego.

    Args:
        reference_number (str): Numer referencyjny.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CertificateEnrollmentStatusResponse, ExceptionResponse]]
     """


    kwargs = _get_kwargs(
        reference_number=reference_number,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    reference_number: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, CertificateEnrollmentStatusResponse, ExceptionResponse]]:
    """ Pobranie statusu przetwarzania wniosku certyfikacyjnego

     Zwraca informacje o statusie wniosku certyfikacyjnego.

    Args:
        reference_number (str): Numer referencyjny.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CertificateEnrollmentStatusResponse, ExceptionResponse]
     """


    return (await asyncio_detailed(
        reference_number=reference_number,
client=client,

    )).parsed
