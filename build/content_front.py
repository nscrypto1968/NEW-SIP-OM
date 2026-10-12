# -*- coding: utf-8 -*-
"""Preliminary pages of the report."""

from docgen import Doc, BODY_SIZE


def title_page(doc, media):
    """The title page, laid out like the approved reference report."""
    logo = media['logo'] if 'logo' in media else None
    doc.blank(1)
    doc.para('DES\u2019S NAVINCHANDRA MEHTA INSTITUTE OF TECHNOLOGY AND '
             'DEVELOPMENT,', size=BODY_SIZE, bold=True, align='center')
    doc.para('MUMBAI \u2013 400028', size=BODY_SIZE, bold=True, align='center')
    if logo:
        doc.image(logo, 1.30, 1.23, before=120, after=120)
    else:
        doc.blank(1)
    doc.para('SUMMER INTERNSHIP REPORT ON', bold=True, align='center',
             before=120)
    doc.para('\u201c FUNDAMENTAL ANALYSIS OF THE FMCG SECTOR \u201c', bold=True,
             align='center')
    doc.para('(With Internship Exposure to Equity Dealing, the Futures and '
             'Options Market and Trading Terminals at Rosy Blue Securities '
             'Pvt. Ltd.)', size=11.0, bold=True, align='center', before=60)
    doc.para('Submitted in partial fulfilment for the award of the degree of',
             bold=True, align='center', before=160)
    doc.para('MASTER OF MANAGEMENT STUDIES', bold=True, align='center')
    doc.para('FINANCE', bold=True, align='center')
    doc.para('UNIVERSITY OF MUMBAI', bold=True, align='center')
    doc.para('Submitted by', bold=True, align='center', before=160)
    doc.para('Nikhil [ADD: full name as per institute records]', bold=True,
             align='center')
    doc.para('ROLL NO :- [ADD: roll number]', bold=True, align='center')
    doc.para('2025-2027', bold=True, align='center')
    doc.para('Under The Guidance of', bold=True, align='center', before=160)
    doc.para('DR. RAHUL N. WADEKAR', bold=True, align='center')


def certificate(doc):
    doc.new_page()
    doc.para('CERTIFICATE', bold=True, align='center', size=BODY_SIZE)
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
        align='both', before=160)
    doc.blank(4.0)
    doc.para('-------------------------                                        '
             '                                -------------------------',
             align='left')
    doc.para('Dr. Rasika Mallya                                                    '
             '                                        Dr. Rahul Wadekar',
             bold=True, align='left')
    doc.para('DIRECTOR                                                             '
             '                                            PROJECT GUIDE',
             bold=True, align='left')
    doc.blank(3.0)
    doc.para('EXTERNAL EXAMINER', bold=True, align='left')


def declaration(doc):
    doc.new_page()
    doc.para('DECLARATION', bold=True, align='center')
    doc.para(
        'I, Nikhil [ADD: full name], Roll No. [ADD: roll number], a student of '
        'the Master of Management Studies (Finance) programme of the '
        'University of Mumbai, hereby declare that this project report '
        'submitted by me to the partial fulfilment of the requirement for the '
        'award of Master of Management Studies (MMS) of the University of '
        'Mumbai is a bonafide work undertaken by me and it is not submitted to '
        'any other University or Institute for the award of any degree, '
        'diploma or certificate, or published at any time before.',
        align='both', before=160)
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
        align='both', before=120)
    doc.blank(3.0)
    doc.para('Name :  Nikhil [ADD: full name]                                        '
             'Signature', align='left')
    doc.para('Roll No. [ADD: roll number]                                        '
             '(Nikhil [ADD: full name])', align='left')


def acknowledgement(doc):
    doc.new_page()
    doc.para('ACKNOWLEDGEMENT', bold=True, align='center')
    doc.para(
        'This project has been a valuable learning experience, and I am '
        'grateful to everyone who supported me through it. I extend my sincere '
        'thanks to our Director, Dr. Rasika Mallya, and to my internal project '
        'guide, Dr. Rahul N. Wadekar, whose guidance, patient review and '
        'constructive suggestions shaped this report. The insistence that '
        'every figure be traced to a verifiable source, and that every table '
        'be followed by an interpretation rather than a restatement, has '
        'improved both the discipline and the usefulness of this work.',
        align='both', before=120)
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
    doc.blank(1.0)
    doc.para('Nikhil [ADD: full name]', bold=True, align='right')


