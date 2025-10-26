<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:upo="http://upo.schematy.mf.gov.pl/KSeF/v4-2" xmlns:xs="http://www.w3.org/2001/XMLSchema" version="1.0">
	<xsl:output version="1.0" encoding="UTF-8"/>
	<xsl:template match="/">
		<html lang="pl">
			<head>
				<title>Urzędowe Potwierdzenie Odbioru</title>
				<meta charset="utf-8"/>
				<style>
                    .upo {
                        font-family: 'Arial', sans-serif;
                        max-width: 1200px;
                        padding: 20px; 
                        margin: 20px auto; 
                        font-size: 11pt;
                        background-color: #F2F2F2; 
                        border: 1px solid black; 
                        box-sizing: border-box; 
                    }
                    .tyt {
                        margin-bottom: 20px;
                        text-align: center;
                        width: 80%;
                        font-size: 16pt;
                        display: inline-block;
                    }
                    .sek {
                        background-color: #E7E7E7;
                        border: 2px solid black;
                        text-align: left;
                        margin-bottom: -2px
                    }
                    .seh {
                        font-weight: bold
                    }
                    .inf {
                        font-size: 10pt;
                        padding-bottom: 10px;
                    }
                    .pol {
                        border-top: 2px solid black;
                        border-left: 1px solid black;
                        background-color: white;
                    }
                    .p50 {
                        display: table-cell;
                        width: 600px;
                    }
                    .ety {
                        text-align: left;
                        font-size: 10pt;
                        padding: 3px;
                        color: black
                    }
                    .war {
                        text-align: center;
                        font-size: 16px;
                        padding-top: 15px;
                        padding-bottom: 10px;
                        word-wrap: break-word;
                        white-space: normal;
                    }
                    .brl {
                        border-left: 2px solid black;
                    }
                    .nip {
                        padding-right: 50px;
                    }
                    .stc {
                        padding-bottom: 30px;
                    }
                    .wyd {
                        text-align: left;
                        font-size: 10pt;
                    }
                    .wer {
                        float: right;
                    }
                    .we2 {
                        font-size: 11pt;
                        border: 2px solid black;
                        display: table-cell;
                        padding: 2px;
                        width: 100px;
                        text-align: center;
                    }
                    .nbr {
                        border-right: none;
                    }
                    .b {
                        font-weight: bold;
                    }
                    table {
                        border-collapse: collapse;
                        width: 100%; /* Ensure the table takes the full width */
                        table-layout: fixed; /* Ensure the columns have fixed widths */
                    }
                    th {
					    font-size: 14px;
					    background-color: #E7E7E7;
                    }
					td {
                        font-size: 13pt; /* wielkość czcionki pól tabeli */
                        padding: 4px;
                    }
                    th, td {
                        border: 1px solid black;
                        word-wrap: break-word; /* Ensure the text wraps within the cell */
                        white-space: normal; /* Ensure the text wraps within the cell */
                    }
                    th.column1 { width: 3%; }
					th.column2 { width: 10%; }  
                    th.column3 { width: 20%; }
                    th.column4 { width: 10%; }
                    th.column5 { width: 20%; }
                    th.column6 { width: 20%; }
                    th.column7 { width: 17%; }
                </style>
			</head>
			<body>
				<div class="upo">
					<div>
						<div class="tyt" style="display: inline-block;width: 136px;">
                            Krajowy System
                            <br/>
							<span style="font-weight:bold;font-size:34px;">
								<span style="color:red">e</span>-Faktur</span>
						</div>
						<div class="tyt">
                            URZĘDOWE POŚWIADCZENIE ODBIORU DOKUMENTU
                            <br/>
                            ELEKTRONICZNEGO KSeF
                        </div>
					</div>
					<xsl:apply-templates select="upo:Potwierdzenie"/>
				</div>
			</body>
		</html>
	</xsl:template>
	<xsl:template match="upo:Potwierdzenie">
		<div class="sek">
			<div class="seh">A. PEŁNA NAZWA PODMIOTU, KTÓREMU DORĘCZONO DOKUMENT ELEKTRONICZNY</div>
			<div class="pol">
				<div class="war b">
					<xsl:value-of select="upo:NazwaPodmiotuPrzyjmujacego"/>
				</div>
			</div>
		</div>
		<div class="sek">
			<div class="seh">B. INFORMACJA O DOKUMENCIE</div>
			<div class="inf">Dokument został zarejestrowany w systemie teleinformatycznym Ministerstwa Finansów</div>
			<div class="pol">
				<div class="p50">
					<div class="ety">Identyfikator dokumentu przesłanego do KSeF:</div>
					<div class="war">
						<xsl:value-of select="upo:NumerReferencyjnySesji"/>
					</div>
				</div>
				<div class="p50 brl">
					<div class="ety">Identyfikator podatkowy podmiotu (Uwierzytelnionego):</div>
					<div class="war b">
						<xsl:value-of select="upo:Uwierzytelnienie/upo:IdKontekstu/upo:Nip"/>
					</div>
				</div>
			</div>
			<div class="pol">
				<div class="ety">Wartość funkcji skrótu dokumentu w postaci otrzymanej przez system (łącznie z podpisem elektronicznym):</div>
				<div class="war">
					<xsl:value-of select="upo:Uwierzytelnienie/upo:SkrotDokumentuUwierzytelniajacego"/>
				</div>
			</div>
			<div class="pol">
				<div class="ety">Nazwa pliku XSD struktury logicznej dotycząca przesłanego dokumentu:</div>
				<div class="war">
					<xsl:value-of select="upo:NazwaStrukturyLogicznej"/>
				</div>
			</div>
			<div class="pol">
				<div class="ety">Kod formularza przedłożonego dokumentu elektronicznego:</div>
				<div class="war">
					<xsl:value-of select="upo:KodFormularza"/>
				</div>
			</div>
			<div class="pol">
				<table>
					<thead>
						<tr>
							<th class="column1">Lp.</th>
							<th class="column2">Nip Sprzedawcy</th>
							<th class="column3">Numer identyfikujący fakturę<br/>w Krajowym Systemie<br/>e-Faktur (KSeF)</th>
							<th class="column4">Numer faktury</th>
							<th class="column5">Data przesłania dokumentu do systemu informatycznego Ministerstwa Finansów</th>
							<th class="column6">Data nadania numeru KSeF w systemie informatycznym Ministerstwa Finansów</th>
							<th class="column7">Wartość funkcji skrótu złożonego dokumentu</th>
						</tr>
					</thead>
					<tbody>
						<xsl:for-each select="upo:Dokument">
							<tr>
								<td class="war">
									<xsl:number/>
								</td>
								<td class="war">
									<xsl:value-of select="upo:NipSprzedawcy"/>
								</td>
								<td class="war">
									<xsl:value-of select="upo:NumerKSeFDokumentu"/>
								</td>
								<td class="war">
									<xsl:value-of select="upo:NumerFaktury"/>
								</td>
								<td class="war">
									<xsl:value-of select="upo:DataPrzeslaniaDokumentu"/>
								</td>
								<td class="war">
									<xsl:value-of select="upo:DataNadaniaNumeruKSeF"/>
								</td>
								<td class="war">
									<xsl:value-of select="upo:SkrotDokumentu"/>
								</td>
							</tr>
						</xsl:for-each>
					</tbody>
				</table>
			</div>
		</div>
	</xsl:template>
</xsl:stylesheet>
