# -*- coding: utf-8 -*-
"""References and bibliography."""

from docgen import Doc


REFERENCES = [
    'Annual Reports of Hindustan Unilever Limited for the financial years '
    '2023-24, 2024-25 and 2025-26.',
    'Annual Reports of Britannia Industries Limited for the financial years '
    '2023-24, 2024-25 and 2025-26.',
    'Annual Reports of Dabur India Limited for the financial years 2023-24, '
    '2024-25 and 2025-26.',
    'Hindustan Unilever Limited, audited consolidated financial statements '
    'and corporate announcements on the demerger of the ice cream '
    'undertaking, effective 1 December 2025.',
    'Britannia Industries Limited, audited consolidated financial statements '
    'and corporate announcements, 2024 to 2026.',
    'Dabur India Limited, audited consolidated financial statements and '
    'corporate announcements, 2024 to 2026.',
    'Securities and Exchange Board of India, www.sebi.gov.in \u2014 '
    'regulations, circulars and investor-protection material; accessed '
    '9 October 2026.',
    'National Stock Exchange of India Limited, www.nseindia.com \u2014 market '
    'information, contract specifications, margin framework and daily '
    'surveillance lists; accessed 9 October 2026.',
    'BSE Limited, www.bseindia.com \u2014 market information, contract '
    'specifications, margin framework and corporate announcements; accessed '
    '9 October 2026.',
    'Reserve Bank of India, www.rbi.org.in \u2014 monetary policy statement '
    'of August 2026 and database on the Indian economy; accessed September '
    'and October 2026.',
    'Ministry of Finance, Government of India \u2014 Economic Survey '
    '2025-26.',
    'India Brand Equity Foundation, Fast Moving Consumer Goods industry '
    'report, updated September 2026, www.ibef.org.',
    'Rosy Blue Securities Private Limited, www.rosybluesecurities.co.in '
    '\u2014 About Us and Our Services pages, giving the firm\u2019s '
    'SEBI registration number, corporate identity number, exchange '
    'memberships and registered office; accessed 12 October 2026.',
    'Ministry of Corporate Affairs, Government of India \u2014 company '
    'master data for Rosy Blue Securities Private Limited, CIN '
    'U65990MH1994PTC080450, as reproduced in the company data services '
    'of the Registrar of Companies; accessed 12 October 2026.',
    'NielsenIQ India, FMCG quarterly growth data as reported in the industry '
    'report of the India Brand Equity Foundation; accessed October 2026.',
    'National Securities Depository Limited and Central Depository Services '
    '(India) Limited \u2014 depository statistics, as on 31 August 2026.',
    'Hindustan Unilever Limited, Britannia Industries Limited and Dabur '
    'India Limited \u2014 official company websites, company profile, brand '
    'portfolio and investor-relations material.',
]

BIBLIO_HEADINGS = [
    ('Books and study material', [
        'Chandra, P. (2019). Investment Analysis and Portfolio Management. '
        'McGraw Hill Education.',
        'Kothari, C. R. (2019). Research Methodology: Methods and Techniques. '
        'New Age International Publishers.',
        'Hull, J. C. Options, Futures and Other Derivatives. Pearson.',
        'Bhole, L. M. and Mahakud, J. Financial Institutions and Markets. '
        'McGraw Hill Education.',
        'Pathak, B. V. The Indian Financial System: Markets, Institutions and '
        'Services. Pearson.',
        'National Institute of Securities Markets and NSE Academy '
        'certification workbooks on the capital market and the derivatives '
        'market, current editions.',
    ]),
    ('Regulations, circulars and rule books', [
        'Securities and Exchange Board of India Act, 1992.',
        'SEBI (Stock Brokers) Regulations, 1992, as amended.',
        'SEBI circular on the standardisation of the expiry day for equity '
        'derivative contracts, 2025.',
        'NSE and BSE circulars on the shift of the equity-derivative expiry '
        'day to Tuesday and Thursday respectively with effect from '
        '1 September 2025.',
        'Exchange circulars on Computer-to-Computer Link software approval, '
        'terminal registration and user identification.',
        'Exchange circulars on transaction charges for the capital market and '
        'the equity-derivatives segment.',
        'Finance Act provisions prescribing the securities transaction tax '
        'rates applicable from 1 April 2026.',
        'SEBI circulars on margining for cash and equity-derivatives segments, '
        'and on the upstreaming of client funds.',
    ]),
    ('Websites and online sources', [
        'Hindustan Unilever Limited. Company profile, brand portfolio, '
        'financial results and investor presentations.',
        'Britannia Industries Limited. Company profile, brand portfolio and '
        'financial results.',
        'Dabur India Limited. Company profile, business verticals and '
        'financial results.',
        'National Stock Exchange of India Limited. Company and market '
        'information, share price data and contract specifications.',
        'BSE Limited. Company information, shareholding patterns and share '
        'price data.',
        'Securities and Exchange Board of India. Regulations, circulars and '
        'investor education material.',
        'Reserve Bank of India. Macroeconomic and monetary policy '
        'information.',
        'India Brand Equity Foundation. Sector reports on fast moving '
        'consumer goods, food processing and related industries.',
        'Moneycontrol and Screener. Published financial statements, financial '
        'ratios and market information used for cross-checking the ratios '
        'computed in this report.',
        'Business news publications and company press releases, used only for '
        'corporate events reported during the study period.',
    ]),
]


def references(doc):
    doc.new_page()
    doc.chapter('REFERENCES / BIBLIOGRAPHY')
    doc.para('REFERENCES', bold=True, align='left', before=140)
    for i, item in enumerate(REFERENCES, 1):
        doc.para('%d.  %s' % (i, item), align='both', indent_left=200,
                 first_line=-200)
    doc.para('BIBLIOGRAPHY', bold=True, align='left', before=200)
    for head, items in BIBLIO_HEADINGS:
        doc.para(head, bold=True, align='left', before=140)
        for i, item in enumerate(items, 1):
            doc.para('%d.  %s' % (i, item), align='both', indent_left=200,
                     first_line=-200)
    doc.para(
        'Note on data: the financial statements used in this report are the '
        'audited consolidated statements of the three companies. Figures '
        'described as published are reproduced from those statements; figures '
        'described as the author\u2019s computation have been calculated from '
        'them using the formulas stated in Chapter 6. Illustrative figures in '
        'Chapter 2 are constructed by the author to demonstrate a mechanism '
        'and are not drawn from any of the sources listed above.',
        align='both', before=200)
