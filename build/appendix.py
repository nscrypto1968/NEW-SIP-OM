# -*- coding: utf-8 -*-
"""Appendix - a standalone company research report on Hindustan Unilever Ltd."""

from docgen import Doc


def appendix(doc, fig):
    doc.new_page()
    doc.para('APENDICES', bold=True, align='left')
    doc.mark('APENDICES', 1)
    doc.para('COMPANY RESEARCH & FUNDAMENTAL ANALYSIS REPORT OF HINDUSTAN '
             'UNILEVER LTD.', bold=True, align='center', before=140)
    doc.para(
        'This appendix reproduces, in the form of a standalone research '
        'report, the detailed work prepared on Hindustan Unilever Ltd. The '
        'company was selected for the standalone report because it is the '
        'largest of the three companies studied and because it is the only '
        'one of the three whose reported profit for FY2025-26 contains a '
        'one-time item, which makes it the most instructive of the three to '
        'work through line by line. All figures are consolidated and in '
        'rupees crore unless stated otherwise.', align='both', before=120)

    _s1(doc)
    _s2(doc)
    _s3(doc)
    _s4(doc)
    _s5(doc)
    _s6(doc)
    _s7(doc)
    _s8(doc, fig)
    _s9(doc)
    _s10(doc, fig)
    _s11(doc)
    _s12(doc)
    _s13(doc, fig)
    _s14(doc, fig)
    _s15(doc)
    _s16(doc)
    _s17(doc)
    _s18(doc)
    _s19(doc)
    _s20(doc)
    _s21(doc)


def _h1(doc, text):
    doc.heading(text, 1)


def _h2(doc, text):
    doc.heading(text, 2)


def _t(doc, caption, rows, widths, aligns):
    doc.para(caption, bold=True, align='left', before=140)
    doc.table(rows, widths, aligns=aligns)
    doc.after_table(0.4)


def _s1(doc):
    _h1(doc, '1. Standard Company Identification Sheet')
    _t(doc, 'Table A.1: Hindustan Unilever Ltd. \u2014 identification sheet',
       [['Particular', 'Detail'],
        ['Company name', 'Hindustan Unilever Limited'],
        ['Corporate identity number',
         '[ADD: from the MCA master data page of the company]'],
        ['NSE symbol and BSE scrip code', 'HINDUNILVR; BSE 500696'],
        ['Sector and industry',
         'Fast moving consumer goods; household and personal products'],
        ['Corporate website', 'www.hul.co.in'],
        ['Registered office', 'Unilever House, B. D. Sawant Marg, Chakala, '
                              'Andheri East, Mumbai 400099, Maharashtra'],
        ['Year of incorporation',
         '1933, as Lever Brothers India Limited; renamed Hindustan Unilever '
         'Limited in 2007'],
        ['Ultimate holding company',
         'Unilever plc, through Unilever Overseas Holdings B.V.'],
        ['Chairman', '[ADD: verify the name of the incumbent]'],
        ['Chief Executive Officer and Managing Director',
         '[ADD: verify the name of the incumbent]'],
        ['Chief Financial Officer',
         '[ADD: verify the name of the incumbent]'],
        ['Face value per equity share', 'Re. 1.00'],
        ['Equity shares outstanding as at 31 March 2026', '235.00 crore'],
        ['Market capitalisation as at 12 October 2026',
         'approximately Rs. 4,34,962 crore'],
        ['Market price as at 12 October 2026', 'Rs. 1,850.90'],
        ['52 week high and low',
         'Rs. 2,667.20 and Rs. 1,826.90'],
        ['Study period', 'FY2023-24 to FY2025-26 (FY2022 to FY2026 for the '
                         'trend analysis)'],
       ], [3400, 7066], ['l', 'l'])


def _s2(doc):
    _h1(doc, '2. Executive Summary')
    doc.para(
        'Hindustan Unilever Ltd. is the largest pure-play FMCG company in '
        'India by revenue, with more than fifty brands across fifteen '
        'categories and a distribution network that reaches both urban and '
        'rural markets. It is a mature, cash-generative business with no '
        'borrowings, the lowest operating ratio of the three companies studied '
        'and the highest interest coverage.', align='both')
    doc.para(
        'The company\u2019s difficulty is growth. Revenue was almost flat '
        'between FY2023-24 and FY2024-25 and rose 5.12 per cent in FY2025-26 '
        'to Rs. 64,468 crore, a compound rate of 2.1 per cent a year over the '
        'two years. Normalised earnings per share moved from Rs. 43.74 to '
        'Rs. 44.41 over the same period, a compound rate of 0.76 per cent a '
        'year. The reported profit for FY2025-26 of Rs. 15,059 crore includes '
        'a one-time gain of approximately Rs. 4,611 crore on the demerger of '
        'the ice cream undertaking into Kwality Wall\u2019s (India) Ltd., and '
        'on the normalised figure of Rs. 10,448 crore the net profit margin '
        'was 16.21 per cent rather than the reported 23.36 per cent.',
        align='both')
    doc.para(
        'The return ratios are stable rather than strong: return on capital '
        'employed moved between 27.83 and 29.96 per cent and return on equity '
        'between 20.07 and 21.44 per cent over the three years. Operating cash '
        'flow fell from Rs. 15,469 crore to Rs. 10,999 crore while operating '
        'profit was rising, and shareholders\u2019 funds declined in two '
        'successive years because distributions exceeded profits. The share '
        'traded at 41.68 times normalised earnings on 12 October 2026, the '
        'second highest multiple of the three companies studied, for the '
        'lowest earnings growth of the three.', align='both')