def executive_summary(doc):
    doc.new_page()
    doc.para('EXECUTIVE SUMMARY', bold=True, align='center')
    para = lambda t: doc.para(t, align='both', before=120)
    para(
        'Summer training is an important part of management education because '
        'it places the student inside the activity being studied rather than '
        'outside it. This report combines the two components required of the '
        'internship: a record of the work performed on the equity dealing desk '
        'of Rosy Blue Securities Pvt. Ltd. in the capacity of an Equity '
        'Dealer, and a fundamental analysis of the Indian fast-moving consumer '
        'goods sector with a comparative study of three listed companies.')
    para(
        'The operational component of the report documents the dealing '
        'function as it operates on a stock broker\u2019s desk. It covers the '
        'structure of the Indian secondary market, the trading mechanism on '
        'the exchange-provided terminal and on the member\u2019s '
        'Computer-to-Computer Link facility, the margining framework in the '
        'cash and equity derivatives segments, the settlement cycle, and the '
        'ladder of statutory charges that applies to every executed trade. The '
        'report records the working day of a dealer, the order types used in '
        'practice, the pre-trade risk checks applied before an order leaves '
        'the member\u2019s server, and the post-trade reconciliation performed '
        'at the close of the session. Six worked examples convert this '
        'description into computed evidence: a cost-of-carry valuation of an '
        'illustrative futures contract, a five-day mark-to-market settlement '
        'sequence, a Black-Scholes valuation of an illustrative option with '
        'its sensitivities, a margin build-up and shortfall scenario, and the '
        'charge computation on illustrative delivery and intraday round trips.')
    para(
        'The analytical component applies fundamental analysis to the Indian '
        'FMCG sector. The sector is the fourth largest in the Indian economy, '
        'employs around three million people and is valued at approximately '
        'Rs. 25 lakh crore, with household and personal care contributing half '
        'of all sales. Three companies with a March financial year end were '
        'selected for comparative study: Hindustan Unilever Ltd., Britannia '
        'Industries Ltd. and Dabur India Ltd. Their financial statements for '
        'FY2023-24, FY2024-25 and FY2025-26 were analysed using thirteen '
        'ratios covering profitability, returns, liquidity, leverage, '
        'efficiency and market valuation, and the three were ranked on those '
        'ratios in a factor analysis.')
    para(
        'The analysis finds that Britannia Industries is the strongest '
        'performer on profitability and capital efficiency, recording a net '
        'profit margin of 13.25 per cent, a return on capital employed of '
        '52.63 per cent and a return on equity of 49.68 per cent in FY2025-26. '
        'Hindustan Unilever has the most conservative financial structure, '
        'being effectively debt free, with the lowest operating ratio and the '
        'highest interest coverage in the group, but its underlying earnings '
        'were almost flat in FY2025-26 once the one-time gain of '
        'Rs. 4,611 crore from the demerger of its ice cream undertaking is '
        'excluded. Dabur India has the strongest short-term liquidity position '
        'and the lowest market valuation, but its revenue and profit growth '
        'over the three years has been the slowest and its earnings per share '
        'has grown at 1.34 per cent a year. On the composite ranking of '
        'thirteen ratios, Hindustan Unilever scores 120 points, Britannia 117 '
        'and Dabur 114, a narrow spread that reflects the trade-off between '
        'financial safety and growth rather than a clear overall winner.')
    para(
        'The report concludes that fundamental analysis identifies differences '
        'in the quality of performance rather than a single superior company, '
        'and that on a dealing desk the same security is assessed on an '
        'entirely different set of attributes, principally price band, '
        'liquidity and volatility. The main learning of the internship is that '
        'the analytical and operational views are complementary and must be '
        'held together. The analysis in this report is academic and does not '
        'constitute investment advice.')
