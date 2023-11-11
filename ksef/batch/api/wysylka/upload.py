from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from ...models.exception_response import ExceptionResponse
from ...models.upload_response import UploadResponse
from io import BytesIO
from ...types import File, FileJsonType
from typing import Dict



def _get_kwargs(
    reference_number: str,
    part_name: str,
    *,
    content: File,
    headers: dict,
) -> Dict[str, Any]:
    

    headers.update({
        'Content-Type': 'application/octet-stream',
        'Accept': 'application/json',
    })
    cookies = {}
    return {
        "method": "put",
        "url": "/batch/Upload/{ReferenceNumber}/{PartName}".format(ReferenceNumber=reference_number,PartName=part_name,),
        "content": content.to_bytes(),
        "headers": headers,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ExceptionResponse, UploadResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = UploadResponse.from_dict(response.json())



        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ExceptionResponse, UploadResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    reference_number: str,
    part_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    content: File,
    headers: dict,
) -> Response[Union[ExceptionResponse, UploadResponse]]:
    """ Wysyłka wsadowa paczki faktur do KSeF - załadowanie części paczki

     Załadowanie zaszyfrowanych części paczki

    Args:
        reference_number (str):
        part_name (str):
        content_data (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, UploadResponse]]
     """


    kwargs = _get_kwargs(
        reference_number=reference_number,
part_name=part_name,
content=content,
headers=headers,
    )

    print("*"*20, "/batch/Upload/{ReferenceNumber}/{PartName}")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//batch/Upload/{ReferenceNumber}/{PartName}")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    reference_number: str,
    part_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    content: File,
    headers: dict,
) -> Optional[Union[ExceptionResponse, UploadResponse]]:
    """ Wysyłka wsadowa paczki faktur do KSeF - załadowanie części paczki

     Załadowanie zaszyfrowanych części paczki

    Args:
        reference_number (str):
        part_name (str):
        content_data (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, UploadResponse]
     """


    return sync_detailed(
        reference_number=reference_number,
part_name=part_name,
client=client,
content=content,
headers=headers,
    ).parsed

async def asyncio_detailed(
    reference_number: str,
    part_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    content: File,

) -> Response[Union[ExceptionResponse, UploadResponse]]:
    """ Wysyłka wsadowa paczki faktur do KSeF - załadowanie części paczki

     Załadowanie zaszyfrowanych części paczki

    Args:
        reference_number (str):
        part_name (str):
        content_data (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, UploadResponse]]
     """


    kwargs = _get_kwargs(
        reference_number=reference_number,
part_name=part_name,
content=content,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    reference_number: str,
    part_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    content: File,

) -> Optional[Union[ExceptionResponse, UploadResponse]]:
    """ Wysyłka wsadowa paczki faktur do KSeF - załadowanie części paczki

     Załadowanie zaszyfrowanych części paczki

    Args:
        reference_number (str):
        part_name (str):
        content_data (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, UploadResponse]
     """


    return (await asyncio_detailed(
        reference_number=reference_number,
part_name=part_name,
client=client,
content=content,

    )).parsed
