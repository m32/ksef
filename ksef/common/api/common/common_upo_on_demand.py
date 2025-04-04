from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.upo_on_demand_response import UpoOnDemandResponse
from typing import Dict
from typing import cast
from ...models.exception_response import ExceptionResponse



def _get_kwargs(
    reference_number: str,
    ksef_reference_number: str,

) -> Dict[str, Any]:
    

    cookies = {}


    

    

    

    return {
        "method": "get",
        "url": "/common/Upo/ondemand/{ReferenceNumber}/{KsefReferenceNumber}".format(ReferenceNumber=reference_number,KsefReferenceNumber=ksef_reference_number,),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, UpoOnDemandResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpoOnDemandResponse.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, UpoOnDemandResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    reference_number: str,
    ksef_reference_number: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, ExceptionResponse, UpoOnDemandResponse]]:
    """ Interfejs wspólny pobrania UPO na żądanie

     Pobieranie UPO na żądanie

    Args:
        reference_number (str):
        ksef_reference_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, UpoOnDemandResponse]]
     """


    kwargs = _get_kwargs(
        reference_number=reference_number,
ksef_reference_number=ksef_reference_number,

    )

    print("*"*20, "/common/Upo/ondemand/{ReferenceNumber}/{KsefReferenceNumber}")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//common/Upo/ondemand/{ReferenceNumber}/{KsefReferenceNumber}")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    reference_number: str,
    ksef_reference_number: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, ExceptionResponse, UpoOnDemandResponse]]:
    """ Interfejs wspólny pobrania UPO na żądanie

     Pobieranie UPO na żądanie

    Args:
        reference_number (str):
        ksef_reference_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, UpoOnDemandResponse]
     """


    return sync_detailed(
        reference_number=reference_number,
ksef_reference_number=ksef_reference_number,
client=client,

    ).parsed

async def asyncio_detailed(
    reference_number: str,
    ksef_reference_number: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, ExceptionResponse, UpoOnDemandResponse]]:
    """ Interfejs wspólny pobrania UPO na żądanie

     Pobieranie UPO na żądanie

    Args:
        reference_number (str):
        ksef_reference_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, UpoOnDemandResponse]]
     """


    kwargs = _get_kwargs(
        reference_number=reference_number,
ksef_reference_number=ksef_reference_number,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    reference_number: str,
    ksef_reference_number: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, ExceptionResponse, UpoOnDemandResponse]]:
    """ Interfejs wspólny pobrania UPO na żądanie

     Pobieranie UPO na żądanie

    Args:
        reference_number (str):
        ksef_reference_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, UpoOnDemandResponse]
     """


    return (await asyncio_detailed(
        reference_number=reference_number,
ksef_reference_number=ksef_reference_number,
client=client,

    )).parsed
