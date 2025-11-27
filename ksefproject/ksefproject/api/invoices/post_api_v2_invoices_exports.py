from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from ...models.export_invoices_response import ExportInvoicesResponse
from ...models.invoice_export_request import InvoiceExportRequest
from typing import cast



def _get_kwargs(
    *,
    body: InvoiceExportRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/invoices/exports",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, ExportInvoicesResponse]]:
    if response.status_code == 201:
        response_201 = ExportInvoicesResponse.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, ExportInvoicesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: InvoiceExportRequest,

) -> Response[Union[Any, ExceptionResponse, ExportInvoicesResponse]]:
    """ Eksport paczki faktur

     Rozpoczyna asynchroniczny proces wyszukiwania faktur w systemie KSeF na podstawie przekazanych
    filtrów oraz przygotowania ich w formie zaszyfrowanej paczki.
    Wymagane jest przekazanie informacji o szyfrowaniu w polu <b>Encryption</b>, które służą do
    zabezpieczenia przygotowanej paczki z fakturami.
    Maksymalnie można uruchomić 10 równoczesnych eksportów w zalogowanym kontekście.

    System pobiera faktury rosnąco według daty określonej w filtrze (Invoicing, Issue, PermanentStorage)
    i dodaje je do paczki aż do osiągnięcia jednego z poniższych limitów:
    * Limit liczby faktur: 10 000 sztuk
    * Limit rozmiaru danych(skompresowanych): 1GB

    Paczka eksportu zawiera dodatkowy plik z metadanymi faktur w formacie JSON (`_metadata.json`).
    Zawartość pliku to
    obiekt z tablicą <b>invoices</b>, gdzie każdy element jest obiektem typu <b>InvoiceMetadata</b>
    (taki jak zwracany przez endpoint `POST /invoices/query/metadata`).

    <b>Plik z metadanymi(_metadata.json) nie jest wliczany do limitów algorytmu budowania paczki</b>.

    `Do realizacji pobierania przyrostowego należy stosować filtrowanie po dacie PermanentStorage`.

    **Sortowanie:**

    - permanentStorageDate | invoicingDate | issueDate (Asc) - pole wybierane na podstawie filtrów



    **Wymagane uprawnienia**: `InvoiceRead`.

    Args:
        body (InvoiceExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, ExportInvoicesResponse]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: InvoiceExportRequest,

) -> Optional[Union[Any, ExceptionResponse, ExportInvoicesResponse]]:
    """ Eksport paczki faktur

     Rozpoczyna asynchroniczny proces wyszukiwania faktur w systemie KSeF na podstawie przekazanych
    filtrów oraz przygotowania ich w formie zaszyfrowanej paczki.
    Wymagane jest przekazanie informacji o szyfrowaniu w polu <b>Encryption</b>, które służą do
    zabezpieczenia przygotowanej paczki z fakturami.
    Maksymalnie można uruchomić 10 równoczesnych eksportów w zalogowanym kontekście.

    System pobiera faktury rosnąco według daty określonej w filtrze (Invoicing, Issue, PermanentStorage)
    i dodaje je do paczki aż do osiągnięcia jednego z poniższych limitów:
    * Limit liczby faktur: 10 000 sztuk
    * Limit rozmiaru danych(skompresowanych): 1GB

    Paczka eksportu zawiera dodatkowy plik z metadanymi faktur w formacie JSON (`_metadata.json`).
    Zawartość pliku to
    obiekt z tablicą <b>invoices</b>, gdzie każdy element jest obiektem typu <b>InvoiceMetadata</b>
    (taki jak zwracany przez endpoint `POST /invoices/query/metadata`).

    <b>Plik z metadanymi(_metadata.json) nie jest wliczany do limitów algorytmu budowania paczki</b>.

    `Do realizacji pobierania przyrostowego należy stosować filtrowanie po dacie PermanentStorage`.

    **Sortowanie:**

    - permanentStorageDate | invoicingDate | issueDate (Asc) - pole wybierane na podstawie filtrów



    **Wymagane uprawnienia**: `InvoiceRead`.

    Args:
        body (InvoiceExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, ExportInvoicesResponse]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InvoiceExportRequest,

) -> Response[Union[Any, ExceptionResponse, ExportInvoicesResponse]]:
    """ Eksport paczki faktur

     Rozpoczyna asynchroniczny proces wyszukiwania faktur w systemie KSeF na podstawie przekazanych
    filtrów oraz przygotowania ich w formie zaszyfrowanej paczki.
    Wymagane jest przekazanie informacji o szyfrowaniu w polu <b>Encryption</b>, które służą do
    zabezpieczenia przygotowanej paczki z fakturami.
    Maksymalnie można uruchomić 10 równoczesnych eksportów w zalogowanym kontekście.

    System pobiera faktury rosnąco według daty określonej w filtrze (Invoicing, Issue, PermanentStorage)
    i dodaje je do paczki aż do osiągnięcia jednego z poniższych limitów:
    * Limit liczby faktur: 10 000 sztuk
    * Limit rozmiaru danych(skompresowanych): 1GB

    Paczka eksportu zawiera dodatkowy plik z metadanymi faktur w formacie JSON (`_metadata.json`).
    Zawartość pliku to
    obiekt z tablicą <b>invoices</b>, gdzie każdy element jest obiektem typu <b>InvoiceMetadata</b>
    (taki jak zwracany przez endpoint `POST /invoices/query/metadata`).

    <b>Plik z metadanymi(_metadata.json) nie jest wliczany do limitów algorytmu budowania paczki</b>.

    `Do realizacji pobierania przyrostowego należy stosować filtrowanie po dacie PermanentStorage`.

    **Sortowanie:**

    - permanentStorageDate | invoicingDate | issueDate (Asc) - pole wybierane na podstawie filtrów



    **Wymagane uprawnienia**: `InvoiceRead`.

    Args:
        body (InvoiceExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, ExportInvoicesResponse]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: InvoiceExportRequest,

) -> Optional[Union[Any, ExceptionResponse, ExportInvoicesResponse]]:
    """ Eksport paczki faktur

     Rozpoczyna asynchroniczny proces wyszukiwania faktur w systemie KSeF na podstawie przekazanych
    filtrów oraz przygotowania ich w formie zaszyfrowanej paczki.
    Wymagane jest przekazanie informacji o szyfrowaniu w polu <b>Encryption</b>, które służą do
    zabezpieczenia przygotowanej paczki z fakturami.
    Maksymalnie można uruchomić 10 równoczesnych eksportów w zalogowanym kontekście.

    System pobiera faktury rosnąco według daty określonej w filtrze (Invoicing, Issue, PermanentStorage)
    i dodaje je do paczki aż do osiągnięcia jednego z poniższych limitów:
    * Limit liczby faktur: 10 000 sztuk
    * Limit rozmiaru danych(skompresowanych): 1GB

    Paczka eksportu zawiera dodatkowy plik z metadanymi faktur w formacie JSON (`_metadata.json`).
    Zawartość pliku to
    obiekt z tablicą <b>invoices</b>, gdzie każdy element jest obiektem typu <b>InvoiceMetadata</b>
    (taki jak zwracany przez endpoint `POST /invoices/query/metadata`).

    <b>Plik z metadanymi(_metadata.json) nie jest wliczany do limitów algorytmu budowania paczki</b>.

    `Do realizacji pobierania przyrostowego należy stosować filtrowanie po dacie PermanentStorage`.

    **Sortowanie:**

    - permanentStorageDate | invoicingDate | issueDate (Asc) - pole wybierane na podstawie filtrów



    **Wymagane uprawnienia**: `InvoiceRead`.

    Args:
        body (InvoiceExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, ExportInvoicesResponse]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
