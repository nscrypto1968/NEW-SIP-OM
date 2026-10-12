# -*- coding: utf-8 -*-
"""Chapter 3 (sector overview) and Chapter 4 (research methodology)."""

from docgen import Doc, BODY_SIZE


def chapter_3(doc, fig):
    doc.new_page()
    doc.chapter('CHAPTER 3 :- FUNDAMENTAL ANALYSIS - SECTOR OVERVIEW')
    doc.para(
        'Fundamental analysis begins with the industry in which a company '
        'operates, because the industry determines the range of outcomes that '
        'are available to any individual firm within it. This chapter sets out '
        'the importance of the Indian fast-moving consumer goods sector, its '
        'industry-wide advantages and disadvantages, the challenges it faces, '
        'and an overview of its ten largest listed companies. The company-wise '
        'financial analysis is presented in Chapter 5 under the economic, '
        'industry and company framework, and the comparative ratio analysis in '
        'Chapter 6.', align='both')

    doc.heading('3.1 IMPORTANCE OF THE FMCG SECTOR', 2,
                '   3.1 Importance of the FMCG Sector')
    para = lambda t, **kw: doc.para(t, align='both', **kw)

    doc.para('A.  Contribution to the economy', bold=True, align='left',
             before=160)
    para(
        'The FMCG sector is the fourth largest sector of the Indian economy. It '
        'provides employment to around three million people, which is '
        'approximately five per cent of total factory employment in the '
        'country. The Indian FMCG market generated revenue of approximately '
        'Rs. 25 lakh crore, equivalent to US$ 289.1 billion, in 2025 and is '
        'expected to grow at a compound annual rate of 17.3 per cent through '
        'the period 2025 to 2030, reaching nearly US$ 642.87 billion by 2030. '
        'Household and personal care products alone contribute about half of '
        'total FMCG sales.', before=120)
    para(
        'The sector\u2019s importance does not rest only on its size. Because '
        'its products are consumed repeatedly and at short intervals, demand '
        'is comparatively insensitive to the business cycle. This '
        'defensiveness is the reason the sector is treated differently from '
        'cyclical industries in portfolio construction, and it is also the '
        'reason the sector is analysed here alongside the internship, since a '
        'dealer on a broking desk regularly handles client interest in exactly '
        'these securities.')
    fig('fig3_1', 6.0, 2.9, before=140, after=80)
    doc.caption('Figure 3.1: Indian FMCG market size, 2025 and 2030 (projected)')
    para(
        'The projection above, which is the published industry estimate, '
        'implies that the market roughly doubles over five years. The figure '
        'should be read as an expectation of nominal growth, part of which '
        'reflects price increases rather than additional volume, and it is '
        'therefore a statement about the size of the opportunity rather than '
        'of the return available to any particular company.')

    doc.para('B.  Rural and urban consumption', bold=True, align='left',
             before=160)
    para(
        'The urban segment contributes about 62 per cent of total FMCG '
        'revenue, while rural India accounts for more than 38 per cent. The '
        'two markets behave differently. Rural demand is closely linked to the '
        'monsoon, to the level of minimum support prices and to the '
        'government\u2019s transfer programmes, and it responds strongly to '
        'the pack sizes and price points that are made available. Urban demand '
        'is linked to wage growth, to employment in the services sector and to '
        'premiumisation. The balance between the two is therefore one of the '
        'most important variables in any forecast of the sector.')
    fig('fig3_2', 5.6, 2.6, before=140, after=80)
    doc.caption('Figure 3.2: Urban and rural share of Indian FMCG sales')
    para(
        'The split matters for interpretation of company performance. Two '
        'companies of similar size can report very different growth in the '
        'same year purely because of the difference in their rural and urban '
        'mix. Dabur derives 45 to 50 per cent of its revenue from rural '
        'markets and reaches over 1,31,000 villages and 1.42 million outlets, '
        'while Hindustan Unilever generates 35 to 40 per cent of its revenue '
        'from rural areas and supports its rural distribution with a retailer '
        'ordering application that has about 1.4 million retailers on board. '
        'A year in which rural demand weakens will therefore affect Dabur more '
        'than Hindustan Unilever, irrespective of the quality of either '
        'company\u2019s execution.')

    doc.para('C.  Growth drivers of the sector', bold=True, align='left',
             before=160)
    for b in [
        'Rising disposable income and a large young population: India\u2019s '
        'middle-class population is larger than the total population of the '
        'United States and the median age of the population is about 27 years, '
        'which sustains both the volume of consumption and the willingness to '
        'try premium products.',
        'Policy support for consumption: the Union Budget 2025-26 was directed '
        'partly at consumer spending, and the increase in disposable income '
        'and the focus on rural development create a favourable environment '
        'for staples and for packaged foods.',
        'Shift from unbranded to branded products: as incomes rise, households '
        'substitute branded and packaged goods for loose and unbranded '
        'substitutes, which expands the organised market even when total '
        'consumption grows slowly.',
        'Expansion of distribution into smaller towns and villages: direct '
        'reach, rural preferred dealer networks and retailer ordering '
        'applications have extended the reach of the larger companies well '
        'beyond the principal cities.',
        'Growth of e-commerce and quick commerce: e-commerce accounted for '
        'nearly 18 per cent of FMCG sales across the top eight metro cities in '
        'the quarter from October to December 2025, and quick commerce now '
        'accounts for 70 to 75 per cent of total e-grocery orders, against '
        'about 35 per cent in 2022.',
        'Premiumisation: within categories such as personal care, foods and '
        'beverages, consumers have moved towards higher-priced variants, which '
        'allows companies to improve margin even where volume growth is '
        'modest.',
        'Investment by large companies: several of the largest firms have '
        'announced significant capital expenditure programmes, including '
        'Hindustan Unilever\u2019s plan to invest up to Rs. 20,000 crore in '
        'manufacturing capacity in premium segments and ITC\u2019s plan of '
        'about Rs. 20,000 crore over the next five to six years.',
    ]:
        doc.para('- ' + b, align='both', indent_left=360, first_line=216)

    doc.heading('3.2 INDUSTRY-WIDE ADVANTAGES & DISADVANTAGES', 2,
                '   3.2 Industry-Wide Advantages & Disadvantages')
    doc.para('Advantages', bold=True, align='left', before=160)
    for b in [
        'Defensive demand: the products are consumed frequently and are '
        'purchased again within a short interval, so revenue is less exposed '
        'to a downturn in economic activity than in discretionary industries.',
        'Low unit price and wide penetration: because the unit price is small, '
        'a household can continue to buy the product through periods of '
        'pressure on income, which stabilises volume.',
        'Brand loyalty and pricing power: established brands in categories '
        'such as detergents, biscuits and health supplements command a price '
        'premium and retain consumers across cycles, which protects margin.',
        'Negative working capital in practice: the larger companies collect '
        'from distributors sooner than they pay their own suppliers, so '
        'operations are partly financed by trade credit. All three companies '
        'studied have a negative cash conversion cycle.',
        'Established distribution as a barrier to entry: a distribution '
        'network that reaches millions of retail outlets takes years and '
        'substantial capital to build, and it is the principal reason a new '
        'entrant cannot easily displace an incumbent.',
        'Cash-generative with low capital intensity: the sector converts a '
        'large proportion of its operating profit into operating cash flow and '
        'requires comparatively modest capital expenditure to maintain '
        'existing capacity.',
    ]:
        doc.para('- ' + b, align='both', indent_left=360, first_line=216)
    doc.para('Disadvantages', bold=True, align='left', before=160)
    for b in [
        'Exposure to input cost inflation: the principal raw materials are '
        'agricultural commodities and crude oil derivatives, whose prices '
        'cannot be controlled by the company, and packaging costs move with '
        'the price of polymers.',
        'Limited ability to pass on cost increases quickly: because the '
        'products are everyday necessities, a price increase invites consumer '
        'resistance and regulatory attention, so companies often absorb cost '
        'pressure in margin.',
        'Intense competition: the sector contains large domestic groups, '
        'Indian subsidiaries of global companies and a growing set of '
        'digital-first brands, and competition on price and on shelf space is '
        'continuous.',
        'Dependence on advertising: FMCG was the largest advertising sector in '
        'India in 2024, contributing around 34 per cent of total advertising '
        'expenditure with spends of about Rs. 31,428 crore. Advertising is a '
        'recurring cost that must be maintained to hold market share.',
        'Slow volume growth in mature categories: several of the largest '
        'categories have reached high penetration and grow at approximately '
        'the rate of population growth, so a company must find new categories '
        'or new geographies to grow faster than the market.',
        'Regulatory and quality exposure: the sector is subject to food safety '
        'standards, labelling and advertising regulation, and legal '
        'metrology, and a single quality or labelling failure can damage a '
        'brand across its entire category.',
    ]:
        doc.para('- ' + b, align='both', indent_left=360, first_line=216)

    doc.heading('3.3 SECTOR CHALLENGES', 2, '   3.3 Sector Challenges')
    para(
        'The challenges listed below are the ones that are most visible in the '
        'financial statements of the companies analysed in this report, rather '
        'than a general list of industry concerns.', before=120)
    for b in [
        'Moderating volume growth with a widening rural-urban gap: India\u2019s '
        'FMCG sector recorded overall volume growth of 4.1 per cent in 2025, '
        'down from 4.7 per cent in 2024. Rural volume growth fell to 3.6 per '
        'cent from 5 per cent, while urban growth edged up to 4.6 per cent '
        'from 4.5 per cent. The rural slowdown is the single most important '
        'challenge facing companies with a rural-weighted portfolio.',
        'Input cost and packaging cost pressure: prices of edible oils, milk '
        'solids, wheat, sugar and crude-oil-linked packaging materials move '
        'independently of consumer demand, and a simultaneous rise compresses '
        'gross margin in the same year in which demand is weak.',
        'Competition from digital-first brands: new product launches in the '
        'sector rose 1.8 times in the year ending May 2025, although only '
        'about 4 per cent of those launches reached a market penetration of '
        'one per cent. The failure rate lowers the expected return on '
        'innovation spending without reducing the amount that must be spent.',
        'Shift of volume to channels with different economics: quick commerce '
        'and e-commerce are growing far faster than general trade, but the '
        'commission, delivery and platform cost in these channels is higher, '
        'so a shift in channel mix can reduce margin even while revenue grows.',
        'Regulatory intervention on pricing and on health: restrictions on the '
        'advertising of products high in fat, salt and sugar, and on '
        'packaging and labelling, can change the economics of a category '
        'quickly. The introduction of the goods and services tax reform on '
        'packaged goods has also altered the effective price points available '
        'to manufacturers in some categories.',
        'Foreign exchange and commodity exposure on imports: companies that '
        'import palm oil, wheat or packaging material carry a translation and '
        'purchasing exposure which cannot be fully hedged, and depreciation of '
        'the rupee raises landed cost directly.',
        'Talent and distribution cost inflation: the cost of frontline sales '
        'and distribution manpower has risen faster than the price of the '
        'product in several categories, which increases the fixed component of '
        'the cost structure.',
    ]:
        doc.para('- ' + b, align='both', indent_left=360, first_line=216)

    doc.heading('3.4 TOP 10 INDIAN FMCG COMPANIES OVERVIEW', 2,
                '   3.4 Top 10 Indian FMCG Companies Overview')
    para(
        'Table 3.1 gives an overview of the ten largest listed companies in '
        'the Indian FMCG sector and the position each occupies within it. The '
        'companies are listed in the order of their principal area of '
        'operation rather than in order of size, because a single ranking by '
        'market capitalisation would place companies of very different '
        'business models next to each other without explaining the '
        'difference.')
    doc.table_title('Table 3.1: Leading listed companies in the Indian FMCG sector')
    doc.table([
        ['Sr. No.', 'Company name', 'Principal segment',
         'Core position in the sector'],
        ['1', 'Hindustan Unilever Ltd.', 'Home care, beauty and wellbeing, '
                                         'personal care and foods',
         'The largest pure-play FMCG company in India, with more than fifty '
         'brands across fifteen categories and one of the widest distribution '
         'networks in the country.'],
        ['2', 'ITC Ltd.', 'Cigarettes, packaged foods, personal care, hotels '
                          'and paper',
         'A diversified conglomerate in which the non-cigarette FMCG business '
         'is the fastest-growing segment. The scale of the tobacco business '
         'funds the expansion of the consumer portfolio.'],
        ['3', 'Nestl\u00e9 India Ltd.', 'Packaged foods and beverages, '
                                        'prepared dishes and confectionery',
         'The leading packaged foods company, particularly strong in '
         'instant noodles, coffee, chocolate and infant nutrition, with a '
         'premium portfolio and high dependency on a few large brands.'],
        ['4', 'Britannia Industries Ltd.', 'Biscuits, breads, cakes and dairy',
         'The market leader in biscuits, with a distribution reach that '
         'extends into rural markets through preferred dealer networks, and a '
         'growing presence in dairy and adjacent snacking categories.'],
        ['5', 'Dabur India Ltd.', 'Ayurvedic and natural healthcare, personal '
                                  'care and foods',
         'The largest Ayurvedic and natural healthcare company in India, with '
         'products reaching eight out of ten Indian households and a strong '
         'rural and semi-urban presence.'],
        ['6', 'Marico Ltd.', 'Edible oils, hair oils and packaged foods',
         'A leader in coconut oil and hair oils with a focused portfolio of '
         'few large brands, and a growing presence in premium packaged '
         'snacking through acquisitions.'],
        ['7', 'Godrej Consumer Products Ltd.', 'Home care, personal care and '
                                               'insecticides',
         'A leading player in household insecticides and in hair colour, with '
         'a substantial international business in Indonesia, Africa and Latin '
         'America.'],
        ['8', 'Colgate-Palmolive (India) Ltd.', 'Oral care',
         'The market leader in oral care, with a concentrated portfolio and '
         'very high return on capital employed, and comparatively limited '
         'diversification outside toothpaste and toothbrushes.'],
        ['9', 'Tata Consumer Products Ltd.', 'Tea, coffee, salt, spices and '
                                             'packaged foods',
         'A leading player in tea and salt with a rapidly expanding foods and '
         'beverages portfolio, and the owner of several large beverage and '
         'food brands acquired in recent years.'],
        ['10', 'Emami Ltd.', 'Personal care and healthcare',
         'A focused personal care company with strong brands in cooling oils, '
         'men\u2019s grooming and balms, and a significant rural and '
         'winter-season sales profile.'],
    ], [700, 2100, 2600, 5066], aligns=['c', 'l', 'l', 'l'])
    doc.after_table(0.4)
    para(
        'The composition of this list is itself informative for the analysis '
        'that follows. Five of the ten companies derive the greater part of '
        'their revenue from foods and beverages, four are weighted towards '
        'personal and home care, and one, ITC, is a diversified conglomerate '
        'whose FMCG business sits beside a much larger tobacco business. The '
        'three companies selected for detailed analysis in this report were '
        'chosen to represent three different positions on that spectrum: a '
        'diversified home and personal care company, a foods company and a '
        'healthcare-led personal care company. The reasons for the selection '
        'are set out in Chapter 4.')


