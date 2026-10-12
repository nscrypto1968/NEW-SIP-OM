# -*- coding: utf-8 -*-
"""Preliminary pages of the report.

The layout follows the approved reference report line for line:  the title
page is built from centred bold 12 pt paragraphs spaced by blank paragraphs,
the certificate carries the institute's letterhead, and each of the remaining
preliminary pages opens with a centred title -- 12 pt for CERTIFICATE and
DECLARATION, 14 pt for ACKNOWLEDGEMENT and EXECUTIVE SUMMARY.
"""

from docgen import Doc, BODY_SIZE

BIG = 14.0
TITLE_BEFORE = 200
TITLE_AFTER = 120


def _c(doc, text, size=BODY_SIZE, before=0, after=80):
    """A centred bold line, the way every line of the title page is set."""
    return doc.para(text, size=size, bold=True, align='center',
                    before=before, after=after)


def _front_title(doc, text, size=BODY_SIZE):
    """The title of a preliminary page:  centred, bold, keepNext."""
    return doc.para(text, size=size, bold=True, align='center',
                    before=TITLE_BEFORE, after=TITLE_AFTER, keep_next=True)


def _spacers(doc, n):
    for _ in range(n):
        doc.para('', after=0)


def title_page(doc, media):
    """The title page, laid out like the approved reference report."""
    logo = media['logo'] if 'logo' in media else None
    _spacers(doc, 3)
    _c(doc, 'DES\u2019S NAVINCHANDRA MEHTA INSTITUTE OF TECHNOLOGY AND '
            'DEVELOPMENT,')
    _c(doc, 'MUMBAI \u2013 400028')
    _spacers(doc, 1)
    if logo:
        doc.image(logo, 2.20, 1.98, before=0, after=0)
    else:
        _spacers(doc, 1)
    _spacers(doc, 1)
    _c(doc, 'SUMMER INTERNSHIP REPORT ON')
    _spacers(doc, 1)
    _c(doc, '\u201c FUNDAMENTAL ANALYSIS OF THE FMCG SECTOR \u201c')
    _spacers(doc, 1)
    _c(doc, 'Submitted in partial fulfilment for the award of the degree of')
    _spacers(doc, 1)
    _c(doc, 'MASTER OF MANAGEMENT STUDIES')
    _c(doc, 'FINANCE')
    _c(doc, 'UNIVERSITY OF MUMBAI')
    _c(doc, 'Submitted by')
    _c(doc, 'Nikhil [ADD: full name as per institute records]')
    _c(doc, 'ROLL NO :- [ADD: roll number]')
    _c(doc, '2025-2027')
    _c(doc, 'Under The Guidance of')
    _c(doc, 'DR. RAHUL N. WADEKAR')


def certificate(doc, media=None):
    """The certificate page, carrying the institute's letterhead."""
    doc.new_page()
    letterhead = media['letterhead'] if media is not None and 'letterhead' in media else None
    if letterhead:
        doc.image(letterhead, 7.27, 1.92, before=0, after=0)
    _spacers(doc, 1)
    _front_title(doc, 'CERTIFICATE')
    doc.para(
        'This is to certify that the summer internship report titled '
        '\u201cFundamental Analysis of the FMCG Sector\u201d submitted in '
        'partial fulfilment for the MMS Degree Examination by Nikhil '
        '[ADD: full name], Roll No. [ADD: roll number], is a record of '
        'research work carried out by the student during the period from '
        '[ADD: internship start date] to [ADD: internship end date] under my '
        'guidance, and has been found satisfactory. This project work is '
        'original and not submitted earlier for the award of any degree, '
        'diploma or associateship of any other University/Institute.',
        align='both')
    _spacers(doc, 6)
    doc.para('-------------------------                                        '
             '                                -------------------------',
             align='both')
    doc.para('Dr. Rasika Mallya                                                    '
             '                                        Dr. Rahul Wadekar',
             align='both')
    doc.para('DIRECTOR                                                             '
             '                                            PROJECT GUIDE',
             align='both')
    _spacers(doc, 2)
    doc.para('EXTERNAL EXAMINER', bold=True, align='both')


def declaration(doc):
    doc.new_page()
    _front_title(doc, 'DECLARATION')
    doc.para(
        'I, Nikhil [ADD: full name], Roll No. [ADD: roll number], a student of '
        'the Master of Management Studies (Finance) programme of the '
        'University of Mumbai, hereby declare that this project report '
        'submitted by me to the partial fulfilment of the requirement for the '
        'award of Master of Management Studies (MMS) of the University of '
        'Mumbai is a bonafide work undertaken by me and it is not submitted to '
        'any other University or Institute for the award of any degree, '
        'diploma or certificate, or published at any time before.',
        align='both')
    doc.para(
        'The report is based on my own learning and observation during the '
        'summer internship undertaken at Rosy Blue Securities Pvt. Ltd. in the '
        'capacity of an Equity Dealer, together with information drawn from '
        'publicly available documents of the stock exchanges, the Securities '
        'and Exchange Board of India, the Reserve Bank of India and the annual '
        'reports of the companies analysed. Confidential information of the '
        'firm, including client names, client codes, permanent account '
        'numbers, unique client codes, terminal identifiers and the firm\u2019s '
        'internal financial data, has not been disclosed. All trading examples '
        'given in this report are illustrative and are identified as such. The '
        'fundamental analysis of the FMCG sector has been carried out for '
        'academic purposes only and does not constitute investment advice.',
        align='both')
    _spacers(doc, 6)
    doc.para('Name :  Nikhil [ADD: full name]                                   '
             '          Signature', align='both')
    doc.para('Roll No. [ADD: roll number]                                      '
             '          (Nikhil [ADD: full name])', align='both')