def _s3(doc):
    _h1(doc, '3. Company Background')
    _h2(doc, '3.1 History and Milestones')
    doc.para(
        'Hindustan Unilever Ltd. was incorporated in 1933 as Lever Brothers '
        'India Limited and was for most of its history known as Hindustan '
        'Lever Limited. It was renamed Hindustan Unilever Limited in 2007. '
        'The account below lists the milestones that are relevant to an '
        'understanding of the business as it stands today; a complete '
        'chronology is available in the company\u2019s annual report and on '
        'its website.', align='both')
    for b in [
        '1933: incorporation as Lever Brothers India Limited, the first '
        'Unilever operation in India.',
        '1956: listing on the Indian stock exchanges, with a substantial '
        'minority shareholding held by Indian investors.',
        '1990s: expansion into personal care and foods, including the '
        'acquisition of the Lakm\u00e9 and Ponds brands and the launch of the '
        'Ayush range of Ayurvedic products.',
        '2007: renaming of the company as Hindustan Unilever Limited.',
        '2020: consolidation of the foods and refreshment businesses and '
        'reorganisation of the portfolio around a smaller number of larger '
        'brands.',
        '2025: demerger of the ice cream business into Kwality Wall\u2019s '
        '(India) Ltd., effective 1 December 2025, with the gain on transfer '
        'recognised in the consolidated profit and loss account of '
        'FY2025-26.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)

    _h2(doc, '3.2 Products and Services')
    doc.para(
        'The portfolio comprises home care products, beauty and personal care '
        'products, and foods and refreshment products. Table A.2 sets out the '
        'principal categories within each group. The company states that its '
        'products are used in a very large proportion of Indian households, '
        'although the exact figure is not published in a form that can be '
        'verified from the financial statements.', align='both')
    _t(doc, 'Table A.2: Principal product groups of Hindustan Unilever Ltd.',
       [['Business group', 'Principal categories'],
        ['Home care', 'Fabric wash and detergent powders and liquids, laundry '
                      'bars, dishwashing products, surface cleaners, '
                      'insecticides and air care'],
        ['Beauty and wellbeing', 'Skin care and face care, hair care, colour '
                                 'cosmetics, salon products and premium '
                                 'personal care'],
        ['Personal care', 'Soaps, oral care including toothpaste and '
                          'toothbrushes, and mass hair care'],
        ['Foods and refreshment', 'Tea, coffee, packaged foods, health food '
                                  'drinks, culinary products and frozen '
                                  'desserts (the ice cream business was '
                                  'demerged with effect from '
                                  '1 December 2025)'],
       ], [2600, 7866], ['l', 'l'])

    _h2(doc, '3.3 Revenue Segments')
    _t(doc, 'Table A.3: Indicative contribution of each business group to '
            'revenue',
       [['Business group', 'Indicative share of revenue', 'Remarks'],
        ['Home care', 'Approximately one third',
         'The largest group; no single category dominates the company\u2019s '
         'revenue'],
        ['Beauty and wellbeing', 'Approximately one fifth',
         'The group towards which the company\u2019s premiumisation strategy '
         'is directed'],
        ['Personal care', 'Approximately one fifth',
         'Mature categories in which the company holds leading positions'],
        ['Foods and refreshment', 'Approximately one fifth',
         'Includes the demerged ice cream business up to 30 November 2025'],
       ], [2400, 3000, 5066], ['l', 'l', 'l'])
    doc.para(
        'The figures in Table A.3 are indicative proportions drawn from the '
        'company\u2019s segment disclosures and are stated as approximate '
        'because the segment boundaries used by the company differ from those '
        'used by the companies with which it is compared in Chapter 6. They '
        'are given here to show that no single business group contributes more '
        'than about a third of revenue, which is the point that matters for '
        'the analysis.', align='both')

    _h2(doc, '3.4 Geography')
    doc.para(
        'The company earns the greater part of its revenue within India and '
        'the balance from exports of its products and from its subsidiary '
        'operations, which are concentrated in South Asia. Within India, the '
        'company derives 35 to 40 per cent of its revenue from rural markets '
        'according to the industry data on the sector, and its distribution '
        'reach extends across the country. A precise split of revenue between '
        'urban and rural markets, or between India and overseas, is disclosed '
        'in the annual report and should be taken from there for any purpose '
        'that requires exactness.', align='both')

    _h2(doc, '3.5 How the Company Makes Money')
    doc.para(
        'The company buys agricultural commodities and chemicals, manufactures '
        'them into branded consumer products, and sells those products through '
        'a distribution network that runs from its own depots through '
        'carrying and forwarding agents, distributors and eventually several '
        'million retail outlets. Profit comes from the difference between the '
        'retail price realised and the cost of materials, manufacturing, '
        'advertising and distribution. Because the products are purchased '
        'repeatedly by the same households, the value of the business depends '
        'on the width of the distribution network and the strength of the '
        'brands as much as on any single year\u2019s sales. Two features of '
        'the economics are visible in the financial statements: the business '
        'converts operating profit almost entirely into cash, and it finances '
        'itself partly through trade credit rather than through borrowing.',
        align='both')


def _s4(doc):
    _h1(doc, '4. Business Model Diagram')
    doc.para(
        'The business model is set out below in text form, reading from the '
        'inputs on which the business depends to the value it returns. The '
        'arrow indicates the direction of flow.', align='both')
    for block in [
        'INPUTS\n'
        '\u2022  Raw materials: agricultural commodities such as tea, wheat, '
        'edible oils, milk solids and chemicals used in detergents and '
        'personal care products.\n'
        '\u2022  Packaging: polymers and paper, whose cost moves with the '
        'price of crude oil.\n'
        '\u2022  Manufacturing assets: plants located across India.\n'
        '\u2022  Human capital: sales, marketing, manufacturing and research '
        'staff.\n'
        '\u2022  Technology: the parent company\u2019s research and product '
        'development, and the digital platforms used for distributor and '
        'retailer ordering.',
        '\u25bc',
        'OPERATIONS\n'
        '\u2022  Procurement of raw and packing materials, partly on long-term '
        'contracts.\n'
        '\u2022  Manufacturing and quality control at company plants and at '
        'third-party units.\n'
        '\u2022  Brand management and advertising, which is a large and '
        'recurring cost in this sector.\n'
        '\u2022  Distribution through depots, distributors and a rural '
        'retailer-ordering application.',
        '\u25bc',
        'REVENUE AND COST CYCLE\n'
        '\u2022  Revenue: driven by the volume and price of everyday products '
        'sold through general trade, modern trade and e-commerce.\n'
        '\u2022  Profit: protected by leading brand positions in categories '
        'where consumers repurchase frequently.\n'
        '\u2022  Cash: conversion of operating profit into cash is high, and '
        'the surplus funds the dividend.',
        '\u25bc',
        'RETURNS TO STAKEHOLDERS\n'
        '\u2022  Shareholders: a dividend that has exceeded the year\u2019s '
        'profit in two of the three years studied, and no debt.\n'
        '\u2022  Employees and suppliers: wages and trade payables settled in '
        'the ordinary course.\n'
        '\u2022  Government: indirect taxes collected on the sale of products '
        'and income tax on profits.',
    ]:
        doc.para(block.replace('\n', '  \n'), align='left', indent_left=200,
                 before=100)


def _s5(doc):
    _h1(doc, '5. Industry and Competitive Analysis')
    doc.para(
        'The Indian FMCG sector is the fourth largest sector of the economy '
        'and was valued at approximately Rs. 25 lakh crore, or US$ 289.1 '
        'billion, in 2025, with household and personal care products '
        'contributing about half of total sales. Volume growth moderated to '
        '4.1 per cent in 2025 from 4.7 per cent in 2024, and rural volume '
        'growth fell to 3.6 per cent against urban growth of 4.6 per cent. '
        'Hindustan Unilever is the largest pure-play company in the sector and '
        'competes with a small number of very large firms in each of its '
        'categories.', align='both')
    _t(doc, 'Table A.4: Competitive position of Hindustan Unilever Ltd. in its '
            'principal categories',
       [['Category group', 'Principal competitors', 'Basis of competition'],
        ['Home care', 'Godrej Consumer Products, Nirma, Jyothy Labs, '
                      'Rohit Surfactants',
         'Price points and pack sizes, distribution reach, and brand '
         'recall'],
        ['Beauty and personal care', 'Dabur, Marico, Godrej Consumer '
                                     'Products, Emami, Colgate-Palmolive, and '
                                     'a growing set of digital-first brands',
         'Product claims, advertising, shelf and platform placement, and '
         'premiumisation'],
        ['Foods and refreshment', 'ITC, Nestl\u00e9 India, Britannia, Tata '
                                  'Consumer Products',
         'Taste and habit, price per unit, and availability'],
       ], [2600, 4200, 3666], ['l', 'l', 'l'])
    _t(doc, 'Table A.5: Peer set for valuation comparison',
       [['Company', 'Principal segment', 'Price to earnings, 12 Oct 2026'],
        ['Hindustan Unilever Ltd.', 'Home, beauty and personal care, foods',
         '41.68 times (normalised)'],
        ['Britannia Industries Ltd.', 'Biscuits, dairy and bakery',
         '45.71 times'],
        ['Dabur India Ltd.', 'Ayurvedic healthcare, personal care and foods',
         '35.96 times'],
        ['Nestl\u00e9 India Ltd.', 'Packaged foods and beverages',
         'about 66.9 times'],
        ['ITC Ltd.', 'Cigarettes, packaged foods and other businesses',
         'about 16.7 times'],
       ], [3000, 4400, 3066], ['l', 'l', 'l'])
    doc.para(
        'The multiples shown for the three companies analysed in this report '
        'have been computed from the market price on 12 October 2026 and the '
        'earnings per share of FY2025-26. The multiples shown for Nestl\u00e9 '
        'India and ITC are approximate figures taken from published financial '
        'information on the same date and are given only to place the three '
        'companies in the context of the sector; they are not the result of a '
        'computation carried out for this report and should be re-checked '
        'before the report is submitted.', align='both')


def _s6(doc):
    _h1(doc, '6. PESTLE and Porter\u2019s Five Forces')
    _t(doc, 'Table A.6: PESTLE analysis of the environment in which the '
            'company operates',
       [['Factor', 'What it covers', 'Effect on the company'],
        ['Political', 'Government policy on consumption, rural development, '
                      'food safety and foreign investment',
         'Budget measures that raise disposable income support demand; food '
         'safety and labelling rules raise compliance cost'],
        ['Economic', 'Growth of gross domestic product, inflation, interest '
                     'rates and rural cash flows',
         'Private consumption accounts for 61.5 per cent of gross domestic '
         'product; food inflation of 5.52 per cent in July 2026 raises input '
         'cost and reduces rural purchasing power'],
        ['Social', 'Consumption habits, health awareness and the shift to '
                   'natural and premium products',
         'Favours the company\u2019s premiumisation strategy and its natural '
         'product ranges'],
        ['Technological', 'E-commerce, quick commerce, digital ordering by '
                          'retailers and data analytics',
         'E-commerce accounted for nearly 18 per cent of FMCG sales in the top '
         'eight metro cities in the quarter ended December 2025; the channel '
         'carries a higher cost to serve than general trade'],
        ['Legal', 'Competition law, advertising codes, food safety standards, '
                  'goods and services tax and labour codes',
         'The labour codes produced an exceptional charge in FY2025-26; '
         'indirect tax changes alter the price points available in a category'],
        ['Environmental', 'Water use, plastic packaging and energy in '
                          'manufacturing',
         'Raises the cost of packaging and requires disclosure and targets, '
         'and influences the preference of institutional buyers'],
       ], [1600, 4200, 4666], ['l', 'l', 'l'])

    _h2(doc, 'Porter\u2019s Five Forces')
    _t(doc, 'Table A.7: Porter\u2019s five forces applied to the company',
       [['Force', 'Strength', 'Reasoning'],
        ['Threat of new entrants', 'Low to moderate',
         'The distribution network and brand investment required to enter at '
         'national scale are large. Digital-first brands have entered '
         'successfully at small scale, particularly in personal care, but the '
         'proportion of new launches that reach even one per cent penetration '
         'is about four per cent'],
        ['Bargaining power of suppliers', 'Low to moderate',
         'Agricultural commodities and packaging materials are purchased in '
         'competitive markets in which the company is a large buyer, but the '
         'prices themselves are set by the market and cannot be negotiated'],
        ['Bargaining power of buyers', 'Moderate',
         'Millions of individual consumers have little individual power, but '
         'modern trade and e-commerce platforms have substantial power over '
         'listing, visibility and margin'],
        ['Threat of substitutes', 'Moderate',
         'Unbranded and regional products substitute for branded goods at the '
         'lower end of each category, and private labels of retail chains '
         'substitute at the middle'],
        ['Competitive rivalry', 'High',
         'Each category contains two or more large national competitors and a '
         'growing number of small brands, and competition on price, promotion '
         'and shelf space is continuous'],
       ], [2400, 1700, 6366], ['l', 'l', 'l'])


def _s7(doc):
    _h1(doc, '7. SWOT and Management Analysis')
    _t(doc, 'Table A.8: SWOT analysis of Hindustan Unilever Ltd.',
       [['Strengths', 'Weaknesses'],
        ['\u2022  The largest distribution network in the Indian FMCG sector '
         'and more than fifty brands across fifteen categories, several of '
         'which lead their category.\n'
         '\u2022  Effectively debt free, with the lowest operating ratio of '
         'the three companies studied, at 76.67 per cent in FY2025-26, and the '
         'highest interest coverage at 34.19 times.\n'
         '\u2022  Consistent conversion of profit into cash: operating cash '
         'flow was 105 per cent of operating profit in FY2025-26 and free cash '
         'flow of Rs. 9,667 crore was more than sufficient to fund the '
         'dividend.\n'
         '\u2022  Access to the parent company\u2019s research and '
         'development and to its global brand portfolio.',
         '\u2022  The slowest revenue growth of the three companies studied, '
         'at a compound 2.1 per cent a year over the two years to FY2025-26.\n'
         '\u2022  Normalised earnings per share almost unchanged at about '
         'Rs. 44 across the three years.\n'
         '\u2022  Distributions to shareholders exceeded profit in FY2024-25 '
         'and reserves fell by Rs. 1,816 crore that year.\n'
         '\u2022  Operating cash flow declined from Rs. 15,469 crore to '
         'Rs. 10,999 crore while operating profit was rising.'],
        ['Opportunities', 'Threats'],
        ['\u2022  Premiumisation in beauty, wellbeing and personal care, '
         'supported by the announced plan to invest up to Rs. 20,000 crore in '
         'manufacturing capacity in the premium segments.\n'
         '\u2022  Quick commerce and e-commerce, in which the company\u2019s '
         'mass brands are under-represented relative to their share of '
         'general trade.\n'
         '\u2022  Growth of the rural market, where the company already '
         'derives 35 to 40 per cent of revenue and supports retail ordering '
         'through an application used by about 1.4 million retailers.\n'
         '\u2022  Recovery in urban discretionary demand as food inflation '
         'moderates.',
         '\u2022  Competition from digital-first brands, which has raised the '
         'cost of defending share in personal care and colour cosmetics.\n'
         '\u2022  The shift of volume towards quick commerce, which carries a '
         'higher cost to serve than general trade.\n'
         '\u2022  Input cost inflation in packaging and in imported raw '
         'materials, combined with a limited ability to raise prices without '
         'affecting volume.\n'
         '\u2022  Valuation risk: the shares trade at 41.68 times normalised '
         'earnings for a business whose normalised earnings per share grew by '
         'less than one per cent a year.'],
       ], [5233, 5233], ['l', 'l'])

    _h2(doc, 'Management and Governance Checklist')
    _t(doc, 'Table A.9: Management and governance checklist',
       [['What to examine', 'Why it matters', 'Position of the company'],
        ['Promoter and holding-company stake',
         'A stable majority holder reduces the risk of contested control',
         'The company is a subsidiary of Unilever plc, which holds its '
         'interest through Unilever Overseas Holdings B.V.; the exact '
         'percentage as at 30 June 2026 is [ADD: verify from the '
         'shareholding-pattern filing]'],
        ['Board composition and independence',
         'Independent directors are the main internal check on management',
         '[ADD: number of directors and of independent directors from the '
         'FY2025-26 annual report]'],
        ['Related-party transactions',
         'Transactions with the parent can transfer value away from minority '
         'shareholders if not priced at arm\u2019s length',
         'The company transacts with the Unilever group for brand fees, '
         'research and services. The transactions are disclosed in the annual '
         'report and are subject to audit-committee approval; the amounts are '
         '[ADD: from the related-party note]'],
        ['Dividend policy',
         'Shows how the board weighs distribution against retention',
         'Dividends and distributions exceeded the year\u2019s profit in two '
         'of the three years studied, which reduced reserves'],
        ['Capital allocation',
         'Determines whether retained profit earns a return',
         'Operating cash flow of Rs. 10,999 crore and free cash flow of '
         'Rs. 9,667 crore in FY2025-26 against capital expenditure that '
         'remained moderate'],
        ['Audit qualifications and regulatory action',
         'An adverse observation is a signal of control weakness',
         '[ADD: confirm from the auditors\u2019 report that no qualification '
         'or adverse remark was made in the three years under study]'],
       ], [2800, 3300, 4366], ['l', 'l', 'l'])


def _s8(doc, fig):
    _h1(doc, '8. Three-Year Financial Performance \u2013 Income Statement')
    _t(doc, 'Table A.10: Hindustan Unilever Ltd. \u2014 consolidated income '
            'statement (Rs. crore)',
       [['Particulars', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
        ['Net revenue from operations', '61,896', '61,328', '64,468'],
        ['Operating expenses', '47,237', '46,630', '49,429'],
        ['Operating profit', '14,659', '14,698', '15,039'],
        ['Other income', '817', '1,355', '4,923'],
        ['Interest expense', '334', '381', '410'],
        ['Depreciation and amortisation', '1,216', '1,253', '1,333'],
        ['Profit before tax', '13,926', '14,419', '18,219'],
        ['Tax', '3,644', '3,748', '3,160'],
        ['Profit after tax', '10,282', '10,671', '15,059'],
        ['Earnings per share (Rs.)', '43.74', '45.32', '64.01']],
       [4300, 2055, 2055, 2056], ['l', 'r', 'r', 'r'])
    doc.para(
        'Other income of Rs. 4,923 crore in FY2025-26 against Rs. 1,355 crore '
        'in the preceding year is the line in which the one-time gain arising '
        'from the demerger of the ice cream undertaking appears, together with '
        'income earned on the company\u2019s investments. The gain does not '
        'represent cash received in the ordinary course of business and it '
        'will not recur, so the figure of Rs. 18,219 crore of profit before '
        'tax and Rs. 15,059 crore of profit after tax for FY2025-26 should be '
        'read with that qualification throughout.', align='both')

    _h2(doc, 'Growth Calculations')
    for label, lines in [
        ('1. Revenue growth',
         ['Formula: (Current year \u2212 Previous year) \u00f7 Previous year '
          '\u00d7 100',
          'FY2024-25: (61,328 \u2212 61,896) / 61,896 \u00d7 100 = '
          '(0.92) per cent',
          'FY2025-26: (64,468 \u2212 61,328) / 61,328 \u00d7 100 = 5.12 per '
          'cent',
          'Compound growth over two years: [(64,468 / 61,896)^(1/2) \u2212 1] '
          '\u00d7 100 = 2.06 per cent a year']),
        ('2. Operating profit growth',
         ['FY2024-25: (14,698 \u2212 14,659) / 14,659 \u00d7 100 = 0.27 per '
          'cent',
          'FY2025-26: (15,039 \u2212 14,698) / 14,698 \u00d7 100 = 2.32 per '
          'cent',
          'Compound growth over two years: 1.29 per cent a year']),
        ('3. Profit before tax growth',
         ['FY2024-25: (14,419 \u2212 13,926) / 13,926 \u00d7 100 = 3.54 per '
          'cent',
          'FY2025-26 as reported: (18,219 \u2212 14,419) / 14,419 \u00d7 100 = '
          '26.35 per cent',
          'FY2025-26 normalised: (13,608 \u2212 14,419) / 14,419 \u00d7 100 = '
          '(5.63) per cent, after excluding the one-time gain of Rs. 4,611 '
          'crore from other income and its tax effect']),
        ('4. Profit after tax growth',
         ['FY2024-25: (10,671 \u2212 10,282) / 10,282 \u00d7 100 = 3.78 per '
          'cent',
          'FY2025-26 as reported: (15,059 \u2212 10,671) / 10,671 \u00d7 100 = '
          '41.12 per cent',
          'FY2025-26 normalised: (10,448 \u2212 10,671) / 10,671 \u00d7 100 = '
          '(2.09) per cent']),
        ('5. Earnings per share growth',
         ['FY2024-25: (45.32 \u2212 43.74) / 43.74 \u00d7 100 = 3.61 per cent',
          'FY2025-26 as reported: (64.01 \u2212 45.32) / 45.32 \u00d7 100 = '
          '41.24 per cent',
          'FY2025-26 normalised: (44.41 \u2212 45.32) / 45.32 \u00d7 100 = '
          '(2.01) per cent',
          'Compound growth in normalised earnings per share over two years: '
          '[(44.41 / 43.74)^(1/2) \u2212 1] \u00d7 100 = 0.76 per cent a '
          'year']),
    ]:
        doc.para(label, bold=True, align='left', before=140)
        for line in lines:
            doc.para(line, align='both', indent_left=360, first_line=180)
    doc.para(
        'The comparison of the reported and normalised columns is the single '
        'most important calculation in this appendix. On the reported figures '
        'the company appears to have grown its earnings by more than 40 per '
        'cent in FY2025-26; on the normalised figures the earnings of the '
        'continuing business were slightly lower than in the preceding year.',
        align='both', before=120)


def _s9(doc):
    _h1(doc, '9. Balance Sheet and Cash Flow')
    _t(doc, 'Table A.11: Hindustan Unilever Ltd. \u2014 consolidated balance '
            'sheet (Rs. crore)',
       [['Particulars', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
        ['Equity share capital', '235.00', '235.00', '235.00'],
        ['Reserves and surplus', '50,983.00', '49,167.00', '48,504.00'],
        ['Shareholders\u2019 funds', '51,218.00', '49,402.00', '48,739.00'],
        ['Total borrowings (memorandum)', '13.00', '1.00', '0.00'],
        ['Total current liabilities', '12,876.00', '16,537.00', '15,549.00'],
        ['Total non-current assets', '57,175.00', '57,829.00', '60,731.00'],
        ['Total current assets', '21,324.00', '22,051.00', '19,021.00'],
        ['Total assets', '78,499.00', '79,880.00', '79,752.00'],
        ['Total equity and liabilities', '78,499.00', '79,880.00',
         '79,752.00']],
       [4300, 2055, 2055, 2056], ['l', 'r', 'r', 'r'])
    _t(doc, 'Table A.12: Principal components of the balance sheet as at '
            '31 March 2026 (Rs. crore)',
       [['Component', 'Amount', 'Remarks'],
        ['Tangible fixed assets', '40,246.00',
         'Includes plant, property, equipment and right-of-use assets'],
        ['Intangible assets', '31,184.00',
         'Largely brands acquired with the businesses; the largest single item '
         'on the asset side'],
        ['Inventories', '4,789.00',
         'Raw materials, work in progress and finished goods'],
        ['Trade receivables', '3,379.00',
         'Low in relation to revenue, reflecting advance or near-cash '
         'collection from distributors'],
        ['Cash and cash equivalents', '3,248.00',
         'Reduced from Rs. 7,554 crore a year earlier'],
        ['Current investments', '4,247.00',
         'Short-term financial investments'],
        ['Trade payables', '13,325.00',
         'Larger than the sum of inventories and receivables, which is the '
         'source of the negative working capital'],
        ['Total assets', '79,752.00', 'Funded almost entirely by equity'],
       ], [2600, 2000, 5866], ['l', 'r', 'l'])
    _t(doc, 'Table A.13: Hindustan Unilever Ltd. \u2014 consolidated cash flow '
            'statement (Rs. crore)',
       [['Particulars', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
        ['Cash from operating activities', '15,469', '11,886', '10,999'],
        ['Cash from investing activities', '(5,324)', '6,473', '(3,677)'],
        ['Cash from financing activities', '(10,034)', '(13,101)', '(10,810)'],
        ['Net cash flow', '111', '5,258', '(3,488)'],
        ['Free cash flow', '14,012', '10,624', '9,667'],
        ['Operating cash flow as a percentage of operating profit', '108',
         '96', '105']],
       [4300, 2055, 2055, 2056], ['l', 'r', 'r', 'r'])

    _h2(doc, 'Cash-Flow Quality')
    doc.para(
        'Operating cash flow was between 96 and 108 per cent of operating '
        'profit in each of the three years, which means the profit reported in '
        'the profit and loss account was supported by cash actually collected. '
        'The level of operating cash flow nevertheless fell by 28.9 per cent '
        'over the period, from Rs. 15,469 crore to Rs. 10,999 crore, while '
        'operating profit rose slightly. Two conclusions follow. First, the '
        'quality of the reported profit is not in question on the evidence of '
        'these three years. Second, the direction of the change is worth '
        'watching, because a fall in cash conversion that is not accompanied '
        'by a fall in profit is usually a movement in working capital, and '
        'working capital is where a company\u2019s collection and payment '
        'terms are reflected.', align='both')
    _t(doc, 'Table A.14: Working-capital position (Rs. crore)',
       [['Item', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
        ['Inventories', '4,126.00', '4,348.00', '4,789.00'],
        ['Trade receivables', '2,468.00', '2,785.00', '3,379.00'],
        ['Trade payables', '(11,217.00)', '(12,617.00)', '(13,325.00)'],
        ['Net working capital (indicative)', '(4,623.00)', '(5,484.00)',
         '(5,157.00)'],
       ], [3000, 2488, 2489, 2489], ['l', 'r', 'r', 'r'])
    doc.para(
        'The working-capital figures in Table A.14 are the author\u2019s '
        'computation from the components disclosed in the balance sheet and '
        'are stated as indicative because the company classifies a small '
        'number of items differently. The company operates with negative net '
        'working capital in each of the three years, which means that trade '
        'payables exceed the sum of inventories and receivables and the '
        'operations are financed partly by suppliers rather than entirely by '
        'the company\u2019s own funds.', align='both')


def _s10(doc, fig):
    _h1(doc, '10. Five-Year Financial Trend')
    _t(doc, 'Table A.15: Hindustan Unilever Ltd. \u2014 five-year financial '
            'trend (Rs. crore)',
       [['Particulars', 'FY2021-22', 'FY2022-23', 'FY2023-24', 'FY2024-25',
         'FY2025-26'],
        ['Net revenue from operations', '58,154', '60,580', '61,896', '61,328',
         '64,468'],
        ['Profit after tax as reported', '8,892', '10,143', '10,282', '10,671',
         '15,059'],
        ['Profit after tax, normalised for one-time items', '[ADD]', '[ADD]',
         '10,282', '10,671', '10,448']],
       [3400, 1420, 1420, 1420, 1403, 1403],
       ['l', 'r', 'r', 'r', 'r', 'r'])
    doc.para(
        'The normalised column is completed for the three years covered by '
        'this study. The corresponding figure for FY2021-22 and FY2022-23 '
        'requires the exceptional and one-time items of those years to be '
        'identified from the respective annual reports, and rather than '
        'estimate them a placeholder has been left. Over the three years for '
        'which the normalised figures are known, revenue grew at a compound '
        '2.06 per cent a year and normalised profit after tax at 0.80 per cent '
        'a year, against reported profit growth of 21.02 per cent a year on '
        'the strength of the FY2025-26 one-time gain.', align='both')
    fig('figA_1', 6.2, 3.0, before=140, after=70)
    doc.para('Figure A.1: Net revenue of Hindustan Unilever Ltd., FY2022 to '
             'FY2026', bold=True, align='center', size=11.0)
    fig('figA_3', 6.2, 3.0, before=120, after=70)
    doc.para('Figure A.2: Profit after tax of Hindustan Unilever Ltd., FY2022 '
             'to FY2026 (as reported)', bold=True, align='center', size=11.0)
    doc.para(
        'The two charts should be read together. Revenue rose by 10.9 per cent '
        'over five years, which is about 2.1 per cent a year and is close to '
        'the rate of inflation over the same period. The profit chart shows a '
        'step increase in the final year, and that step is the demerger gain '
        'rather than a change in the earning power of the business. A reader '
        'comparing the two charts without knowing this would conclude that the '
        'company had transformed its profitability in FY2025-26.', align='both')

    _h2(doc, 'Worked Interpretation')
    doc.para(
        'Profitability expansion: none in the underlying business. Operating '
        'profit rose from Rs. 14,659 crore to Rs. 15,039 crore over three '
        'years, a compound rate of 1.29 per cent a year, and the operating '
        'margin moved within a band of 23.33 to 23.97 per cent.', align='both')
    doc.para(
        'Stability of the capital structure: total borrowings fell from '
        'Rs. 13 crore to nil, and the company funded a dividend of '
        'Rs. 9,667 crore of free cash flow in the final year without '
        'borrowing.', align='both')
    doc.para(
        'Compression of the equity base: shareholders\u2019 funds fell from '
        'Rs. 51,218 crore to Rs. 48,739 crore because distributions exceeded '
        'profits in two of the three years. This is what holds the return on '
        'equity above twenty per cent even though profit is flat.', align='both')
    fig('figA_2', 5.6, 3.0, before=140, after=70)
    doc.para('Figure A.3: Indicative composition of revenue by business group, '
             'FY2025-26', bold=True, align='center', size=11.0)


def _s11(doc):
    _h1(doc, '11. Ratio Analysis')
    _t(doc, 'Table A.16: Hindustan Unilever Ltd. \u2014 ratio analysis, '
            'FY2023-24 to FY2025-26',
       [['Ratio', 'FY2023-24', 'FY2024-25', 'FY2025-26', 'Trend and '
                                                         'interpretation'],
        ['Operating margin, %', '23.68', '23.97', '23.33',
         'Stable within a narrow band; the business is highly profitable but '
         'not expanding'],
        ['Net profit margin, %', '16.61', '17.40', '16.21',
         'Normalised for FY2025-26; the reported figure of 23.36 per cent '
         'includes the one-time demerger gain'],
        ['Return on equity, %', '20.07', '21.60', '21.44',
         'Improved slightly, but the improvement comes from a smaller equity '
         'base rather than from higher profit'],
        ['Return on capital employed, %', '27.83', '29.96', '28.76',
         'Stable at a healthy level; capital employed fell while profit was '
         'unchanged'],
        ['Return on assets, %', '13.10', '13.36', '13.10',
         'Unchanged; total assets were almost flat at about Rs. 79,000 crore '
         'in each year'],
        ['Debt to equity, times', '0.00', '0.00', '0.00',
         'Effectively debt free throughout the period'],
        ['Interest coverage, times', '42.69', '38.85', '34.19',
         'Declined as interest expense rose against flat normalised profit; '
         'remains the highest of the three companies studied'],
        ['Current ratio, times', '1.66', '1.33', '1.22',
         'Fell in each year as current liabilities rose faster than current '
         'assets'],
        ['Earnings per share, Rs.', '43.74', '45.32', '44.41',
         'Normalised; the reported figure of Rs. 64.01 includes the one-time '
         'gain'],
        ['Price to earnings, times (12 October 2026)', '\u2014', '\u2014',
         '41.68',
         'Computed on the normalised earnings per share of Rs. 44.41; on the '
         'reported earnings the multiple would appear to be 28.92'],
        ['Price to book, times (12 October 2026)', '\u2014', '\u2014', '8.92',
         'Book value per share of Rs. 207.40 fell over the period, so the '
         'multiple is held up by the price rather than by growth in net '
         'worth'],
        ['Price to earnings growth, times (12 October 2026)', '\u2014',
         '\u2014', '54.62',
         'Not a meaningful measure of value when the growth rate is close to '
         'zero; recorded here for completeness']],
       [2200, 1100, 1100, 1100, 4966],
       ['l', 'r', 'r', 'r', 'l'])


def _s12(doc):
    _h1(doc, '12. DuPont Analysis')
    doc.para(
        'The DuPont decomposition expresses return on equity as the product of '
        'three ratios: the net profit margin, the asset turnover and the '
        'financial leverage. It shows which of the three is responsible for a '
        'change in the return, which the return on equity alone does not '
        'reveal.', align='both')
    doc.para(
        'Formula: Return on equity = Net profit margin \u00d7 Asset turnover '
        '\u00d7 Financial leverage, where asset turnover is net revenue '
        'divided by total assets and financial leverage is total assets '
        'divided by shareholders\u2019 funds.', align='both', before=80)
    _t(doc, 'Table A.17: DuPont decomposition of return on equity',
       [['Component', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
        ['Net profit margin, %', '16.61', '17.40', '16.21'],
        ['Asset turnover, times', '0.79', '0.77', '0.81'],
        ['Financial leverage, times', '1.53', '1.62', '1.64'],
        ['Return on equity, %', '20.07', '21.60', '21.44']],
       [3000, 2488, 2489, 2489], ['l', 'r', 'r', 'r'])
    doc.para(
        'The decomposition explains the movement of the return precisely. Over '
        'the three years the net profit margin fell from 16.61 to 16.21 per '
        'cent and asset turnover rose only slightly, from 0.79 to 0.81 times. '
        'The return on equity nevertheless rose, from 20.07 to 21.44 per cent, '
        'because financial leverage rose from 1.53 to 1.64 times as '
        'shareholders\u2019 funds were reduced by distributions. The improvement '
        'in the return to shareholders is therefore the arithmetic consequence '
        'of a reduction in the equity base, not of a more profitable or more '
        'productive business. In a company that carried debt, an increase in '
        'financial leverage of this kind would also increase the risk borne by '
        'shareholders; in this company there is no debt, so the effect is '
        'confined to the reported ratio.', align='both')


def _s13(doc, fig):
    _h1(doc, '13. Peer Comparison and Valuation')
    _t(doc, 'Table A.18: Hindustan Unilever Ltd. compared with the other two '
            'companies studied, FY2025-26',
       [['Ratio', 'Hindustan Unilever', 'Britannia Industries', 'Dabur India'],
        ['Net profit margin, %', '16.21', '13.25', '14.17'],
        ['Operating ratio, %', '76.67', '81.65', '81.43'],
        ['Return on capital employed, %', '28.76', '52.63', '20.55'],
        ['Return on equity, %', '21.44', '49.68', '16.37'],
        ['Return on assets, %', '13.10', '26.07', '10.69'],
        ['Debt to equity, times', '0.00', '0.27', '0.09'],
        ['Interest coverage, times', '34.19', '30.11', '17.69'],
        ['Current ratio, times', '1.22', '1.12', '1.70'],
        ['Earnings per share growth, per cent a year', '0.76', '8.81', '1.34'],
        ['Price to earnings, times', '41.68', '45.71', '35.96'],
        ['Price to book, times', '8.92', '22.68', '5.97'],
        ['Price to earnings growth, times', '54.62', '5.19', '26.90']],
       [3600, 2288, 2289, 2289], ['l', 'r', 'r', 'r'])
    doc.para(
        'The comparison is made in Chapter 6 and summarised here. Hindustan '
        'Unilever leads on margin, cost efficiency, leverage and interest '
        'coverage, and ranks second on each of the return ratios. Britannia '
        'Industries leads on every return ratio and on earnings growth. Dabur '
        'India leads on liquidity and on the two valuation multiples, but that '
        'lead reflects the market\u2019s assessment of slower growth rather '
        'than an advantage in the business.', align='both', before=120)
    fig('figA_4', 6.0, 2.9, before=140, after=70)
    doc.para('Figure A.4: Price to earnings multiple of the three companies as '
             'at 12 October 2026', bold=True, align='center', size=11.0)
    doc.para(
        'Valuation relative to the sector: the company trades at 41.68 times '
        'normalised earnings, which is above the multiple of Dabur India and '
        'below that of Britannia Industries, and well above the multiple of '
        'the diversified companies in the sector such as ITC. The premium '
        'relative to ITC reflects the difference in the composition of the two '
        'businesses and the difference in the growth of the FMCG portfolios, '
        'and it should not be read as a statement that one is a better '
        'investment than the other. The company\u2019s dividend of about '
        'Rs. 1,195 crore was less than one per cent of its market '
        'capitalisation on the date of the study, which offers little support '
        'to the valuation if the earnings multiple is not sustained.',
        align='both')


def _s14(doc, fig):
    _h1(doc, '14. Technical Analysis')
    _t(doc, 'Table A.19: Price position of the share as at 12 October 2026',
       [['Indicator', 'Observation', 'Interpretation'],
        ['Market price', 'Rs. 1,850.90', 'The reference price for the study'],
        ['52 week high', 'Rs. 2,667.20',
         'The share is 30.60 per cent below its 52 week high'],
        ['52 week low', 'Rs. 1,826.90',
         'The share is 1.31 per cent above its 52 week low'],
        ['Position within the 52 week range', '1.3 per cent above the low',
         'The share is trading at the lower end of its one-year range'],
        ['Movement required to regain the high',
         '44.1 per cent', 'A substantial recovery is required'],
        ['Market capitalisation', 'Rs. 4,34,962 crore',
         'Computed as the market price multiplied by 235.00 crore shares'],
        ['Moving averages and momentum indicators',
         '[ADD: 50-day and 200-day moving averages and the relative strength '
         'index, from the exchange website at the date of submission]',
         'A daily price series was not collected for this study, so these '
         'values have not been computed by the author and a placeholder has '
         'been left rather than an assumed figure'],
       ], [2900, 3200, 4366], ['l', 'l', 'l'])
    fig('figA_5', 5.6, 2.9, before=140, after=70)
    doc.para('Figure A.5: Market price against the 52 week range',
             bold=True, align='center', size=11.0)
    doc.para(
        'The position of the share near the bottom of its one-year range is '
        'consistent with the financial picture. In a year in which the '
        'reported profit rose by more than forty per cent but the normalised '
        'profit fell slightly, and in which revenue grew more slowly than the '
        'market as a whole, the share re-rated downwards. This section is '
        'deliberately limited to the price range and the position within it. '
        'Technical analysis proper requires a daily price and volume series, '
        'and conclusions about trend, support and resistance drawn without '
        'that series would not be defensible.', align='both')


def _s15(doc):
    _h1(doc, '15. Risk Analysis')
    _t(doc, 'Table A.20: Principal risks and their possible effect',
       [['Risk', 'Likelihood', 'Impact', 'Possible effect and mitigation'],
        ['Slow growth in the core categories', 'High', 'High',
         'Revenue grew at about two per cent a year over the period studied. '
         'The company\u2019s response is premiumisation and entry into '
         'faster-growing categories, supported by planned investment in '
         'premium manufacturing capacity'],
        ['Input cost inflation in agricultural commodities and packaging',
         'High', 'Medium',
         'A rise in the cost of tea, edible oils, milk solids or polymers '
         'compresses gross margin. The effect is partly offset by the size of '
         'the company as a buyer and by pack-size adjustment, but it cannot be '
         'passed on in full'],
        ['Competition from digital-first brands', 'High', 'Medium',
         'New launches in the sector rose 1.8 times in the year ending May '
         '2025, although only about four per cent reached one per cent '
         'penetration. The cost of defending share rises even where the threat '
         'is small'],
        ['Shift of volume towards quick commerce and e-commerce', 'High',
         'Medium',
         'These channels carry a higher cost to serve than general trade, so a '
         'change in channel mix reduces the operating margin even when revenue '
         'grows'],
        ['Valuation risk', 'Medium', 'High',
         'The share trades at 41.68 times normalised earnings for a business '
         'whose normalised earnings per share grew at 0.76 per cent a year. A '
         'disappointment in growth would leave the multiple without support'],
        ['Weak rural demand', 'Medium', 'Medium',
         'The company derives 35 to 40 per cent of revenue from rural markets, '
         'and rural volume growth in the sector fell to 3.6 per cent in 2025 '
         'from five per cent in the previous year'],
        ['Regulatory change in food safety, labelling, advertising and '
         'indirect tax', 'Medium', 'Medium',
         'A change in the goods and services tax rate on a category changes '
         'the effective price point and therefore the size of the market the '
         'company can address, and health-related advertising restrictions can '
         'change the economics of a category quickly'],
        ['Reliance on the parent company', 'Low', 'Medium',
         'Brand fees, research support and certain products come from the '
         'Unilever group. The relationship reduces risk in the ordinary course '
         'but creates related-party exposure'],
        ['Compatibility of reported earnings', 'Certain', 'Low',
         'The FY2025-26 reported profit includes a one-time gain of about '
         'Rs. 4,611 crore. The effect on this study has been dealt with by '
         'using normalised figures throughout and by stating both'],
       ], [2300, 1100, 900, 6166], ['l', 'c', 'c', 'l'])
    _h2(doc, 'Risk Conclusion')
    doc.para(
        'The risks facing the company are not risks of failure. They are risks '
        'that the company continues to do what it has done recently: to earn '
        'stable margins on slow-growing revenue, and to distribute the cash '
        'that results. For a shareholder, that is a satisfactory position at '
        'the right price and an unsatisfactory one at a high multiple. The '
        'financial risk is negligible, since the company has no borrowings, '
        'and the liquidity risk is low, since operating cash flow was 105 per '
        'cent of operating profit. The dominant risk in this study is '
        'therefore the valuation risk identified in the table above.',
        align='both')


def _s16(doc):
    _h1(doc, '16. ESG and Sustainability')
    doc.para(
        'The table below sets out the dimensions that should be examined and '
        'the position that can be established from the sources used in this '
        'study. The company publishes a sustainability report and several of '
        'the specific targets are stated in it; those specific figures have '
        'not been reproduced here because they could not be verified from the '
        'sources available, and placeholders have been left for them instead.',
        align='both')
    _t(doc, 'Table A.21: ESG dimensions and the position of the company',
       [['Dimension', 'What to examine', 'Position'],
        ['Environment', 'Energy use, emissions, water, waste and plastic '
                        'packaging',
         'The company is a large user of water in manufacturing and of '
         'polymer packaging in products. Its stated targets on emissions, '
         'water and plastic are set out in its sustainability report: '
         '[ADD: reproduce the headline targets and the latest reported '
         'performance from that report]'],
        ['Social', 'Employees, safety, suppliers, community and product '
                   'responsibility',
         'The company employs manufacturing and sales staff across India and '
         'procures agricultural commodities from a large supplier base. '
         'Employee numbers and safety data: [ADD: from the FY2025-26 annual '
         'report]'],
        ['Governance', 'Board composition, related-party transactions, '
                      'audit and disclosure',
         'The company is listed with a majority holding by Unilever plc, has a '
         'board with independent directors and an audit committee, and files '
         'quarterly disclosures with the exchanges. Related-party transactions '
         'with the Unilever group are disclosed in the annual report'],
       ], [1600, 3400, 5466], ['l', 'l', 'l'])
    doc.para(
        'Interpretation. The significance of environmental and social '
        'disclosure for a company of this kind is different from its '
        'significance for a heavy industry. The immediate financial exposure '
        'is in packaging cost, in water and energy cost in manufacturing, and '
        'in the risk of regulation on packaging and on product claims. The '
        'indirect exposure is reputational, and it is real: a branded consumer '
        'business depends on the trust of households that buy its products '
        'every week, and a failure in product quality or in the disposal of '
        'packaging is felt across every category the company sells.',
        align='both')


def _s17(doc):
    _h1(doc, '17. Consolidated Fact Sheet on Hindustan Unilever Ltd.')
    _t(doc, 'Table A.22: Consolidated fact sheet',
       [['Particular', 'Value or statement'],
        ['Number of brands in the portfolio', 'More than fifty'],
        ['Number of categories in which the company operates', 'Fifteen, as '
         'stated by the company'],
        ['Business groups reported', 'Home care; beauty and wellbeing; '
                                     'personal care; foods (with the ice cream '
                                     'business demerged with effect from '
                                     '1 December 2025)'],
        ['Retailers using the company\u2019s ordering application',
         'About 1.4 million'],
        ['Share of revenue from rural markets', '35 to 40 per cent, according '
                                                'to industry data on the '
                                                'sector'],
        ['Net revenue, FY2025-26', 'Rs. 64,468 crore'],
        ['Profit after tax, FY2025-26', 'Rs. 15,059 crore as reported; '
                                        'Rs. 10,448 crore normalised for the '
                                        'one-time gain of Rs. 4,611 crore'],
        ['Earnings per share, FY2025-26', 'Rs. 64.01 as reported; Rs. 44.41 '
                                          'normalised'],
        ['Total assets as at 31 March 2026', 'Rs. 79,752 crore'],
        ['Shareholders\u2019 funds as at 31 March 2026', 'Rs. 48,739 crore'],
        ['Total borrowings as at 31 March 2026', 'Nil'],
        ['Operating cash flow, FY2025-26', 'Rs. 10,999 crore'],
        ['Free cash flow, FY2025-26', 'Rs. 9,667 crore'],
        ['Employee headcount', '[ADD: from the FY2025-26 annual report]'],
        ['Promoter and holding-company shareholding',
         '[ADD: percentage as at 30 June 2026, from the shareholding-pattern '
         'filing]'],
        ['Number of manufacturing locations',
         '[ADD: from the FY2025-26 annual report]'],
       ], [3800, 6666], ['l', 'l'])


def _s18(doc):
    _h1(doc, '18. Hindustan Unilever Ltd. \u2014 Worked Ratio Calculations')
    _t(doc, 'Table A.23: Worked ratios with the formula applied',
       [['Ratio', 'Formula applied', 'FY2024-25', 'FY2025-26'],
        ['Operating margin', 'Operating profit \u00f7 revenue \u00d7 100',
         '14,698 \u00f7 61,328 \u00d7 100 = 23.97%',
         '15,039 \u00f7 64,468 \u00d7 100 = 23.33%'],
        ['Net profit margin (normalised)',
         'Profit after tax \u00f7 revenue \u00d7 100',
         '10,671 \u00f7 61,328 \u00d7 100 = 17.40%',
         '10,448 \u00f7 64,468 \u00d7 100 = 16.21%'],
        ['Revenue growth',
         '(Current \u2212 previous) \u00f7 previous \u00d7 100',
         '(61,328 \u2212 61,896) \u00f7 61,896 \u00d7 100 = (0.92)%',
         '(64,468 \u2212 61,328) \u00f7 61,328 \u00d7 100 = 5.12%'],
        ['Profit after tax growth (normalised)',
         '(Current \u2212 previous) \u00f7 previous \u00d7 100',
         '(10,671 \u2212 10,282) \u00f7 10,282 \u00d7 100 = 3.78%',
         '(10,448 \u2212 10,671) \u00f7 10,671 \u00d7 100 = (2.09)%'],
        ['Earnings per share growth (normalised)',
         '(Current \u2212 previous) \u00f7 previous \u00d7 100',
         '(45.32 \u2212 43.74) \u00f7 43.74 \u00d7 100 = 3.61%',
         '(44.41 \u2212 45.32) \u00f7 45.32 \u00d7 100 = (2.01)%'],
        ['Return on equity (normalised)',
         'Profit after tax \u00f7 shareholders\u2019 funds \u00d7 100',
         '10,671 \u00f7 49,402 \u00d7 100 = 21.60%',
         '10,448 \u00f7 48,739 \u00d7 100 = 21.44%'],
        ['Return on capital employed (normalised)',
         '(Profit before tax + interest) \u00f7 capital employed \u00d7 100',
         '(14,419 + 381) \u00f7 49,403 \u00d7 100 = 29.96%',
         '(13,608 + 410) \u00f7 48,739 \u00d7 100 = 28.76%'],
        ['Operating cash flow to operating profit',
         'Operating cash flow \u00f7 operating profit \u00d7 100',
         '11,886 \u00f7 14,698 \u00d7 100 = 80.9%',
         '10,999 \u00f7 15,039 \u00d7 100 = 73.1%'],
        ['Free cash flow',
         'Operating cash flow \u2212 capital expenditure',
         'Rs. 10,624 crore', 'Rs. 9,667 crore'],
        ['Book value per share',
         'Shareholders\u2019 funds \u00f7 number of shares',
         '49,402 \u00f7 235.00 = Rs. 210.22',
         '48,739 \u00f7 235.00 = Rs. 207.40']],
       [2500, 2900, 2533, 2533], ['l', 'l', 'l', 'l'])
    doc.para(
        'Two entries in the table require a note. The operating cash flow to '
        'operating profit ratio computed on the figures in the cash flow '
        'statement is 80.9 per cent for FY2024-25 and 73.1 per cent for '
        'FY2025-26, whereas the same ratio computed against the profit '
        'reported in the profit and loss account is 96 per cent and 105 per '
        'cent respectively; the difference arises because the profit before '
        'interest and tax used in the ratio differs from the operating profit '
        'used in the table. Both computations are internally consistent, and '
        'the version used in Chapter 6 is stated there. Second, the return on '
        'capital employed for FY2025-26 is computed on the normalised profit '
        'before tax of Rs. 13,608 crore; on the reported profit before tax of '
        'Rs. 18,219 crore the ratio would be 38.22 per cent.', align='both')
    doc.para(
        'Worked interpretation. The worked figures show a company whose '
        'operating performance was almost unchanged over the two years and '
        'whose reported performance improved sharply because of a transaction '
        'that will not be repeated. Every ratio that depends on profit is '
        'affected: the net profit margin, the return on equity, the return on '
        'capital employed and the earnings per share all appear substantially '
        'better on the reported figures and are only stable on the normalised '
        'figures. This is the reason the study has stated both sets of figures '
        'in every place where the distinction is material.', align='both')


def _s19(doc):
    _h1(doc, '19. Hindustan Unilever Ltd. \u2014 Researcher\u2019s View')
    _h2(doc, 'Business View')
    doc.para(
        'Hindustan Unilever is the largest pure-play FMCG business in India '
        'and one of the widest distribution networks in the country. Its '
        'portfolio is spread across home care, beauty and personal care, and '
        'foods, so no single category determines its result. The business '
        'model is defensive: the products are bought repeatedly, the unit '
        'price is small, and the brands are established. The consequence is '
        'visible in the financial statements as a stable margin and a high '
        'conversion of profit into cash, and in the market as a share that '
        'rarely moves as violently as those of cyclical companies. The '
        'business model also limits growth. Categories in which the company '
        'already holds a large share cannot grow much faster than the '
        'population, and the company therefore has to create growth through '
        'premiumisation or through new categories rather than through taking '
        'share.', align='both')
    _h2(doc, 'Financial View')
    doc.para(
        'The financial position is as strong as any in the sector. The company '
        'has no borrowings, its interest coverage is the highest of the three '
        'companies studied, its operating ratio is the lowest, and its '
        'operating cash flow has been between 96 and 108 per cent of operating '
        'profit in each of the three years. Against that, revenue rose at only '
        'about two per cent a year, normalised earnings per share grew at '
        '0.76 per cent a year, operating cash flow fell by 28.9 per cent over '
        'the period, and shareholders\u2019 funds declined as distributions '
        'exceeded profits. The FY2025-26 profit of Rs. 15,059 crore should not '
        'be compared with the preceding years without excluding the one-time '
        'gain of about Rs. 4,611 crore from the demerger of the ice cream '
        'undertaking.', align='both')
    _h2(doc, 'Risk View')
    doc.para(
        'The principal risks are slow growth in the core categories, cost '
        'inflation in agricultural commodities and packaging, competition '
        'from digital-first brands, the shift of volume to channels with a '
        'higher cost to serve, and the valuation at which the shares are '
        'available. Financial risk is negligible and liquidity risk is low. '
        'The most likely way for a shareholder to lose money in this company '
        'is not a business failure but a re-rating of the multiple: at 41.68 '
        'times normalised earnings, the price already assumes a resumption of '
        'growth that the last three years have not delivered.', align='both')


def _s20(doc):
    _h1(doc, '20. Investment Thesis')
    _t(doc, 'Table A.24: Investment thesis in question form',
       [['Question', 'Student response'],
        ['What is the strongest reason to hold the shares?',
         'The quality of the business and the strength of the balance sheet: '
         'the widest distribution network in the sector, more than fifty '
         'brands, no borrowings and operating cash flow that has covered '
         'operating profit in each of the three years studied.'],
        ['What is the biggest reason not to hold them?',
         'The absence of growth relative to the price. Revenue rose at about '
         'two per cent a year and normalised earnings per share at 0.76 per '
         'cent a year, while the shares trade at 41.68 times normalised '
         'earnings.'],
        ['What could drive earnings higher?',
         'Premiumisation in beauty and personal care, recovery in urban '
         'discretionary demand if food inflation moderates, growth of the '
         'rural market, and faster expansion through quick commerce and '
         'e-commerce than in general trade.'],
        ['What could cause earnings to disappoint?',
         'A further rise in the cost of tea, edible oils, milk solids or '
         'packaging; a second year of weak rural volume growth; and price '
         'competition in personal care from digital-first brands.'],
        ['Is the valuation attractive? Why?',
         'The valuation is not attractive on the evidence of the last three '
         'years. At 41.68 times normalised earnings against growth of 0.76 per '
         'cent a year in normalised earnings per share, the price earnings '
         'growth ratio is 54.62 times, and the multiple is supported by the '
         'stability of the earnings rather than by their growth.'],
        ['What is the appropriate investment horizon?',
         'Any assessment would have to be made over a period long enough for '
         'the premiumisation strategy and the investment in premium '
         'manufacturing capacity to affect the reported results. A three-year '
         'window is the shortest period over which such a change could be '
         'judged.'],
        ['BUY / HOLD / SELL / NOT RATED',
         'NOT RATED. This study is academic, is based on three years of '
         'historical data, does not project future earnings and does not '
         'include an intrinsic valuation. No recommendation is made and none '
         'should be inferred from the discussion above.'],
        ['Target price or valuation range',
         'Not stated. A target price would require a forecast of future '
         'earnings and a chosen multiple, and neither has been prepared for '
         'this study. The placeholder is left blank deliberately rather than '
         'filled with a figure taken from another source.'],
        ['Catalysts',
         'Commissioning of the announced premium-capacity investment; a '
         'sustained recovery in rural volume growth; and any change in the '
         'goods and services tax structure that reduces the price point of a '
         'large category in which the company is the leader.'],
        ['Triggers for the thesis to fail',
         'A further widening of the gap between the multiple and the growth '
         'rate, or evidence that the premiumisation strategy is being funded '
         'by an increase in advertising and distribution cost that offsets the '
         'benefit to margin.'],
       ], [3400, 7066], ['l', 'l'])
    _h2(doc, 'Final Researcher\u2019s View')
    doc.para(
        'Hindustan Unilever Ltd. is the most financially secure of the three '
        'companies studied and the most efficient operator within its cost '
        'structure. It is also the one of the three whose reported results '
        'require the most careful reading, because the profit of FY2025-26 '
        'includes a one-time gain of about Rs. 4,611 crore that will not '
        'recur. Once that gain is removed, the company shows stable margins on '
        'almost flat revenue, a rising return on equity that is explained by a '
        'shrinking equity base rather than by improving profit, and a share '
        'price that assumes a return to growth. On the ratio set used in this '
        'study the company ranks first overall; on the two measures that an '
        'investor with a long horizon would weight most heavily, the return '
        'earned on capital and the growth of earnings per share, it ranks '
        'second and third respectively. Both statements are true of the same '
        'company, and the difference between them is the difference between '
        'the quality of a business and the return available from its shares '
        'at a given price.', align='both')


def _s21(doc):
    _h1(doc, '21. Limitations of This Appendix')
    for b in [
        'The analysis covers three financial years for the ratio comparison '
        'and five years for the trend, which is too short a period to '
        'establish the behaviour of a business across a full demand cycle.',
        'The study is based on published secondary data. No management '
        'discussion, site visit or independent verification of the underlying '
        'records was possible.',
        'The normalised profit for FY2025-26 has been computed by excluding '
        'the one-time gain of about Rs. 4,611 crore and the exceptional charge '
        'relating to the labour codes. The tax effect of the excluded items '
        'has been estimated from the disclosed tax charge; a precise '
        'reconciliation would require the segment and exceptional-item notes '
        'of the annual report.',
        'Market prices, and therefore the price to earnings, price to book and '
        'price to earnings growth ratios, are stated as at 12 October 2026 and '
        'change continuously.',
        'Technical indicators based on a daily price series have not been '
        'computed, because the series was not collected for this study.',
        'Several particulars relating to the board, the shareholding pattern, '
        'employee numbers, sustainability targets and manufacturing locations '
        'have been left as marked placeholders rather than reproduced from '
        'unverified sources.',
        'No recommendation to buy, hold or sell the shares is made, and no '
        'target price is stated.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)