def chapter_4(doc):
    doc.new_page()
    doc.chapter('CHAPTER 4 :- RESEARCH METHODOLOGY')

    doc.heading('4.1 RESEARCH DESIGN & OBJECTIVES', 2,
                '   4.1 Research Design & Objectives')
    doc.para(
        'The present study is based on a descriptive and analytical research '
        'design. The study analyses and compares the financial performance of '
        'selected companies in the Indian FMCG sector over the period from '
        'FY2023-24 to FY2025-26. It is descriptive because the objective is to '
        'document and explain the position of each company rather than to test '
        'a causal hypothesis, and analytical because the financial statements '
        'are decomposed into ratios and compared between companies and between '
        'years.', align='both')
    doc.para(
        'The operational component of the report adopts a work-based learning '
        'design, in which the author was placed within the function studied '
        'and the observations were generated by performing the work rather '
        'than by interviewing those who perform it. A descriptive design is '
        'appropriate for that component as well, because the dealing process '
        'is prescribed by regulation and exchange rules rather than '
        'determined by the preferences of participants.', align='both')
    doc.para('The objectives of the research are the following.', align='both')
    for b in [
        'To analyse the profitability of Hindustan Unilever Ltd., Britannia '
        'Industries Ltd. and Dabur India Ltd. over FY2023-24 to FY2025-26.',
        'To study the liquidity and solvency position of the three selected '
        'companies using current ratio, debt to equity and interest coverage.',
        'To analyse the efficiency and the return earned on the capital '
        'employed by each company using operating ratio, return on capital '
        'employed, return on equity, return on assets and return on '
        'investment.',
        'To evaluate the market valuation of the selected companies using the '
        'price to earnings, price to book and price to earnings growth '
        'ratios, and to compare each company\u2019s multiple with the median '
        'multiple of its listed peer set.',
        'To compare the financial performance of the three companies over the '
        'three financial years and to identify the company showing relatively '
        'better financial performance on the selected ratios.',
        'To examine the effect of a one-time item on the comparability of the '
        'reported figures of one of the selected companies, and to state '
        'clearly the basis on which the comparison has been made.',
    ]:
        doc.para('- ' + b, align='both', indent_left=360, first_line=216)

    doc.heading('4.2 SCOPE & SOURCES OF DATA', 2,
                '   4.2 Scope & Sources of Data')
    doc.para(
        'The study is based mainly on secondary data. Financial information '
        'has been collected from audited annual financial statements, the '
        'annual reports of the selected companies, share-related information '
        'published by the exchanges, and published financial information '
        'consolidated from the companies\u2019 own filings. Where a ratio has '
        'been computed by the author rather than reported by the company, the '
        'formula applied is stated along with the result, so that the '
        'derivation can be checked.', align='both')
    doc.para('The major sources of secondary data used in the study are the '
             'following.', align='both')
    for b in [
        'Annual reports of Hindustan Unilever Ltd., Britannia Industries Ltd. '
        'and Dabur India Ltd. for FY2023-24, FY2024-25 and FY2025-26.',
        'Audited consolidated financial statements of the three companies, and '
        'the quarterly results filed with the exchanges.',
        'Corporate announcements and shareholding pattern disclosures filed '
        'with BSE Ltd. and the National Stock Exchange of India Ltd.',
        'Securities and Exchange Board of India publications and circulars, '
        'and exchange bye-laws and regulations, for the operational component '
        'of the report.',
        'Reserve Bank of India publications and the Economic Survey for the '
        'macroeconomic data used in the economic analysis.',
        'India Brand Equity Foundation industry publications for sector size, '
        'growth and investment data.',
        'Published financial information and ratio data collated from the '
        'companies\u2019 own statements, used for cross-checking computed '
        'ratios.',
        'Company websites, for business descriptions, product portfolios, '
        'history and management information.',
    ]:
        doc.para('- ' + b, align='both', indent_left=360, first_line=216)
    doc.para(
        'Primary data consists of the author\u2019s own structured observation '
        'of the dealing desk during the internship, including the sequence of '
        'the working day, the screens and functions used, the categories of '
        'client instruction received, the nature of the risk alerts generated '
        'and the reconciliation procedure followed at the close of the '
        'session. No client record, internal limit or financial figure of the '
        'firm has been reproduced. Every trading example in this report is '
        'constructed by the author and labelled as illustrative.', align='both')

    doc.heading('4.3 SAMPLE SELECTION & PERIOD OF STUDY', 2,
                '   4.3 Sample Selection & Period of Study')
    doc.para(
        'The study uses purposive sampling for the selection of the companies. '
        'Three companies were selected because they represent three distinct '
        'positions within the Indian FMCG sector and because each publishes '
        'sufficient financial information for a comparative analysis over '
        'three financial years. The selection criteria applied were the '
        'following.', align='both')
    for b in [
        'The company must be listed on a recognised Indian stock exchange and '
        'must be part of the FMCG sector on the basis of its principal '
        'revenue.',
        'The company must have a financial year ending on 31 March, so that '
        'the figures of all three companies relate to the same twelve-month '
        'period and are directly comparable.',
        'The company must have audited consolidated financial statements '
        'available for each of the three years under study.',
        'The three companies taken together must represent more than one '
        'segment of the FMCG sector, so that the comparison is not confined '
        'to a single product category.',
    ]:
        doc.para('- ' + b, align='both', indent_left=360, first_line=216)
    doc.para('Name of the companies selected:', bold=True, align='left',
             before=120)
    for b in [
        'Hindustan Unilever Ltd. \u2014 home care, beauty and wellbeing, '
        'personal care and foods.',
        'Britannia Industries Ltd. \u2014 biscuits, breads, cakes and dairy '
        'products.',
        'Dabur India Ltd. \u2014 Ayurvedic and natural healthcare, personal '
        'care and foods.',
    ]:
        doc.para('- ' + b, align='both', indent_left=360, first_line=216)
    doc.para(
        'A fourth company, Nestl\u00e9 India Ltd., was considered and '
        'excluded. The company changed its financial year end from December to '
        'March, so that the twelve months reported as FY2023-24 in fact cover '
        'a fifteen-month period. Including it would have required an '
        'adjustment to the reported figures of one company in one year, which '
        'would have reduced the comparability of the rest of the analysis. The '
        'exclusion is noted here so that the reason for the composition of the '
        'sample is clear.', align='both')
    doc.para(
        'The period of study covers three financial years: FY2023-24, '
        'FY2024-25 and FY2025-26. For simplicity in the ratio tables, these '
        'years are represented as 2024, 2025 and 2026. Market price data used '
        'in the valuation ratios is stated as on 12 October 2026, which is the '
        'date on which it was collected, and the fact that prices change '
        'continuously is acknowledged as a limitation of the study.',
        align='both')
    doc.para(
        'The tools used for analysis are financial ratio analysis and '
        'comparative and trend analysis. The ratios have been grouped into '
        'profitability ratios (net profit margin, operating ratio), return '
        'ratios (return on capital employed, return on equity, return on '
        'assets, return on investment), solvency and leverage ratios (debt to '
        'equity, interest coverage), liquidity ratios (current ratio) and '
        'market valuation ratios (price to earnings, price to book, price to '
        'earnings growth). The interpretation of each ratio is presented '
        'immediately after the table, and the ratio trend charts are used to '
        'show the movement of each ratio across the three years.', align='both')
    doc.para('The limitations of the study are the following.', bold=True,
             align='left', before=160)
    for b in [
        'The study is based mainly on secondary data, so the accuracy of the '
        'analysis depends on the accuracy of the published financial '
        'statements and disclosures relied upon.',
        'The analysis is limited to three selected companies and to three '
        'financial years, which is too short a period to establish a '
        'long-term trend in a sector whose performance is influenced by '
        'monsoon, commodity and policy cycles.',
        'Financial ratios alone cannot provide a complete picture of a '
        'company. The analysis does not include a discounted cash flow '
        'valuation, a study of management quality or an assessment of brand '
        'strength, all of which influence long-term value.',
        'The reported profit of one of the selected companies for FY2025-26 '
        'includes a substantial one-time item. Reported and normalised figures '
        'therefore differ, and the basis used in each table has been stated '
        'explicitly.',
        'Market prices change continuously, whereas the valuation ratios in '
        'this report are computed on market data as at a single date.',
        'The macroeconomic and sector data used in the economic and industry '
        'analysis are stated as at the date on which they were collected, and '
        'several of them are revised subsequently by the publishing agency.',
        'The internship component of the study covers a single firm and a '
        'single dealing desk, so its observations describe a process rather '
        'than the practice of the industry as a whole.',
        'Confidentiality obligations prevented the use of the firm\u2019s '
        'actual order flow, so every quantitative example in the operational '
        'part of the report is illustrative rather than observed.',
    ]:
        doc.para('- ' + b, align='both', indent_left=360, first_line=216)
    doc.para(
        'Four safeguards were adopted with regard to data. First, no '
        'client-identifying information appears anywhere in this report. '
        'Second, no internal financial figure of the firm is disclosed, and '
        'every monetary example in the operational chapters is constructed by '
        'the author and labelled illustrative. Third, no fact about the firm '
        'has been invented; where a particular was not available from the '
        'firm\u2019s own documents, a marked placeholder has been left rather '
        'than an assumed value. Fourth, every figure taken from a published '
        'source is capable of being traced to that source, and the sources are '
        'listed in the references and bibliography.', align='both')