def acknowledgement(doc):
    doc.new_page()
    _front_title(doc, 'ACKNOWLEDGEMENT', size=BIG)
    doc.para(
        'This project has been a valuable learning experience, and I am '
        'grateful to everyone who supported me through it. I extend my sincere '
        'thanks to our Director, Dr. Rasika Mallya, and to my internal project '
        'guide, Dr. Rahul N. Wadekar, whose guidance, patient review and '
        'constructive suggestions shaped this report. The insistence that '
        'every figure be traced to a verifiable source, and that every table '
        'be followed by an interpretation rather than a restatement, has '
        'improved both the discipline and the usefulness of this work.',
        align='both')
    doc.para(
        'I am grateful to my parents and to my friends for their encouragement '
        'and patience during the internship and the writing of this report. '
        'Their support made it possible to combine the demands of a live '
        'dealing desk, which begins well before the market opens, with the '
        'requirements of academic study.', align='both')
    doc.para(
        'I thank the management of Rosy Blue Securities Pvt. Ltd. for granting '
        'me the opportunity to work in the equity dealing function, and the '
        'seniors on the dealing desk, the risk management team and the '
        'back-office staff who explained processes, corrected my errors and '
        'allowed me to observe live operations. I also thank the faculty '
        'members of the Finance specialisation and the library staff of '
        'DES\u2019s NMITD for the academic and infrastructural support extended '
        'during the programme.', align='both')
    doc.para(
        'Finally, I am grateful to everyone who contributed indirectly to this '
        'project. Any error that remains in this report is my own.',
        align='both')
    _spacers(doc, 1)
    doc.para('Nikhil [ADD: full name]', bold=True, align='right')


def executive_summary(doc):
    doc.new_page()
    _front_title(doc, 'EXECUTIVE SUMMARY', size=BIG)
    para = lambda t: doc.para(t, align='both')
    para(
        'Summer training places the student inside the activity being studied '
        'rather than outside it. This report combines the two components '
        'required of the internship: a record of the work performed on the '
        'equity dealing desk of Rosy Blue Securities Pvt. Ltd. as an Equity '
        'Dealer, and a fundamental analysis of the Indian FMCG sector with a '
        'comparative study of three listed companies.')
    para(
        'The operational component documents the dealing function as it '
        'operates on a stock broker\u2019s desk: the structure of the Indian '
        'secondary market, the trading mechanism on the exchange terminal and '
        'on the member\u2019s Computer-to-Computer Link facility, the '
        'margining framework, the settlement cycle and the statutory charges '
        'on every executed trade. It also records the working day of a dealer, '
        'the pre-trade risk checks applied before an order leaves the '
        'member\u2019s server, and the reconciliation at the close of the '
        'session. Six worked examples convert this into computed evidence: a '
        'cost-of-carry valuation of a futures contract, a five-day '
        'mark-to-market settlement, a Black-Scholes valuation of an option, a '
        'margin shortfall scenario, and the charges on illustrative delivery '
        'and intraday trades.')
    para(
        'The analytical component applies fundamental analysis to the Indian '
        'FMCG sector, valued at approximately Rs. 25 lakh crore, with '
        'household and personal care contributing half of all sales and '
        'direct employment of about three million people. Three companies '
        'with a March year end were selected: Hindustan Unilever Ltd., '
        'Britannia Industries Ltd. and Dabur India Ltd. Their financial '
        'statements for FY2023-24 to FY2025-26 were analysed using thirteen '
        'ratios covering profitability, returns, liquidity, leverage, '
        'efficiency and valuation, and ranked in a factor analysis.')
    para(
        'The analysis finds that Britannia Industries is the strongest '
        'performer on profitability and capital efficiency, with a net profit '
        'margin of 13.25 per cent, a return on capital employed of 52.63 per '
        'cent and a return on equity of 49.68 per cent in FY2025-26. '
        'Hindustan Unilever has the most conservative financial structure, '
        'being effectively debt free with the lowest operating ratio and the '
        'highest interest coverage in the group, but its underlying earnings '
        'were almost flat in FY2025-26 once the one-time gain of '
        'Rs. 4,611 crore from the demerger of its ice cream undertaking is '
        'excluded. Dabur India has the strongest liquidity and the lowest '
        'market valuation, but the slowest revenue and profit growth over the '
        'three years. On the composite ranking of thirteen ratios, Hindustan '
        'Unilever scores 120 points, Britannia 117 and Dabur 114.')
    para(
        'The report concludes that fundamental analysis identifies differences '
        'in the quality of performance rather than a single superior company, '
        'and that on a dealing desk a security is assessed on different '
        'attributes: price band, liquidity and volatility. The analysis in '
        'this report is academic and does not constitute investment advice.')
