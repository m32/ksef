<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet 
xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
xmlns:v42="http://upo.schematy.mf.gov.pl/KSeF/v4-2" 
xmlns:v43="http://upo.schematy.mf.gov.pl/KSeF/v4-3" 
xmlns:xs="http://www.w3.org/2001/XMLSchema" version="1.0">
	<xsl:variable name="ns" select="namespace-uri(/*)"/>
	<xsl:output version="1.0" encoding="UTF-8"/>
	<xsl:template match="/">
		<html lang="pl">
			<head>
				<title>Urzędowe Potwierdzenie Odbioru</title>
				<meta charset="utf-8"/>
				<style>

					.upo {
						font-family: 'Arial', sans-serif;
						max-width: 800px;
						padding: 5px; 
						margin: 3px auto; 
						font-size: 12pt;
						background-color: #F2F2F2; 
						border: 2px solid black;
						box-sizing: border-box;
					}
					.tyt1 {
						margin-bottom: 10px;
						display: inline-block;
						white-space: nowrap;
						text-align: left;
					}
					.tyt2 {
						font-size: 10pt;
						margin-bottom: 10px;
						text-align: center;
					}
					.seka {
						background-color: #E7E7E7;
						border-top: 1px solid black; 
						text-align: left;
						margin-bottom: -4px;
					}
					.sekb {
						background-color: #E7E7E7;
						border-top: 1px solid black; 
						text-align: left;
					}
					.seh {
						font-size: 12pt;
						font-weight:bold;
						padding-left: 4px;
						padding-top: 2px;
						padding-bottom: 2px;
					}
					td.pol {
						background-color: white;
					}
					.inf {
						text-align: center;
						font-size: 10pt;
						padding-bottom: 10px;
					}
					.ety {
						text-align: left;
						font-size: 8pt;
						padding: 4px;
						font-weight: bold;
						color: black;
					}
					.war {
						text-align: center;
						font-size: 9pt;
						padding-top: 10px;
						padding-bottom: 10px;
						word-wrap: break-word;
						white-space: normal;
					}
					.wart {
						text-align: center;
						font-size: 7pt;
						padding-top: 4px;
						padding-bottom: 4px;
						word-wrap: break-word;
						white-space: normal;
					}
					.b {
						font-weight: bold; 
					}
					.tab1 {
						margin-right: 0px; 
						margin-left: 0px;
						width: calc(100%); 
					}
					.tab2 {
						background-color: white;
						margin-top: -1px;	
						margin-bottom: 0px;
						margin-right: 0px; 
						margin-left: 0px;
						width: calc(100%); 
					}
					table {
						border-collapse: collapse;
						width: 100%; /* Ensure the table takes the full width */
						table-layout: fixed; /* Ensure the columns have fixed widths */	
					}
					th {
						font-size: 8pt;
						background-color: #E7E7E7;
					}
					td {
						font-size: 8pt; /* wielkość czcionki pól tabeli */
						padding: 2px;
					}
					th, td {
						border: 2px solid black;
						word-wrap: break-word; /* Ensure the text wraps within the cell */
						white-space: normal; /* Ensure the text wraps within the cell */
					}
			@media print {
						* {
							-webkit-print-color-adjust: exact !important;
							print-color-adjust: exact !important;
							color-adjust: exact !important;
						}
						th, td {border: 1px solid black;}
					}
					
			@media screen {
						
						body {
							zoom: 1.5; /* 190% */
							transform-origin: top left;
						     }
					.upo {font-size: 9pt;}
					.tyt2 {font-size: 9pt;}
					.seh {font-weight: normal; font-size: 9pt;}
					.inf {font-size: 8pt;}
					.ety {font-weight: normal;}
					.war {font-size: 8pt;}
					th {font-size: 7pt; font-weight: 600;}
					th, td {border: 1px solid black;}			     
				     }					
				</style>
				<xsl:if test="$ns = 'http://upo.schematy.mf.gov.pl/KSeF/v4-2'">
					<style>
						th.column1 { width: 4%; }
						th.column2 { width: 19%; }
						th.column3 { width: 10%; }
						th.column4 { width: 11%; }
						th.column5 { width: 10%; }
						th.column6 { width: 11%; }
						th.column7 { width: 11%; }
						th.column8 { width: 24%; }
					</style>
				</xsl:if>
				<xsl:if test="$ns = 'http://upo.schematy.mf.gov.pl/KSeF/v4-3'">
					<style>
						th.column1 { width: 3%; }
						th.column2 { width: 18%; }
						th.column3 { width: 10%; }
						th.column4 { width: 10%; }
						th.column5 { width: 10%; }
						th.column6 { width: 11%; }
						th.column7 { width: 11%; }
						th.column8 { width: 21%; }
						th.column9 { width: 6%; }
					</style>
				</xsl:if>
				
			</head>
			<body>
				<div class="upo">
					<div>
						<div class="tyt1" style="display: inline-block; white-space: nowrap;">
							Krajowy System <span style="font-weight: bold; font-size: 28px;"><span style="color: red;">e</span>-Faktur</span>
						</div>
						<br/>
						<div class="tyt2 b">
                            URZĘDOWE POŚWIADCZENIE ODBIORU DOKUMENTU ELEKTRONICZNEGO KSeF
                        </div>
					</div>
					<xsl:apply-templates select="v42:Potwierdzenie | v43:Potwierdzenie"/>
				</div>
			</body>
		</html>
	</xsl:template>
	<xsl:template match="v42:Potwierdzenie | v43:Potwierdzenie">
		<div class="seka">
			<table class="tab1">
				<tr>
					<td>
						<div class="seh">A. PEŁNA NAZWA PODMIOTU, KTÓREMU DORĘCZONO DOKUMENT ELEKTRONICZNY</div>
					</td>
				</tr>
				<tr>
					<td class="pol">
						<div class="war b">
							<xsl:value-of select="v42:NazwaPodmiotuPrzyjmujacego | v43:NazwaPodmiotuPrzyjmujacego"/>
						</div>
					</td>
				</tr>				
			</table>
		</div>
		<div class="sekb">
			<table class="tab1">
				<colgroup>
					<col style="background-color: #E7E7E7; width: 50%;"/>
					<col style="background-color: white; width: 50%;"/>
				</colgroup>
				<tr>
					<td colspan="2">
					<div class="seh">B. INFORMACJA O DOKUMENCIE</div>
					<div class="inf">Dokument został zarejestrowany w systemie teleinformatycznym Ministerstwa Finansów</div>
					</td>
				</tr>
				<tr>
					<td class="ety">Numer referencyjny sesji:</td>
					<td class="war b">
						<xsl:value-of select="v42:NumerReferencyjnySesji | v43:NumerReferencyjnySesji"/>
					</td>
				</tr>
				<tr>
					<td class="ety">Typ kontekstu:</td>
					<td class="war b">
						<xsl:choose>
							<xsl:when test="v42:Uwierzytelnienie/v42:IdKontekstu/v42:Nip | v43:Uwierzytelnienie/v43:IdKontekstu/v43:Nip">NIP</xsl:when>
							<xsl:when test="v42:Uwierzytelnienie/v42:IdKontekstu/v42:NipVatUe | v43:Uwierzytelnienie/v43:IdKontekstu/v43:NipVatUe">NIPVATUE</xsl:when>
							<xsl:when test="v42:Uwierzytelnienie/v42:IdKontekstu/v42:IdZlozonyVatUE | v43:Uwierzytelnienie/v43:IdKontekstu/v43:IdZlozonyVatUE">Identyfikator złożony</xsl:when>
							<xsl:when test="v42:Uwierzytelnienie/v42:IdKontekstu/v42:InternalId | v43:Uwierzytelnienie/v43:IdKontekstu/v43:InternalId">INTERNALID</xsl:when>
							<xsl:otherwise>Brak danych</xsl:otherwise>
						</xsl:choose>
					</td>
				</tr>
				<tr>
					<td class="ety">Identyfikator kontekstu uwierzytelnienia:</td>
					<td class="war b">
						<xsl:choose>
							<xsl:when test="v42:Uwierzytelnienie/v42:IdKontekstu/v42:Nip | v43:Uwierzytelnienie/v43:IdKontekstu/v43:Nip">
								<xsl:value-of select="v42:Uwierzytelnienie/v42:IdKontekstu/v42:Nip | v43:Uwierzytelnienie/v43:IdKontekstu/v43:Nip"/>
							</xsl:when>
							<xsl:when test="v42:Uwierzytelnienie/v42:IdKontekstu/v42:NipVatUe | v43:Uwierzytelnienie/v43:IdKontekstu/v43:NipVatUe">
								<xsl:value-of select="v42:Uwierzytelnienie/v42:IdKontekstu/v42:NipVatUe | v43:Uwierzytelnienie/v43:IdKontekstu/v43:NipVatUe"/>
							</xsl:when>
							<xsl:when test="v42:Uwierzytelnienie/v42:IdKontekstu/v42:IdZlozonyVatUE | v43:Uwierzytelnienie/v43:IdKontekstu/v43:IdZlozonyVatUE">
								<xsl:value-of select="v42:Uwierzytelnienie/v42:IdKontekstu/v42:IdZlozonyVatUE | v43:Uwierzytelnienie/v43:IdKontekstu/v43:IdZlozonyVatUE"/>
							</xsl:when>
							<xsl:when test="v42:Uwierzytelnienie/v42:IdKontekstu/v42:InternalId | v43:Uwierzytelnienie/v43:IdKontekstu/v43:InternalId">
								<xsl:value-of select="v42:Uwierzytelnienie/v42:IdKontekstu/v42:InternalId | v43:Uwierzytelnienie/v43:IdKontekstu/v43:InternalId"/>
							</xsl:when>
								<xsl:otherwise>Brak danych</xsl:otherwise>
						</xsl:choose>
					</td>
				</tr>
				<tr>
					<td class="ety">Nazwa pliku XSD struktury logicznej dotycząca przesłanego dokumentu:</td>
					<td class="war b">
						<xsl:value-of select="v42:NazwaStrukturyLogicznej | v43:NazwaStrukturyLogicznej"/>
					</td>
				</tr>
				<tr>
					<td class="ety">Kod formularza przedłożonego dokumentu elektronicznego:</td>
					<td class="war b">
						<xsl:value-of select="v42:KodFormularza | v43:KodFormularza"/>
					</td>
				</tr>
			</table>
			<div class="tab2">
				<xsl:if test="$ns = 'http://upo.schematy.mf.gov.pl/KSeF/v4-2'">
					<table>
						<thead>
							<tr>
								<th class="column1">Lp.</th>
								<th class="column2">Numer identyfikujący fakturę w KSeF</th>
								<th class="column3">Numer faktury</th>
								<th class="column4">NIP Sprzedawcy</th>
								<th class="column5">Data wystawienia faktury</th>
								<th class="column6">Data przesłania do KSeF</th>
								<th class="column7">Data nadania numeru KSeF</th>
								<th class="column8">Wartość funkcji skrótu złożonego dokumentu</th>
							</tr>
						</thead>
						<tbody>
							<xsl:for-each select="v42:Dokument">
								<tr>
									<td class="wart">
										<xsl:number/>
									</td>
									<td class="wart">
										<xsl:value-of select="v42:NumerKSeFDokumentu"/>
									</td>
									<td class="wart">
										<xsl:value-of select="v42:NumerFaktury"/>
									</td>
									<td class="wart">
										<xsl:value-of select="v42:NipSprzedawcy"/>
									</td>
									<td class="wart">						
										<xsl:value-of select="v42:DataWystawieniaFaktury"/>
									</td>
									<td class="wart">
										<xsl:value-of select="substring(v42:DataPrzeslaniaDokumentu, 1, 10)"/>
										<br/>
										<xsl:value-of select="substring(v42:DataPrzeslaniaDokumentu, 12, 8)"/>	
									</td>
									<td class="wart">
										<xsl:value-of select="substring(v42:DataNadaniaNumeruKSeF, 1, 10)"/>
										<br/>
										<xsl:value-of select="substring(v42:DataNadaniaNumeruKSeF, 12, 8)"/>
									</td>
									<td class="wart">
										<xsl:value-of select="v42:SkrotDokumentu"/>
									</td>
								</tr>
							</xsl:for-each>
						</tbody>
					</table>
				</xsl:if>
				<xsl:if test="$ns = 'http://upo.schematy.mf.gov.pl/KSeF/v4-3'">
					<table>
						<thead>
							<tr>
								<th class="column1">Lp.</th>
								<th class="column2">Numer identyfikujący fakturę w KSeF</th>
								<th class="column3">Numer faktury</th>
								<th class="column4">NIP Sprzedawcy</th>
								<th class="column5">Data wystawienia faktury</th>
								<th class="column6">Data przesłania do KSeF</th>
								<th class="column7">Data nadania numeru KSeF</th>
								<th class="column8">Wartość funkcji skrótu złożonego dokumentu</th>
								<th class="column9">Tryb wysyłki</th>
							</tr>
						</thead>
						<tbody>
							<xsl:for-each select="v43:Dokument">
								<tr>
									<td class="wart">
										<xsl:number/>
									</td>
									<td class="wart">
										<xsl:value-of select="v43:NumerKSeFDokumentu"/>
									</td>
									<td class="wart">
										<xsl:value-of select="v43:NumerFaktury"/>
									</td>
									<td class="wart">
										<xsl:value-of select="v43:NipSprzedawcy"/>
									</td>
									<td class="wart">						
										<xsl:value-of select="v43:DataWystawieniaFaktury"/>
									</td>
									<td class="wart">
										<xsl:value-of select="substring(v43:DataPrzeslaniaDokumentu, 1, 10)"/>
										<br/>
										<xsl:value-of select="substring(v43:DataPrzeslaniaDokumentu, 12, 8)"/>	
									</td>
									<td class="wart">
										<xsl:value-of select="substring(v43:DataNadaniaNumeruKSeF, 1, 10)"/>
										<br/>
										<xsl:value-of select="substring(v43:DataNadaniaNumeruKSeF, 12, 8)"/>
									</td>
									<td class="wart">
										<xsl:value-of select="v43:SkrotDokumentu"/>
									</td>
									<td class="wart">
										<xsl:value-of select="v43:TrybWysylki"/>
									</td>
								</tr>
							</xsl:for-each>
						</tbody>
					</table>
				</xsl:if>
				
				
			</div>
		</div>
	</xsl:template>
</xsl:stylesheet>
