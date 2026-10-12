# -*- coding: utf-8 -*-
"""Chapter 5 - the economic, industry and company framework."""

from docgen import Doc, BODY_SIZE


def chapter_5(doc, fig):
    doc.new_page()
    doc.para('CHAPTER 5 :- EIC FRAMEWORK (ECONOMIC, INDUSTRY & COMPANY '
             'ANALYSIS)', bold=True, align='left')
    doc.mark('CHAPTER 5 :- EIC FRAMEWORK (ECONOMIC, INDUSTRY & COMPANY '
             'ANALYSIS)', 1)
    _economic(doc, fig)
    _industry(doc, fig)
    _hul(doc, fig)
    _britannia(doc, fig)
    _dabur(doc, fig)


# ---------------------------------------------------------------------------
# 5.1  Economic analysis
# ---------------------------------------------------------------------------
def _economic(doc, fig):
    doc.heading('5.1 ECONOMIC ANALYSIS (MACROECONOMIC FACTORS & CURRENT '
                'INDIAN ECONOMY)', 2,
                '   5.1 Economic Analysis (Macroeconomic Factors & Current '
                'Indian Economy)')
    para = lambda t, **kw: doc.para(t, align='both', **kw)
    doc.para('A.  What economic analysis is', bold=True, align='left',
             before=140)
    para(
        'Economic analysis evaluates how money, resources, goods and services '
        'move through a market or a country. It uses data such as gross '
        'domestic product, inflation, employment and interest rates to measure '
        'the financial health of an economy, to guide government policy, and '
        'to help investors decide how much risk they are willing to carry. In '
        'fundamental analysis the purpose of the exercise is narrower: to '
        'establish whether the general economic environment is likely to '
        'support or restrain the earnings of the companies being studied.')
    para(
        'The indicators most relevant to a consumer-goods company are '
        'different from those relevant to a capital-goods company. A producer '
        'of everyday consumption goods depends principally on household real '
        'income, on the level of food and fuel inflation, on rural cash flows '
        'and on the cost of the raw materials and packaging it buys. This '
        'section therefore examines the state of the Indian economy in 2026 '
        'with those channels in mind, and Table 5.1 sets out the principal '
        'indicators used.')
    doc.para('Table 5.1: Principal macroeconomic indicators used in the '
             'analysis', bold=True, align='left', before=120)
    doc.table([
        ['Indicator', 'What it measures', 'Why it matters for an FMCG company'],
        ['Real gross domestic product', 'The total value of final goods and '
                                        'services produced in the economy, '
                                        'adjusted for price change',
         'Sets the growth of aggregate demand and of household income'],
        ['Consumer price inflation', 'The rate of increase in retail prices '
                                     'of a representative basket',
         'Determines real purchasing power and the ability of a company to '
         'take a price increase'],
        ['Food inflation', 'Inflation in food articles within the consumer '
                           'price index',
         'Raises the cost of agricultural raw materials and reduces the '
         'discretionary spending of rural households'],
        ['Policy interest rate', 'The rate at which the central bank lends '
                                 'against government securities',
         'Sets the cost of working capital, the attractiveness of consumer '
         'credit and the valuation multiple of equities'],
        ['Private final consumption expenditure',
         'The share of gross domestic product spent by households',
         'The direct demand base of the sector'],
        ['Rural wage and monsoon conditions',
         'The level of rural cash income and agricultural output',
         'Drives demand for the rural-weighted part of the portfolio'],
        ['Goods and services tax rates',
         'The indirect tax applicable to a product category',
         'Alters the effective price point and therefore the addressable '
         'market of a product'],
    ], [2200, 4300, 3966], aligns=['l', 'l', 'l'])
    doc.after_table(0.5)

    doc.para('B.  The current state of the Indian economy, 2026', bold=True,
             align='left', before=140)
    para(
        'Report date: August to October 2026. India remains one of the '
        'fastest-growing major economies, but its current position is a '
        'combination of strong domestic growth and rising external and '
        'inflationary risk. The economy is supported by consumption, '
        'investment, infrastructure spending, services and improving '
        'financial-sector conditions. At the same time, higher food and energy '
        'prices, geopolitical tension, rupee depreciation and global trade '
        'uncertainty are the principal risks.')
    para(
        'The Economic Survey estimated real gross domestic product growth at '
        '7.4 per cent for FY2025-26 and projected growth of 6.8 to 7.2 per '
        'cent for FY2026-27. The Reserve Bank of India\u2019s projection, made '
        'in August 2026, is more cautious at 6.7 per cent for FY2026-27. The '
        'Survey describes the growth model as being supported by what it '
        'describes as a double engine of consumption and investment. Private '
        'final consumption expenditure accounted for 61.5 per cent of gross '
        'domestic product in FY2025-26.')
    doc.para('Table 5.2: Gross domestic product growth in India',
             bold=True, align='left', before=120)
    doc.table([
        ['Indicator', 'Figure'],
        ['Real gross domestic product growth, FY2025-26 (Economic Survey '
         'estimate)', '7.4 per cent'],
        ['Projection for FY2026-27 (Economic Survey)', '6.8 to 7.2 per cent'],
        ['Projection for FY2026-27 (Reserve Bank of India, August 2026)',
         '6.7 per cent'],
        ['Estimated potential growth rate', 'approximately 7 per cent'],
        ['Private final consumption expenditure, FY2025-26',
         '61.5 per cent of gross domestic product'],
    ], [7400, 3066], aligns=['l', 'l'])
    doc.after_table(0.5)
    para(
        'The significance of these figures for the sector analysed in this '
        'report is indirect but important. A growth rate of about seven per '
        'cent, with consumption contributing so large a share, means that the '
        'volume of goods purchased by households is expanding in line with '
        'income. At the same time, a projected slowdown from 7.4 to 6.7 per '
        'cent between FY2025-26 and FY2026-27 indicates that the growth of '
        'that demand is likely to be slower in the year ahead, which is '
        'relevant to the valuation multiples that the market is willing to '
        'pay for consumer companies.')

    doc.para('C.  Inflation and consumer purchasing power', bold=True,
             align='left', before=140)
    para(
        'Inflation is a sustained increase in the general price level. When it '
        'rises, the purchasing power of money falls. India uses the consumer '
        'price index for retail inflation and for monetary policy decisions, '
        'and the reserve bank operates within a tolerance band of two to six '
        'per cent around a target of four per cent.')
    doc.para('Table 5.3: Consumer price inflation in India, 2026',
             bold=True, align='left', before=120)
    doc.table([
        ['Measure', 'Figure'],
        ['Consumer price index inflation, July 2026', '4.45 per cent'],
        ['Consumer price index inflation, June 2026', '4.38 per cent'],
        ['Rural inflation, July 2026', '4.84 per cent'],
        ['Urban inflation, July 2026', '3.96 per cent'],
        ['Food inflation, July 2026', '5.52 per cent'],
        ['Reserve Bank of India target', '4 per cent'],
        ['Tolerance band', '2 to 6 per cent'],
    ], [7400, 3066], aligns=['l', 'l'])
    doc.after_table(0.5)
    para(
        'Headline inflation of 4.45 per cent is above the reserve bank\u2019s '
        'target but comfortably inside the tolerance band, which means that '
        'the direction of inflation matters more than its level. The important '
        'point for an FMCG company is the composition. Food inflation at 5.52 '
        'per cent is higher than headline inflation, and rural inflation at '
        '4.84 per cent is higher than urban inflation at 3.96 per cent. Food '
        'and rural inflation work in opposite directions for the sector: they '
        'raise the cost of agricultural raw materials such as wheat, milk '
        'solids and edible oils, while at the same time reducing the '
        'discretionary purchasing power of rural households. A company with a '
        'rural-weighted portfolio therefore faces both a cost increase and a '
        'demand constraint in the same period, and this is visible in the '
        'financial statements discussed later in this chapter.')

    doc.para('D.  Interest rates and the cost of capital', bold=True,
             align='left', before=140)
    para(
        'Monetary policy is the process through which the reserve bank manages '
        'interest rates, liquidity and credit conditions in order to maintain '
        'price stability while supporting growth. The most important policy '
        'rate is the repo rate, at which the central bank lends against '
        'government securities.')
    doc.para('Table 5.4: Policy rates in India, as at August 2026',
             bold=True, align='left', before=120)
    doc.table([
        ['Monetary policy indicator', 'Rate'],
        ['Repo rate', '5.25 per cent'],
        ['Standing deposit facility', '5.00 per cent'],
        ['Marginal standing facility and bank rate', '5.50 per cent'],
        ['Reserve Bank of India inflation target', '4 per cent'],
    ], [7400, 3066], aligns=['l', 'l'])
    doc.after_table(0.5)
    para(
        'The reserve bank kept the repo rate unchanged at 5.25 per cent in '
        'August 2026 and maintained a neutral stance, projecting real gross '
        'domestic product growth of 6.7 per cent and inflation of 5.0 per cent '
        'for FY2026-27. For the FMCG sector the rate matters through three '
        'separate channels. It determines the cost of short-term working '
        'capital, which in this sector is small because operations are partly '
        'financed by trade credit. It determines the cost of the borrowings '
        'that fund capacity expansion, which is material for the more '
        'capital-intensive companies. And it determines the discount rate at '
        'which future earnings are valued, which is the reason the price to '
        'earnings multiples of consumer companies are sensitive to the '
        'interest rate cycle even when their own borrowings are negligible.')

    doc.para('E.  Input costs, distribution and competition', bold=True,
             align='left', before=140)
    para(
        'The cost structure of an FMCG company has three large components: raw '
        'and packaging materials, advertising and promotion, and the '
        'distribution network. Raw material cost is the largest and the least '
        'controllable. A biscuit manufacturer buys wheat flour, sugar and '
        'edible oil; a personal care company buys packaging polymers, '
        'surfactants and fragrance; a health and wellness company buys herbs '
        'and food ingredients. Because the products are everyday necessities, '
        'a manufacturer cannot pass on an input cost increase in full without '
        'losing volume, and the usual response is to reduce the pack size or '
        'absorb part of the increase in the gross margin. The operating ratio '
        'computed in Chapter 6 measures the result of those decisions.')
    para(
        'Distribution is the second structural cost. Reaching several million '
        'retail outlets requires a network of carrying and forwarding agents, '
        'distributors and frontline sales staff, and it is the principal '
        'reason that established companies hold a lasting advantage. The '
        'network is also the reason the shift of volume towards e-commerce and '
        'quick commerce matters. E-commerce accounted for nearly 18 per cent of '
        'FMCG sales across the top eight metro cities in the quarter ended '
        'December 2025, against an urban average of about six per cent, and '
        'quick commerce now accounts for 70 to 75 per cent of total e-grocery '
        'orders. These channels reach the consumer faster, but the commission '
        'and platform costs attaching to them are higher than those of general '
        'trade, so a shift in channel mix can reduce the operating margin even '
        'when total revenue is rising.')
    para(
        'Advertising is the third component and it is discretionary in '
        'principle but not in practice, because market share in a branded '
        'category depends on continuous visibility. FMCG was the largest '
        'advertising sector in India in 2024, contributing about 34 per cent '
        'of total advertising expenditure with spends of approximately '
        'Rs. 31,428 crore. Competition has also become more fragmented. New '
        'product launches in the sector rose 1.8 times in the year ending May '
        '2025, but only about four per cent of those launches reached a market '
        'penetration of even one per cent, which means that the cost of failed '
        'innovation is now a material item in the advertising and distribution '
        'budgets of the larger companies.')

    doc.para('F.  Regulation and tax', bold=True, align='left', before=140)
    para(
        'The sector operates under food safety and standards regulation, legal '
        'metrology requirements for packaged goods, and advertising codes that '
        'restrict the promotion of certain product categories to children. '
        'Indirect tax affects the sector more directly than direct tax. The '
        'rate of goods and services tax applicable to a product determines its '
        'effective retail price and therefore the size of the market it can '
        'address; the rate structure was revised for several consumer '
        'categories in the recent past, and the effect on any individual '
        'company depends on the mix of products in its portfolio. A company '
        'whose portfolio is skewed towards the categories on which the rate '
        'was reduced benefits from a lower retail price point and from the '
        'resulting volume, while a company whose portfolio is skewed the other '
        'way may see its price advantage eroded.')

    doc.para('G.  Changing consumer preferences and the digital channel',
             bold=True, align='left', before=140)
    para(
        'Three changes in consumer behaviour are visible in the data and are '
        'relevant to the analysis that follows. The first is a shift towards '
        'health and natural products, which is the segment in which Dabur '
        'operates and towards which the larger companies are also moving. The '
        'second is a preference for convenience, which favours smaller pack '
        'sizes in rural markets and ready-to-consume formats in urban ones. '
        'The third is a willingness to purchase everyday goods online, which '
        'has changed the bargaining position of the manufacturer relative to '
        'the traditional trade channel. The sector recorded value growth of '
        '13.9 per cent with volume growth of six per cent in the June 2026 '
        'quarter, and value growth of 12.9 per cent with volume growth of 5.4 '
        'per cent in the September 2026 quarter, with rural volume growth of '
        '7.7 per cent in the latter quarter. Value growing faster than volume '
        'in both quarters is consistent with a mix that is shifting towards '
        'higher-priced products rather than with an increase in the quantity '
        'consumed.')
    fig('fig5_1', 6.2, 3.0, before=140, after=80)
    doc.para('Figure 5.1: Value and volume growth of the Indian FMCG market',
             bold=True, align='center', size=11.0)
    para(
        'The comparison is important for interpretation. Growth in value can '
        'be achieved by raising prices or by selling a more expensive mix, '
        'neither of which requires more goods to be sold. Growth in volume '
        'requires more goods to be sold. A company whose revenue growth comes '
        'predominantly from price and mix will report the same revenue as a '
        'company whose growth comes from volume, but the second is more likely '
        'to be sustainable because it reflects a genuine increase in '
        'consumption.')

    doc.para('H.  Economic risks relevant to the sector', bold=True,
             align='left', before=140)
    for b in [
        'Food inflation: food inflation of 5.52 per cent in July 2026, higher '
        'than headline inflation, raises the cost of agricultural inputs and '
        'compresses the gross margin of food and health companies.',
        'Rural demand slowdown: rural volume growth fell to 3.6 per cent in '
        '2025 from five per cent in 2024. A second consecutive year of weak '
        'rural growth would affect the companies with the largest rural '
        'exposure most severely.',
        'Crude oil and packaging costs: India imports a substantial part of '
        'its crude oil requirement, and packaging materials derived from '
        'polymers move with the price of oil. A rise in oil prices therefore '
        'raises packaging cost across the whole sector.',
        'Rupee depreciation: a weaker rupee raises the landed cost of imported '
        'raw materials such as edible oil and of imported machinery, and it '
        'increases the reported cost of foreign-currency denominated '
        'borrowings.',
        'Global trade uncertainty and tariffs: trade fragmentation and weaker '
        'global demand affect the export earnings of companies with an '
        'international business and the general level of business confidence.',
        'Consumption recovery that is slower than expected: the sector\u2019s '
        'FY2025-26 revenue growth was expected at six to eight per cent, and a '
        'shortfall against that expectation would leave the current valuation '
        'multiples without support.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)


# ---------------------------------------------------------------------------
# 5.2  Industry analysis
# ---------------------------------------------------------------------------
def _industry(doc, fig):
    doc.heading('5.2 INDUSTRY ANALYSIS (FMCG INDUSTRY DRIVERS & TRENDS)', 2,
                '   5.2 Industry Analysis (FMCG Industry Drivers and Trends)')
    para = lambda t, **kw: doc.para(t, align='both', **kw)
    doc.para('Introduction', bold=True, align='left', before=140)
    para(
        'India has a strong position in the FMCG sector, supported by a large '
        'domestic market, a young population, a manufacturing base that has '
        'been strengthened by production-linked incentive schemes, and a '
        'distribution system that reaches both metropolitan and rural '
        'markets. The sector supplies essential consumption goods to '
        'households, which makes it important for economic stability as well '
        'as for growth.')
    doc.para('Key industry highlights', bold=True, align='left', before=140)
    for b in [
        'The Indian FMCG market generated revenue of approximately Rs. 25 lakh '
        'crore, or US$ 289.1 billion, in 2025 and is expected to reach nearly '
        'US$ 642.87 billion by 2030, a compound annual growth rate of 17.3 per '
        'cent through 2025 to 2030.',
        'The sector is the fourth largest in the Indian economy and provides '
        'employment to around three million people, about five per cent of '
        'total factory employment.',
        'Household and personal care products contribute about 50 per cent of '
        'total FMCG sales, followed by food and beverages, health and '
        'wellness, and other categories.',
        'The urban segment contributes about 62 per cent of revenue and rural '
        'India more than 38 per cent, with rural markets having been the '
        'stronger growth driver in recent years until the slowdown in 2025.',
        'The sector recorded value growth of 13.9 per cent and volume growth '
        'of six per cent in the June 2026 quarter, and value growth of 12.9 '
        'per cent and volume growth of 5.4 per cent in the September 2026 '
        'quarter.',
        'Sector revenue growth for FY2025-26 was expected at six to eight per '
        'cent, supported by stable rural demand and a revival in urban '
        'markets.',
        'FMCG was the largest advertising sector in India in 2024 with spends '
        'of about Rs. 31,428 crore, approximately 34 per cent of total '
        'advertising expenditure.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)
    fig('fig5_2', 6.2, 3.0, before=140, after=80)
    doc.para('Figure 5.2: Composition of Indian FMCG sales by broad category',
             bold=True, align='center', size=11.0)

    doc.para('Major market drivers', bold=True, align='left', before=140)
    for b in [
        'Consumption growth and income levels: the growth of private final '
        'consumption expenditure, which accounted for 61.5 per cent of gross '
        'domestic product in FY2025-26, is the single largest driver of sector '
        'demand.',
        'Rural market expansion: rural consumption presents the largest '
        'opportunity for distribution expansion in tier two and tier three '
        'cities. Companies have responded by strengthening rural dealer '
        'networks and by introducing affordable pack sizes.',
        'Quick commerce and e-commerce: quick commerce currently has a '
        'penetration of only about seven per cent of a potential market of '
        'US$ 45 billion, and it has delivered a sales increase of 50 to 100 '
        'per cent to FMCG companies in FY2024-25. This channel is the fastest '
        'growing route to the consumer.',
        'Premiumisation: rising incomes and greater awareness have moved '
        'demand towards higher-priced variants within the same category, which '
        'supports margin even where volume growth is modest.',
        'Emerging categories: the healthy snack market was valued at US$ 3.13 '
        'billion in 2025 and is expected to reach US$ 4.77 billion by 2034, '
        'and the pet care market is projected to grow from about '
        'Rs. 89,743 crore in FY2023-24 to about Rs. 1,38,461 crore by '
        'FY2031-32. New categories extend the addressable market of the '
        'established companies.',
        'Government policy and investment: the production-linked incentive '
        'scheme for food processing has an outlay of Rs. 10,900 crore and had, '
        'up to June 2025, approved 278 units, attracted about Rs. 9,032 crore '
        'of investment and created about 3.4 lakh jobs.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)

    doc.para('Key segments of the sector', bold=True, align='left', before=140)
    doc.para('Table 5.5: Principal segments of the Indian FMCG sector',
             bold=True, align='left', before=120)
    doc.table([
        ['Segment', 'What it comprises', 'Representative companies'],
        ['Home care', 'Detergents, dishwashing products, surface cleaners, '
                      'insecticides and air care',
         'Hindustan Unilever, Godrej Consumer Products, Jyothy Labs'],
        ['Beauty, wellbeing and personal care',
         'Soaps, shampoos, hair oil, oral care, skin care, deodorants and '
         'colour cosmetics',
         'Hindustan Unilever, Dabur, Colgate-Palmolive, Marico, Emami'],
        ['Foods and beverages', 'Biscuits, breads, dairy, packaged foods, '
                                'instant noodles, coffee, tea, salt and '
                                'spices',
         'Britannia, Nestl\u00e9 India, Tata Consumer Products, ITC, Marico'],
        ['Health and wellness', 'Ayurvedic medicines, health supplements, '
                                'digestives and natural personal care',
         'Dabur, Emami, Zydus Wellness, Himalaya'],
        ['Pet care and emerging categories',
         'Pet food, premium snacks, functional foods and direct-to-consumer '
         'brands', 'Marico, and several newer listed and unlisted entrants'],
    ], [2300, 4300, 3866], aligns=['l', 'l', 'l'])
    doc.after_table(0.5)

    doc.para('Challenges and outlook', bold=True, align='left', before=140)
    para(
        'The sector enters FY2026-27 with three structural issues unresolved. '
        'Volume growth has moderated and the rural-urban gap has widened, with '
        'rural volume growth falling to 3.6 per cent in 2025 against urban '
        'growth of 4.6 per cent. Competition from digital-first brands has '
        'raised the cost of innovation without materially improving the '
        'success rate of new launches. And the shift of volume towards quick '
        'commerce and e-commerce, while expanding reach, carries a higher '
        'channel cost than general trade. Against these, the sector retains '
        'its principal advantages: demand that does not disappear in a '
        'downturn, an established distribution network that is difficult to '
        'replicate, and a balance sheet that converts operating profit into '
        'cash reliably. The outlook for FY2026-27 is for revenue growth of six '
        'to eight per cent, with the direction of rural demand and the '
        'movement of agricultural commodity prices being the two variables '
        'that will determine whether individual companies meet that '
        'expectation.')


# ---------------------------------------------------------------------------
# 5.3  Hindustan Unilever Ltd.
# ---------------------------------------------------------------------------
def _company_header(doc, name, n):
    doc.heading('5.%d COMPANY ANALYSIS \u2013 %s' % (n, name), 2,
                '   5.%d Company Analysis \u2013 %s' % (n, name))


def _fin_table(doc, caption, rows, widths=None):
    doc.para(caption, bold=True, align='left', before=120)
    doc.table(rows, widths or [4300, 2055, 2055, 2056],
              aligns=['l', 'r', 'r', 'r'])
    doc.after_table(0.4)


def _hul(doc, fig):
    _company_header(doc, 'HINDUSTAN UNILEVER LTD.', 3)
    para = lambda t, **kw: doc.para(t, align='both', **kw)
    para(
        'Hindustan Unilever Ltd. is an Indian consumer goods company and the '
        'Indian listed subsidiary of Unilever plc. It is the largest pure-play '
        'FMCG company in the country, with a portfolio of more than fifty '
        'brands across fifteen categories, manufacturing facilities at '
        'multiple locations in India and a distribution network that reaches '
        'both urban and rural markets. The company describes its business as '
        'comprising three segments: Home Care, Beauty and Wellbeing, and '
        'Personal Care, with a Foods and Refreshment business alongside them.')
    doc.para('1.  Company overview and corporate identity', bold=True,
             align='left', before=140)
    doc.para('Table 5.6: Hindustan Unilever Ltd. \u2014 company identification',
             bold=True, align='left', before=120)
    doc.table([
        ['Particular', 'Detail'],
        ['Company name', 'Hindustan Unilever Limited'],
        ['NSE symbol and BSE scrip code',
         'HINDUNILVR; BSE 500696'],
        ['Sector and industry', 'Fast moving consumer goods; household and '
                                'personal products'],
        ['Corporate website', 'www.hul.co.in'],
        ['Registered office', 'Unilever House, B. D. Sawant Marg, Chakala, '
                              'Andheri East, Mumbai 400099, Maharashtra'],
        ['Year of incorporation', 'Incorporated in 1933 as Lever Brothers '
                                  'India Limited; renamed Hindustan Unilever '
                                  'Limited in 2007'],
        ['Ultimate holding company', 'Unilever plc, through Unilever Overseas '
                                     'Holdings B.V.'],
        ['Chief Executive Officer and Managing Director',
         '[ADD: verify the name of the incumbent at the date of submission]'],
        ['Face value', 'Re. 1.00 per equity share'],
        ['Equity shares outstanding', 'approximately 235.0 crore shares'],
        ['Market capitalisation as at 12 October 2026',
         'approximately Rs. 4,34,962 crore'],
        ['Market price as at 12 October 2026', 'Rs. 1,850.90'],
        ['52 week high and low', 'Rs. 2,667.20 and Rs. 1,826.90'],
        ['Study period', 'FY2023-24 to FY2025-26'],
    ], [3400, 7066], aligns=['l', 'l'])
    doc.after_table(0.5)

    doc.para('2.  History and milestones', bold=True, align='left',
             before=140)
    para(
        'The company was incorporated in 1933 and was for most of its history '
        'known as Hindustan Lever Limited. It was renamed Hindustan Unilever '
        'Limited in 2007. Its growth has been built on a series of brand '
        'acquisitions and launches rather than on a single product, and its '
        'scale in the Indian market comes as much from distribution as from '
        'manufacturing. Important milestones include:')
    for b in [
        '1933: incorporation as Lever Brothers India Limited, the first '
        'Unilever operation in India.',
        '1956: listing on Indian stock exchanges, with a large minority '
        'shareholding retained by Indian investors.',
        '1990s: expansion into personal care and foods, including the '
        'acquisition of the Lakm\u00e9 and Ponds brands and the launch of '
        'Ayush products.',
        '2007: renaming of the company as Hindustan Unilever Limited.',
        '2020: uniting of the foods and refreshment businesses and '
        'consolidation of the company\u2019s portfolio around a smaller number '
        'of larger brands.',
        '2025: demerger of the ice cream business into Kwality Wall\u2019s '
        '(India) Ltd., completed with effect from 1 December 2025, with the '
        'ice cream undertaking transferred to the new entity and the gain on '
        'transfer recognised in the company\u2019s consolidated profit and '
        'loss account.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)

    doc.para('3.  Products, brands and revenue segments', bold=True,
             align='left', before=140)
    para(
        'The portfolio is organised into four principal reporting groups. Home '
        'Care comprises fabric wash, household care and cleaning products. '
        'Beauty and Wellbeing comprises skin care, hair care, colour cosmetics '
        'and the premium personal care businesses. Personal Care comprises '
        'soaps, oral care and mass hair care. Foods comprises tea, coffee, '
        'packaged foods, health food drinks and culinary products. The brands '
        'include several of the most recognised consumer names in India, and '
        'the company states that its products reach a very large share of '
        'Indian households. Table 5.7 sets out the segment structure and the '
        'approximate contribution of each group to revenue.')
    doc.para('Table 5.7: Hindustan Unilever Ltd. \u2014 principal segments and '
             'product groups', bold=True, align='left', before=120)
    doc.table([
        ['Segment', 'Principal categories',
         'Indicative share of revenue'],
        ['Home Care', 'Fabric wash, household care, dishwashing and surface '
                      'cleaning', 'approximately one third'],
        ['Beauty and Wellbeing', 'Skin care, hair care, colour cosmetics and '
                                 'premium beauty', 'approximately one fifth'],
        ['Personal Care', 'Soaps, oral care and mass hair care',
         'approximately one fifth'],
        ['Foods', 'Tea, coffee, packaged foods, health food drinks and '
                  'culinary products', 'approximately one fifth'],
    ], [2400, 5100, 2966], aligns=['l', 'l', 'l'])
    doc.after_table(0.5)
    para(
        'The relevant point about this structure for the analysis that follows '
        'is that no single group contributes more than about a third of '
        'revenue. The company is therefore less exposed to the performance of '
        'any single category than a company concentrated in one product line, '
        'but it is also less able to grow faster than the sector simply by '
        'being present in a fast-growing category.')

    doc.para('4.  Financial performance, FY2023-24 to FY2025-26', bold=True,
             align='left', before=140)
    _fin_table(doc,
               'Table 5.8: Hindustan Unilever Ltd. \u2014 consolidated income '
               'statement (Rs. crore)',
               [['Particulars', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
                ['Net revenue from operations', '61,896', '61,328', '64,468'],
                ['Operating expenses', '47,237', '46,630', '49,429'],
                ['Operating profit', '14,659', '14,698', '15,039'],
                ['Operating profit margin (%)', '23.68', '23.97', '23.33'],
                ['Other income', '817', '1,355', '4,923'],
                ['Interest expense', '334', '381', '410'],
                ['Depreciation and amortisation', '1,216', '1,253', '1,333'],
                ['Profit before tax', '13,926', '14,419', '18,219'],
                ['Tax', '3,644', '3,748', '3,160'],
                ['Profit after tax', '10,282', '10,671', '15,059'],
                ['Earnings per share (Rs.)', '43.74', '45.32', '64.01']])
    para(
        'Revenue was almost flat between FY2023-24 and FY2024-25, falling '
        'marginally by 0.92 per cent, and then grew 5.12 per cent in '
        'FY2025-26. Operating profit moved in a narrow band between '
        'Rs. 14,659 crore and Rs. 15,039 crore across the three years, and the '
        'operating margin was between 23.3 and 24.0 per cent throughout. This '
        'is the profile of a mature company in a saturated category: the '
        'business is highly profitable and highly stable, but it is not '
        'growing quickly.')
    para(
        'The reported profit after tax for FY2025-26 of Rs. 15,059 crore '
        'requires specific explanation, because it is not comparable with the '
        'two preceding years. Of that figure, approximately Rs. 4,611 crore '
        'represents a one-time exceptional gain arising from the demerger of '
        'the ice cream business into Kwality Wall\u2019s (India) Ltd., '
        'recognised in accordance with the approved scheme of demerger and the '
        'applicable accounting standards. The gain is an accounting '
        'adjustment measured as the excess of the fair value of the '
        'transferred undertaking over the carrying value of its net assets; it '
        'does not represent cash received by the company and it will not '
        'recur. The company also recorded an exceptional charge in the same '
        'year on account of the implementation of the new labour codes. '
        'Excluding exceptional items, the underlying profit after tax grew by '
        'a low single-digit percentage, which is consistent with the movement '
        'of operating profit.')
    para(
        'Table 5.9 shows the effect of the one-time item on the reported '
        'figures. In the comparative ratio analysis presented in Chapter 6 the '
        'normalised figures have been used for FY2025-26, so that the ratios '
        'of the three companies reflect recurring operating performance rather '
        'than the effect of a non-recurring transaction.')
    _fin_table(doc,
               'Table 5.9: Hindustan Unilever Ltd. \u2014 reported and '
               'normalised profit after tax, FY2025-26 (Rs. crore)',
               [['Particulars', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
                ['Profit after tax as reported', '10,282', '10,671', '15,059'],
                ['Less: one-time gain on the demerger of the ice cream '
                 'undertaking', '\u2014', '\u2014', '(4,611)'],
                ['Profit after tax, normalised', '10,282', '10,671', '10,448'],
                ['Earnings per share as reported (Rs.)', '43.74', '45.32',
                 '64.01'],
                ['Earnings per share, normalised (Rs.)', '43.74', '45.32',
                 '44.46']])
    para(
        'The difference is material. On the reported figures, earnings per '
        'share rose 41.2 per cent in FY2025-26; on the normalised figures it '
        'rose 1.6 per cent and remained slightly below the level of '
        'FY2023-24. Any conclusion about the company\u2019s earnings momentum '
        'that is drawn from the reported figure alone would therefore be '
        'incorrect.')
    fig('fig5_3', 6.1, 2.9, before=140, after=60)
    doc.para('Figure 5.3: Hindustan Unilever Ltd. \u2014 net revenue and '
             'profit after tax, FY2023-24 to FY2025-26', bold=True,
             align='center', size=11.0)
    para(
        'The revenue chart is almost flat, which is the central fact about the '
        'company. Revenue of Rs. 64,468 crore in FY2025-26 is 4.2 per cent '
        'higher than in FY2023-24, an increase of approximately 2.1 per cent a '
        'year over two years. That rate is below both nominal gross domestic '
        'product growth and the rate of inflation over the same period, which '
        'means the company has been losing volume in real terms.')

    doc.para('5.  Balance sheet and cash flow position', bold=True,
             align='left', before=140)
    _fin_table(doc,
               'Table 5.10: Hindustan Unilever Ltd. \u2014 consolidated '
               'balance sheet (Rs. crore)',
               [['Particulars', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
                ['Equity share capital', '235.00', '235.00', '235.00'],
                ['Reserves and surplus', '50,983.00', '49,167.00', '48,504.00'],
                ['Shareholders\u2019 funds', '51,218.00', '49,402.00',
                 '48,739.00'],
                ['Total borrowings (memorandum)', '13.00', '1.00', '0.00'],
                ['Total current liabilities', '12,876.00', '16,537.00',
                 '15,549.00'],
                ['Total non-current assets', '57,175.00', '57,829.00',
                 '60,731.00'],
                ['Total current assets', '21,324.00', '22,051.00', '19,021.00'],
                ['Total assets', '78,499.00', '79,880.00', '79,752.00'],
                ['Total equity and liabilities', '78,499.00', '79,880.00',
                 '79,752.00']])
    _fin_table(doc,
               'Table 5.11: Hindustan Unilever Ltd. \u2014 consolidated cash '
               'flow statement (Rs. crore)',
               [['Particulars', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
                ['Cash from operating activities', '15,469', '11,886',
                 '10,999'],
                ['Cash from investing activities', '(5,324)', '6,473',
                 '(3,677)'],
                ['Cash from financing activities', '(10,034)', '(13,101)',
                 '(10,810)'],
                ['Net cash flow', '111', '5,258', '(3,488)'],
                ['Free cash flow', '14,012', '10,624', '9,667'],
                ['Operating cash flow as a percentage of operating profit',
                 '108', '96', '105']])
    para(
        'Two features of the balance sheet stand out. The first is that the '
        'company is effectively debt free, with total borrowings of less than '
        'Rs. 15 crore in each of the three years against shareholders\u2019 '
        'funds of nearly Rs. 50,000 crore. The second is that shareholders\u2019 '
        'funds fell in each of the two years, from Rs. 51,218 crore to '
        'Rs. 48,739 crore, because the distributions made to shareholders '
        'exceeded the profit earned. Reserves fell by Rs. 1,816 crore in '
        'FY2024-25, a year in which the company earned Rs. 10,671 crore, which '
        'can only be explained by distributions in excess of that year\u2019s '
        'profit. A company can do this for a year without borrowing only '
        'because it carries no debt and generates a large operating cash flow, '
        'and the reduction in reserves is the counterpart of that decision.')
    para(
        'The cash flow statement shows operating cash flow declining from '
        'Rs. 15,469 crore in FY2023-24 to Rs. 10,999 crore in FY2025-26. That '
        'reduction is significant, because it occurred while operating profit '
        'was rising slightly. The explanation is working capital: the '
        'difference between the cash generated and the profit reported '
        'narrowed over the period. Despite this, operating cash flow remained '
        'at 105 per cent of operating profit in FY2025-26, which indicates '
        'that the reported profit continues to be supported by cash, and free '
        'cash flow of Rs. 9,667 crore remains more than sufficient to fund the '
        'dividend.')

    doc.para('6.  Ratio analysis', bold=True, align='left', before=140)
    _fin_table(doc,
               'Table 5.12: Hindustan Unilever Ltd. \u2014 key financial '
               'ratios',
               [['Ratio', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
                ['Net profit margin (%)', '16.61', '17.40', '16.21*'],
                ['Operating profit margin (%)', '23.68', '23.97', '23.33'],
                ['Operating ratio (%)', '76.32', '76.03', '76.67'],
                ['Return on capital employed (%)', '27.83', '29.96', '28.76*'],
                ['Return on equity (%)', '20.07', '21.60', '21.44*'],
                ['Return on assets (%)', '13.10', '13.36', '13.10*'],
                ['Return on investment (%)', '20.07', '21.60', '21.44*'],
                ['Debt to equity (times)', '0.00', '0.00', '0.00'],
                ['Interest coverage (times)', '42.69', '38.85', '34.19*'],
                ['Current ratio (times)', '1.66', '1.33', '1.22'],
                ['Earnings per share (Rs.)', '43.74', '45.32', '44.46*'],
                ['Book value per share (Rs.)', '217.95', '210.22',
                 '207.40']])
    para(
        '* Computed on the normalised profit after tax of Rs. 10,448 crore for '
        'FY2025-26, excluding the one-time gain of Rs. 4,611 crore arising '
        'from the demerger of the ice cream undertaking. The formulas applied '
        'are stated in Chapter 6. Return on investment, defined as profit '
        'after tax divided by shareholders\u2019 funds plus total borrowings, '
        'coincides with return on equity in the case of this company because '
        'the borrowings are negligible. Book value per share is computed on '
        'the 235.00 crore equity shares outstanding as at 31 March 2026.')
    para(
        'The ratio profile is that of an exceptionally safe business with '
        'modest growth. Profitability is stable, between 16 and 17.5 per cent '
        'at the net level and between 23 and 24 per cent at the operating '
        'level, and the operating ratio is the lowest of the three companies '
        'studied, which means the company spends the smallest proportion of '
        'each rupee of revenue on running the business. Leverage is nil and '
        'interest coverage is therefore extremely high, although the ratio '
        'declined from 42.69 to 34.19 times as interest expense rose against a '
        'flat operating profit. The current ratio declined from 1.66 to 1.22 '
        'over the three years as current liabilities increased faster than '
        'current assets, which is a mild liquidity consideration rather than a '
        'concern given the absence of debt.')

    doc.para('7.  Strengths, weaknesses, opportunities and threats', bold=True,
             align='left', before=140)
    doc.para('Table 5.13: Hindustan Unilever Ltd. \u2014 SWOT analysis',
             bold=True, align='left', before=120)
    doc.table([
        ['Strengths', 'Weaknesses'],
        ['\u2022  The largest distribution network in the Indian FMCG sector '
         'and a portfolio of more than fifty brands, several of which lead '
         'their category.\n'
         '\u2022  Effectively debt free, with the lowest operating ratio of '
         'the three companies studied and the strongest interest coverage.\n'
         '\u2022  Consistent cash generation: operating cash flow was 105 per '
         'cent of operating profit in FY2025-26 and free cash flow of '
         'Rs. 9,667 crore comfortably funds the dividend.\n'
         '\u2022  Access to the parent company\u2019s research and development '
         'and global brand portfolio.',
         '\u2022  Revenue growth has been the slowest of the three companies: '
         '2.1 per cent a year over the two years to FY2025-26.\n'
         '\u2022  Normalised earnings per share was flat at about Rs. 44 '
         'across the three years.\n'
         '\u2022  Distributions to shareholders exceeded the profit earned in '
         'FY2024-25, and reserves were reduced by Rs. 1,816 crore that '
         'year.\n'
         '\u2022  Declining operating cash flow, from Rs. 15,469 crore to '
         'Rs. 10,999 crore, while profit was rising.'],
        ['Opportunities', 'Threats'],
        ['\u2022  Premiumisation in beauty, wellbeing and personal care, '
         'supported by a plan to invest up to Rs. 20,000 crore in '
         'manufacturing capacity in the premium segments.\n'
         '\u2022  Quick commerce and e-commerce, where the company\u2019s mass '
         'brands are under-represented relative to their share of general '
         'trade.\n'
         '\u2022  Growth of the rural market, where the company already '
         'derives 35 to 40 per cent of revenue and supports retail ordering '
         'through a retailer application with about 1.4 million users.\n'
         '\u2022  Recovery in urban discretionary demand as inflation '
         'moderates.',
         '\u2022  Competition from digital-first brands, which has raised the '
         'cost of defending share in personal care and colour cosmetics.\n'
         '\u2022  A shift in channel mix towards quick commerce, which carries '
         'a higher cost to serve than general trade.\n'
         '\u2022  Input cost inflation in packaging and in imported raw '
         'materials, combined with limited ability to raise prices.\n'
         '\u2022  Valuation risk: the shares trade at a high multiple of '
         'earnings that have been flat, which leaves little room for '
         'disappointment.'],
    ], [5233, 5233], aligns=['l', 'l'])
    doc.after_table(0.5)

    doc.para('8.  Competitive position within the sector', bold=True,
             align='left', before=140)
    para(
        'Hindustan Unilever competes with ITC in packaged foods, with '
        'Colgate-Palmolive in oral care, with Godrej Consumer Products in home '
        'care and insecticides, with Marico in hair oil and with Dabur in '
        'natural personal care. Its competitive position rests on scale in '
        'distribution and on the strength of its brands rather than on price, '
        'and its financial statements reflect that position: it earns the '
        'highest net profit margin of the three companies studied, carries no '
        'debt and converts profit into cash reliably. Its weakness is the same '
        'scale that produces those advantages, because a business of this size '
        'cannot grow quickly by taking share in a category that is itself '
        'growing slowly.')


# ---------------------------------------------------------------------------
# 5.4  Britannia Industries Ltd.
# ---------------------------------------------------------------------------
def _britannia(doc, fig):
    _company_header(doc, 'BRITANNIA INDUSTRIES LTD.', 4)
    para = lambda t, **kw: doc.para(t, align='both', **kw)
    para(
        'Britannia Industries Ltd. is one of India\u2019s largest packaged '
        'foods companies and the market leader in biscuits. The company '
        'manufactures and sells biscuits, breads, cakes, rusk, dairy products '
        'and adjacent snacking categories, and it distributes through a '
        'network that reaches both urban markets and a large number of rural '
        'preferred dealers. Its business is more concentrated than that of '
        'Hindustan Unilever, which is the reason it has grown faster and earns '
        'a higher return on the capital it employs.')
    doc.para('1.  Company overview and corporate identity', bold=True,
             align='left', before=140)
    doc.para('Table 5.14: Britannia Industries Ltd. \u2014 company '
             'identification', bold=True, align='left', before=120)
    doc.table([
        ['Particular', 'Detail'],
        ['Company name', 'Britannia Industries Limited'],
        ['NSE symbol and BSE scrip code', 'BRITANNIA; BSE 500825'],
        ['Sector and industry', 'Fast moving consumer goods; consumer food'],
        ['Corporate website', 'www.britannia.co.in'],
        ['Registered office', '5/1A, Hungerford Street, Kolkata 700017, West '
                              'Bengal'],
        ['Year of incorporation', 'Incorporated in 1918 as Britannia Biscuit '
                                  'Company; renamed Britannia Industries '
                                  'Limited in 1979'],
        ['Promoter group', 'Wadia Group'],
        ['Managing Director', '[ADD: verify the name of the incumbent at the '
                               'date of submission; the company announced the '
                               'appointment of a Deputy Managing Director and '
                               'a Chief Financial Officer with effect from '
                               '1 October 2026]'],
        ['Face value', 'Re. 1.00 per equity share'],
        ['Equity shares outstanding', 'approximately 24.09 crore shares'],
        ['Market capitalisation as at 12 October 2026',
         'approximately Rs. 1,15,827 crore'],
        ['Market price as at 12 October 2026', 'Rs. 4,808.10'],
        ['52 week high and low', 'Rs. 6,271.00 and Rs. 4,734.10'],
        ['Study period', 'FY2023-24 to FY2025-26'],
    ], [3400, 7066], aligns=['l', 'l'])
    doc.after_table(0.5)

    doc.para('2.  History and milestones', bold=True, align='left',
             before=140)
    para(
        'The company was incorporated in 1918 as the Britannia Biscuit Company '
        'and was for several decades a subsidiary of Associated Biscuits '
        'International. Control passed to the Wadia Group in the 1990s, after '
        'which the company restructured its business around a smaller number '
        'of larger brands and invested in distribution and in manufacturing '
        'capacity. Important milestones include:')
    for b in [
        '1918: incorporation as Britannia Biscuit Company Limited in Kolkata.',
        '1979: renaming of the company as Britannia Industries Limited.',
        '1990s: change of ownership to the Wadia Group and consolidation of '
        'the biscuit business.',
        '2000s: launch of the Tiger brand at a low price point, which '
        'extended the company\u2019s reach into rural and price-sensitive '
        'markets.',
        '2010s: entry into dairy through a joint venture and gradual expansion '
        'into breads, cakes, rusk and adjacent snacking categories.',
        '2020s: continued investment in distribution through rural preferred '
        'dealers, in cost efficiency programmes and in premium product '
        'variants.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)

    doc.para('3.  Products, brands and revenue segments', bold=True,
             align='left', before=140)
    para(
        'The biscuit business remains the core of the company and includes '
        'well-known brands across price points, from the mass-market Tiger '
        'brand to the premium Good Day, Marie Gold, NutriChoice and Bourbon '
        'brands. The dairy business supplies milk, curd and cheese-based '
        'products. The adjacent businesses include breads, cakes, rusk and '
        'croissants. Because the portfolio is concentrated in biscuits, both '
        'the revenue and the margin of the company depend heavily on the '
        'prices of wheat flour, sugar, edible oil and packaging material.')
    doc.para('Table 5.15: Britannia Industries Ltd. \u2014 principal product '
             'groups', bold=True, align='left', before=120)
    doc.table([
        ['Product group', 'Principal categories', 'Role in the portfolio'],
        ['Biscuits', 'Mass-market, mid-price and premium biscuits across '
                     'several brands',
         'The core business and the largest contributor to revenue'],
        ['Dairy', 'Milk, curd, cheese and related products',
         'A growing business that uses the same distribution network and '
         'raises the value of each delivery'],
        ['Bakery and adjacent categories',
         'Breads, cakes, rusk and croissants',
         'Extends the brand into consumption occasions close to the biscuit '
         'business'],
        ['Premium and health-oriented products',
         'Whole-wheat, millet, sugar-free and high-protein variants',
         'Responds to the shift in consumer preference towards health and '
         'supports margin'],
    ], [2600, 3900, 3966], aligns=['l', 'l', 'l'])
    doc.after_table(0.5)

    doc.para('4.  Financial performance, FY2023-24 to FY2025-26', bold=True,
             align='left', before=140)
    _fin_table(doc,
               'Table 5.16: Britannia Industries Ltd. \u2014 consolidated '
               'income statement (Rs. crore)',
               [['Particulars', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
                ['Net revenue from operations', '16,769', '17,943', '19,152'],
                ['Operating expenses', '13,603', '14,766', '15,638'],
                ['Operating profit', '3,166', '3,177', '3,514'],
                ['Operating profit margin (%)', '18.88', '17.71', '18.35'],
                ['Other income', '211', '202', '224'],
                ['Interest expense', '164', '139', '113'],
                ['Depreciation and amortisation', '300', '313', '337'],
                ['Profit before tax', '2,913', '2,927', '3,289'],
                ['Tax', '779', '749', '752'],
                ['Profit after tax', '2,134', '2,178', '2,537'],
                ['Earnings per share (Rs.)', '88.84', '90.45', '105.18']])
    para(
        'Revenue grew in each of the three years, at 7.00 per cent in '
        'FY2024-25 and 6.74 per cent in FY2025-26, and the compound growth '
        'rate over the two years was 6.87 per cent. Operating profit was '
        'almost unchanged between FY2023-24 and FY2024-25, and the operating '
        'margin fell from 18.88 to 17.71 per cent, before recovering to 18.35 '
        'per cent in FY2025-26 with a 10.61 per cent increase in operating '
        'profit. The pattern indicates that the company absorbed input cost '
        'pressure in FY2024-25 and recovered it in the following year.')
    para(
        'Profit after tax grew 6.49 per cent in FY2024-25 after rising 6.20 per '
        'cent in FY2023-24, and then rose 16.48 per cent in FY2025-26, which '
        'was faster than revenue growth. Two factors explain the acceleration: '
        'operating profit rose faster than revenue, and interest expense fell '
        'from Rs. 139 crore to Rs. 113 crore as the company repaid borrowings. '
        'The effective tax rate also declined from 25.59 to 22.87 per cent in '
        'that year. A part of the FY2025-26 profit growth is therefore '
        'attributable to a lower tax charge rather than to operations, and the '
        'sustainability of the growth rate depends on whether the operating '
        'improvement continues.')
    fig('fig5_4', 6.1, 2.9, before=140, after=60)
    doc.para('Figure 5.4: Britannia Industries Ltd. \u2014 net revenue and '
             'profit after tax, FY2023-24 to FY2025-26', bold=True,
             align='center', size=11.0)
    para(
        'Unlike the chart for Hindustan Unilever, both lines in this chart '
        'slope upward, and the profit line steepens in the final year. The '
        'company has grown its revenue by 14.21 per cent and its profit by '
        '18.88 per cent over the two years, which places it clearly ahead of '
        'the sector\u2019s expected revenue growth of six to eight per cent in '
        'the most recent year.')

    doc.para('5.  Balance sheet and cash flow position', bold=True,
             align='left', before=140)
    _fin_table(doc,
               'Table 5.17: Britannia Industries Ltd. \u2014 consolidated '
               'balance sheet (Rs. crore)',
               [['Particulars', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
                ['Equity share capital', '24.09', '24.09', '24.09'],
                ['Reserves and surplus', '3,917.43', '4,331.63', '5,082.47'],
                ['Shareholders\u2019 funds', '3,941.52', '4,355.72', '5,106.56'],
                ['Non-current borrowings', '904.72', '712.94', '286.11'],
                ['Current borrowings', '1,136.49', '511.83', '1,071.72'],
                ['Total borrowings (memorandum)', '2,041.21', '1,224.77',
                 '1,357.83'],
                ['Total current liabilities', '4,084.41', '3,618.26',
                 '4,179.99'],
                ['Total non-current assets', '4,224.90', '4,924.87', '5,054.28'],
                ['Total current assets', '4,848.66', '3,913.68', '4,677.66'],
                ['Total assets', '9,073.56', '8,838.55', '9,731.94'],
                ['Total equity and liabilities', '9,073.56', '8,838.55',
                 '9,731.94']])
    _fin_table(doc,
               'Table 5.18: Britannia Industries Ltd. \u2014 consolidated cash '
               'flow statement (Rs. crore)',
               [['Particulars', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
                ['Cash from operating activities', '2,573', '2,491', '2,612'],
                ['Cash from investing activities', '485', '69', '(741)'],
                ['Cash from financing activities', '(2,839)', '(2,754)',
                 '(1,783)'],
                ['Net cash flow', '219', '(194)', '88'],
                ['Free cash flow', '2,085', '2,120', '2,408'],
                ['Operating cash flow as a percentage of operating profit',
                 '105', '100', '98']])
    para(
        'The balance sheet shows a deliberate reduction in leverage. Total '
        'borrowings fell from Rs. 2,041 crore to Rs. 1,358 crore, and '
        'shareholders\u2019 funds rose from Rs. 3,942 crore to Rs. 5,107 crore, '
        'so that the debt to equity ratio fell from 0.52 to 0.27 times. The '
        'composition of the borrowings changed as well: long-term borrowings '
        'fell by more than two-thirds, from Rs. 905 crore to Rs. 286 crore, '
        'while short-term borrowings rose, which reduces the average cost of '
        'debt and is consistent with the fall in interest expense from '
        'Rs. 164 crore to Rs. 113 crore.')
    para(
        'Operating cash flow was stable at about Rs. 2,600 crore in each year, '
        'and free cash flow rose to Rs. 2,408 crore in FY2025-26 as capital '
        'expenditure remained moderate. The company paid out Rs. 1,783 crore '
        'in financing activities in FY2025-26, mostly as dividend, and still '
        'added to cash. Operating cash flow was 98 per cent of operating '
        'profit in the final year, which is a small decline from 105 per cent '
        'in FY2023-24 but remains a strong conversion ratio.')

    doc.para('6.  Ratio analysis', bold=True, align='left', before=140)
    _fin_table(doc,
               'Table 5.19: Britannia Industries Ltd. \u2014 key financial '
               'ratios',
               [['Ratio', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
                ['Net profit margin (%)', '12.73', '12.14', '13.25'],
                ['Operating profit margin (%)', '18.89', '17.70', '18.35'],
                ['Operating ratio (%)', '81.12', '82.29', '81.65'],
                ['Return on capital employed (%)', '51.43', '54.94', '52.63'],
                ['Return on equity (%)', '54.14', '50.00', '49.68'],
                ['Return on assets (%)', '23.52', '24.64', '26.07'],
                ['Return on investment (%)', '35.67', '39.03', '39.25'],
                ['Debt to equity (times)', '0.52', '0.28', '0.27'],
                ['Interest coverage (times)', '18.76', '22.06', '30.11'],
                ['Current ratio (times)', '1.19', '1.08', '1.12'],
                ['Earnings per share (Rs.)', '88.84', '90.45', '105.18'],
                ['Book value per share (Rs.)', '163.62', '180.81',
                 '211.98']])
    para(
        'The return ratios are the distinguishing feature of this company. '
        'Return on equity of 49.68 per cent and return on capital employed of '
        '52.63 per cent are far above those of the other two companies '
        'studied, and they reflect the combination of a high net profit margin '
        'relative to the size of the asset base and a comparatively small '
        'equity base. The debt to equity ratio of 0.27 times is higher than '
        'Dabur\u2019s and much higher than Hindustan Unilever\u2019s, but the '
        'return generated on that capital more than compensates, and interest '
        'coverage strengthened from 18.76 to 30.11 times over the three years.')

    doc.para('7.  Strengths, weaknesses, opportunities and threats', bold=True,
             align='left', before=140)
    doc.para('Table 5.20: Britannia Industries Ltd. \u2014 SWOT analysis',
             bold=True, align='left', before=120)
    doc.table([
        ['Strengths', 'Weaknesses'],
        ['\u2022  Market leadership in biscuits and one of the strongest '
         'distribution networks in the Indian packaged foods industry, '
         'including a rural preferred dealer network.\n'
         '\u2022  The highest return on equity and return on capital employed '
         'of the three companies studied, at 49.68 and 52.63 per cent in '
         'FY2025-26.\n'
         '\u2022  Consistent cash generation: operating cash flow of about '
         'Rs. 2,600 crore in each of the three years and free cash flow of '
         'Rs. 2,408 crore in FY2025-26.\n'
         '\u2022  A deliberate reduction in leverage: total borrowings fell '
         'from Rs. 2,041 crore to Rs. 1,358 crore over the three years.',
         '\u2022  Concentration in a single product category. Biscuits account '
         'for the greater part of revenue, so the company is directly exposed '
         'to wheat, sugar and edible oil prices.\n'
         '\u2022  The lowest net profit margin of the three companies studied, '
         'at 13.25 per cent, and the highest operating ratio, at 81.65 per '
         'cent.\n'
         '\u2022  A current ratio below 1.2 times in each year, which leaves '
         'little short-term liquidity buffer.\n'
         '\u2022  Part of the FY2025-26 profit growth came from a lower '
         'effective tax rate rather than from operations.'],
        ['Opportunities', 'Threats'],
        ['\u2022  Growth of the dairy and adjacent bakery businesses, which '
         'use the same distribution network and raise the value of each '
         'delivery.\n'
         '\u2022  Health-oriented and premium variants, including whole-wheat, '
         'millet and high-protein products, which respond to a genuine shift '
         'in consumer preference.\n'
         '\u2022  Continued expansion in rural markets, where the company has '
         'invested in preferred dealer networks.\n'
         '\u2022  Operating leverage on fixed costs if revenue growth continues '
         'at the current rate.',
         '\u2022  Input cost inflation in wheat flour, sugar, edible oil and '
         'packaging, which the company can pass on only gradually.\n'
         '\u2022  Competition in biscuits from regional manufacturers and from '
         'the snacking portfolios of larger diversified companies.\n'
         '\u2022  The steady shift of snacking demand towards savoury and '
         'health-oriented products, in which the company\u2019s portfolio is '
         'less developed than in sweet biscuits.\n'
         '\u2022  Valuation risk: the shares trade at the highest multiple of '
         'the three companies studied, which assumes that the current rate of '
         'earnings growth continues.'],
    ], [5233, 5233], aligns=['l', 'l'])
    doc.after_table(0.5)

    doc.para('8.  Competitive position within the sector', bold=True,
             align='left', before=140)
    para(
        'Britannia competes in biscuits with regional manufacturers and with '
        'the snacking portfolios of companies such as ITC and Nestl\u00e9 '
        'India, and in dairy with the large cooperative and private dairy '
        'brands. Its competitive position rests on cost efficiency and '
        'distribution reach rather than on premium pricing, which is why its '
        'net profit margin is the lowest of the three companies studied while '
        'its return on capital is the highest. That combination is possible '
        'because the business is asset-light relative to its profit and because '
        'it operates with negative working capital, collecting from '
        'distributors before it pays its suppliers.')


# ---------------------------------------------------------------------------
# 5.5  Dabur India Ltd.
# ---------------------------------------------------------------------------
def _dabur(doc, fig):
    _company_header(doc, 'DABUR INDIA LTD.', 5)
    para = lambda t, **kw: doc.para(t, align='both', **kw)
    para(
        'Dabur India Ltd. is the largest Ayurvedic and natural healthcare '
        'company in India and one of the largest FMCG companies in the '
        'country. Its products reach eight out of ten Indian households, and '
        'its portfolio comprises three brands with revenue above Rs. 1,000 '
        'crore, three brands above Rs. 500 crore and sixteen brands in the '
        'range of Rs. 100 to 500 crore. The company derives between 45 and 50 '
        'per cent of its revenue from rural markets and reaches over 1,31,000 '
        'villages and 1.42 million retail outlets, which makes it the most '
        'rural-weighted of the three companies studied.')
    doc.para('1.  Company overview and corporate identity', bold=True,
             align='left', before=140)
    doc.para('Table 5.21: Dabur India Ltd. \u2014 company identification',
             bold=True, align='left', before=120)
    doc.table([
        ['Particular', 'Detail'],
        ['Company name', 'Dabur India Limited'],
        ['NSE symbol and BSE scrip code', 'DABUR; BSE 500096'],
        ['Sector and industry', 'Fast moving consumer goods; personal products '
                                'and consumer healthcare'],
        ['Corporate website', 'www.dabur.com'],
        ['Registered office', '8/3, Asaf Ali Road, New Delhi 110002'],
        ['Year of incorporation', 'Incorporated in 1975; the business itself '
                                  'dates from 1884, when it was founded as a '
                                  'pharmacy in Kolkata'],
        ['Promoter group', 'Burman family'],
        ['Chief Executive Officer', '[ADD: verify the name of the incumbent at '
                                     'the date of submission]'],
        ['Face value', 'Re. 1.00 per equity share'],
        ['Equity shares outstanding', 'approximately 177.37 crore shares'],
        ['Market capitalisation as at 12 October 2026',
         'approximately Rs. 68,128 crore'],
        ['Market price as at 12 October 2026', 'Rs. 384.10'],
        ['52 week high and low', 'Rs. 534.00 and Rs. 368.05'],
        ['Study period', 'FY2023-24 to FY2025-26'],
    ], [3400, 7066], aligns=['l', 'l'])
    doc.after_table(0.5)

    doc.para('2.  History and milestones', bold=True, align='left',
             before=140)
    para(
        'The business began in 1884 as a pharmacy in Kolkata that prepared '
        'Ayurvedic medicines, and it was incorporated as a company in 1975. '
        'Its growth has been built on the conversion of traditional Ayurvedic '
        'remedies into packaged consumer products and on a distribution '
        'network that extends further into rural India than that of most of '
        'its competitors. Important milestones include:')
    for b in [
        '1884: foundation of the business as an Ayurvedic pharmacy in Kolkata.',
        '1975: incorporation of Dabur India Limited.',
        '1990s: professionalisation of the management and expansion from '
        'medicines into personal care products.',
        '2000s: extension of the portfolio into foods, including fruit juices '
        'and packaged honey, and expansion into international markets.',
        '2010s: acquisition of overseas brands in personal care and foods, '
        'particularly in the Middle East, Africa and South Asia, and '
        'consolidation of the domestic business around a smaller number of '
        'larger brands.',
        '2020s: restructuring of the India business into separate verticals '
        'for healthcare, home and personal care, and foods, with continued '
        'investment in rural distribution and in e-commerce.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)

    doc.para('3.  Products, brands and revenue segments', bold=True,
             align='left', before=140)
    para(
        'The business is organised into three India verticals and an '
        'international business. Consumer care comprises hair oil, shampoo, '
        'oral care, skin care and home care products. Healthcare comprises '
        'Ayurvedic medicines, digestives, health supplements and ethical '
        'products. Foods comprises fruit juices, beverages, honey and culinary '
        'products. The international business operates branded consumer '
        'products in a number of markets in the Middle East, Africa and South '
        'Asia.')
    doc.para('Table 5.22: Dabur India Ltd. \u2014 principal business verticals',
             bold=True, align='left', before=120)
    doc.table([
        ['Vertical', 'Principal categories',
         'Characteristics of the business'],
        ['Healthcare', 'Ayurvedic medicines, digestives, health supplements '
                       'and ethical products',
         'The traditional core of the company and the source of its identity '
         'as a natural health company; margins are comparatively high'],
        ['Home and Personal Care',
         'Hair oil, shampoo, oral care, skin care and home care',
         'The largest contributor to revenue; directly competitive with the '
         'personal care portfolios of the larger diversified companies'],
        ['Foods and Beverages',
         'Fruit juices, beverages, honey and culinary products',
         'Grew faster than the rest of the portfolio in recent years and '
         'broadens the company\u2019s exposure beyond health and personal care'],
        ['International business',
         'Branded consumer products in the Middle East, Africa and South Asia',
         'Provides geographic diversification and foreign currency revenue, '
         'and is exposed to currency and political risk'],
    ], [2300, 4200, 3966], aligns=['l', 'l', 'l'])
    doc.after_table(0.5)

    doc.para('4.  Financial performance, FY2023-24 to FY2025-26', bold=True,
             align='left', before=140)
    _fin_table(doc,
               'Table 5.23: Dabur India Ltd. \u2014 consolidated income '
               'statement (Rs. crore)',
               [['Particulars', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
                ['Net revenue from operations', '12,404', '12,563', '13,193'],
                ['Operating expenses', '10,004', '10,247', '10,743'],
                ['Operating profit', '2,400', '2,316', '2,450'],
                ['Operating profit margin (%)', '19.35', '18.44', '18.57'],
                ['Other income', '482', '552', '584'],
                ['Interest expense', '124', '164', '145'],
                ['Depreciation and amortisation', '399', '446', '469'],
                ['Profit before tax', '2,359', '2,258', '2,420'],
                ['Tax', '548', '518', '551'],
                ['Profit after tax', '1,811', '1,740', '1,869'],
                ['Earnings per share (Rs.)', '10.40', '9.97', '10.68']])
    para(
        'Revenue grew slowly, at 1.28 per cent in FY2024-25 and 5.02 per cent '
        'in FY2025-26, and the compound growth rate over the two years was '
        '3.13 per cent. Operating profit was lower in FY2024-25 than in the '
        'preceding year, and the operating margin fell from 19.35 to 18.44 per '
        'cent, before recovering marginally to 18.57 per cent in FY2025-26. '
        'Profit after tax shows the same pattern: it fell 3.92 per cent in '
        'FY2024-25 and then rose 7.41 per cent in FY2025-26, but the '
        'FY2025-26 figure of Rs. 1,869 crore is only 3.20 per cent higher than '
        'the FY2023-24 figure of Rs. 1,811 crore. Earnings per share over the '
        'same period moved from Rs. 10.40 to Rs. 10.68, a compound growth rate '
        'of 1.34 per cent a year.')
    para(
        'The reason for the weak profit growth in FY2024-25 was the '
        'combination of slower revenue growth and a rise in interest expense '
        'from Rs. 124 crore to Rs. 164 crore, together with an increase in '
        'depreciation as capital expenditure was commissioned. The recovery in '
        'FY2025-26 came from a 5.02 per cent increase in revenue and a '
        'reduction in interest expense, and other income also contributed '
        'Rs. 585 crore, which is a larger amount relative to profit than in '
        'either of the other two companies studied. That is a point of '
        'caution in the analysis: a significant part of Dabur\u2019s reported '
        'profit is derived from income earned on its investments rather than '
        'from the sale of goods.')
    fig('fig5_5', 6.1, 2.9, before=140, after=60)
    doc.para('Figure 5.5: Dabur India Ltd. \u2014 net revenue and profit after '
             'tax, FY2023-24 to FY2025-26', bold=True, align='center',
             size=11.0)
    para(
        'The revenue line rises gently and the profit line dips in the middle '
        'year before recovering. Neither line shows the acceleration visible '
        'in the chart for Britannia, which is consistent with the ratio '
        'analysis in Chapter 6: the company\u2019s return on capital employed '
        'has declined from 22.52 to 20.55 per cent over the three years, '
        'because capital employed has grown faster than the profit earned on '
        'it.')

    doc.para('5.  Balance sheet and cash flow position', bold=True,
             align='left', before=140)
    _fin_table(doc,
               'Table 5.24: Dabur India Ltd. \u2014 consolidated balance sheet '
               '(Rs. crore)',
               [['Particulars', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
                ['Equity share capital', '177.20', '177.23', '177.37'],
                ['Reserves and surplus', '9,689.10', '10,623.46', '11,242.15'],
                ['Shareholders\u2019 funds', '9,866.30', '10,800.69',
                 '11,419.52'],
                ['Non-current borrowings', '535.97', '304.03', '15.96'],
                ['Current borrowings', '622.10', '426.09', '1,046.72'],
                ['Total borrowings (memorandum)', '1,158.07', '730.12',
                 '1,062.68'],
                ['Total current liabilities', '3,930.43', '4,318.44',
                 '5,239.08'],
                ['Total non-current assets', '9,443.06', '9,699.82', '8,593.95'],
                ['Total current assets', '5,679.62', '6,532.46', '8,885.96'],
                ['Total assets', '15,122.68', '16,232.28', '17,479.91'],
                ['Total equity and liabilities', '15,122.68', '16,232.28',
                 '17,479.91']])
    _fin_table(doc,
               'Table 5.25: Dabur India Ltd. \u2014 consolidated cash flow '
               'statement (Rs. crore)',
               [['Particulars', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
                ['Cash from operating activities', '2,013', '1,987', '2,579'],
                ['Cash from investing activities', '(971)', '(448)', '(1,279)'],
                ['Cash from financing activities', '(1,161)', '(1,405)',
                 '(1,236)'],
                ['Net cash flow', '(119)', '133', '64'],
                ['Free cash flow', '1,453', '1,448', '2,180'],
                ['Operating cash flow as a percentage of operating profit',
                 '104', '103', '122']])
    para(
        'The balance sheet shows the accumulation of financial investments '
        'rather than investment in the operating business. Non-current '
        'investments rose from Rs. 5,266 crore in FY2023-24 to about '
        'Rs. 4,352 crore in FY2025-26, while current investments rose from '
        'Rs. 1,667 crore to Rs. 4,595 crore, so that total investments of '
        'about Rs. 8,947 crore in FY2025-26 are a large proportion of the '
        'total balance sheet of Rs. 17,480 crore. Current assets rose from '
        'Rs. 5,680 crore to Rs. 8,886 crore over the three years, most of the '
        'increase being in investments rather than in inventory or '
        'receivables. This is the reason the company has the strongest current '
        'ratio of the three companies studied, and also the reason its return '
        'on assets is the lowest: a large part of the asset base is not '
        'employed in the business at all.')
    para(
        'Borrowings fell from Rs. 1,158 crore to Rs. 730 crore and then rose '
        'again to Rs. 1,063 crore, but the composition changed substantially. '
        'Long-term borrowings were almost repaid, falling from Rs. 536 crore '
        'to Rs. 16 crore, while short-term borrowings rose from Rs. 622 crore '
        'to Rs. 1,047 crore. The shift reduces the average cost of borrowing, '
        'which is consistent with the fall in interest expense from Rs. 164 '
        'crore to Rs. 145 crore in FY2025-26.')
    para(
        'The cash flow statement is the strongest part of the financial '
        'record. Operating cash flow rose 29.79 per cent to Rs. 2,579 crore in '
        'FY2025-26 and was 122 per cent of operating profit, which is the '
        'highest conversion of the three companies. Free cash flow rose to '
        'Rs. 2,180 crore. In other words, the weakness of the company lies in '
        'the growth of its business, not in the quality of its earnings.')

    doc.para('6.  Ratio analysis', bold=True, align='left', before=140)
    _fin_table(doc,
               'Table 5.26: Dabur India Ltd. \u2014 key financial ratios',
               [['Ratio', 'FY2023-24', 'FY2024-25', 'FY2025-26'],
                ['Net profit margin (%)', '14.60', '13.85', '14.17'],
                ['Operating profit margin (%)', '19.35', '18.43', '18.57'],
                ['Operating ratio (%)', '80.65', '81.56', '81.43'],
                ['Return on capital employed (%)', '22.52', '21.00', '20.55'],
                ['Return on equity (%)', '18.36', '16.11', '16.37'],
                ['Return on assets (%)', '11.98', '10.72', '10.69'],
                ['Return on investment (%)', '16.43', '15.09', '14.97'],
                ['Debt to equity (times)', '0.12', '0.07', '0.09'],
                ['Interest coverage (times)', '20.02', '14.77', '17.69'],
                ['Current ratio (times)', '1.45', '1.51', '1.70'],
                ['Earnings per share (Rs.)', '10.40', '9.97', '10.68'],
                ['Book value per share (Rs.)', '55.63', '60.89', '64.38']])
    para(
        'The ratio trend is the least favourable of the three companies. '
        'Return on capital employed fell in each of the three years, from '
        '22.52 to 20.55 per cent, return on equity fell from 18.36 to 16.37 '
        'per cent and return on assets fell from 11.98 to 10.69 per cent. The '
        'company earns a reasonable net profit margin of about 14 per cent and '
        'carries little debt, with a debt to equity ratio never exceeding 0.12 '
        'times, but the capital it retains is not producing a growing return. '
        'Shareholders\u2019 funds rose from Rs. 9,866 crore to Rs. 11,420 crore '
        'over the three years, and the financial investments on the balance '
        'sheet rose with them, while return on equity fell from 18.36 to 16.37 '
        'per cent and return on investment from 16.43 to 14.97 per cent. The '
        'company is therefore accumulating capital faster than it can deploy '
        'that capital profitably, which is the opposite of the position at '
        'Britannia Industries, where a much smaller equity base produces a '
        'much higher return.')

    doc.para('7.  Strengths, weaknesses, opportunities and threats', bold=True,
             align='left', before=140)
    doc.para('Table 5.27: Dabur India Ltd. \u2014 SWOT analysis', bold=True,
             align='left', before=120)
    doc.table([
        ['Strengths', 'Weaknesses'],
        ['\u2022  The leading position in Ayurvedic and natural healthcare, a '
         'category that is growing as consumer preference shifts towards '
         'natural products, and a portfolio reaching eight out of ten Indian '
         'households.\n'
         '\u2022  The deepest rural reach of the three companies studied, '
         'covering over 1,31,000 villages and 1.42 million outlets, with 45 to '
         '50 per cent of revenue derived from rural markets.\n'
         '\u2022  The highest cash conversion of the three companies: '
         'operating cash flow was 122 per cent of operating profit in '
         'FY2025-26.\n'
         '\u2022  Low leverage, with a debt to equity ratio below 0.12 times in '
         'each of the three years.',
         '\u2022  The slowest revenue growth of the three companies, at a '
         'compound rate of 3.13 per cent over the two years to FY2025-26.\n'
         '\u2022  Earnings per share growing at only 1.34 per cent a year, '
         'which is below the rate of inflation.\n'
         '\u2022  Falling return on capital employed, return on equity and '
         'return on assets in each of the three years.\n'
         '\u2022  A large part of reported profit comes from other income, and '
         'a large part of the asset base is held as financial investments '
         'rather than employed in the business.'],
        ['Opportunities', 'Threats'],
        ['\u2022  Growth of the natural and Ayurvedic categories, which the '
         'company is best placed to serve and which the larger personal care '
         'companies are also entering.\n'
         '\u2022  Expansion of the foods and beverages vertical, which grew '
         'faster than the rest of the portfolio in recent years.\n'
         '\u2022  E-commerce and quick commerce, where rural-weighted brands '
         'are under-represented and where the company\u2019s health positioning '
         'carries a premium.\n'
         '\u2022  International expansion in the Middle East, Africa and South '
         'Asia, where the brands are established and the categories are less '
         'penetrated.',
         '\u2022  Weak rural demand: the company has the largest rural '
         'exposure of the three companies studied, and rural volume growth '
         'fell to 3.6 per cent in 2025 against urban growth of 4.6 per cent.\n'
         '\u2022  Entry of larger competitors into the natural and herbal '
         'personal care categories, which the company has historically '
         'dominated.\n'
         '\u2022  Input cost inflation in herbs, edible oils and packaging '
         'materials.\n'
         '\u2022  Regulatory or labelling changes affecting the claims that '
         'may be made for Ayurvedic and health products.'],
    ], [5233, 5233], aligns=['l', 'l'])
    doc.after_table(0.5)

    doc.para('8.  Competitive position within the sector', bold=True,
             align='left', before=140)
    para(
        'Dabur competes with Hindustan Unilever, Colgate-Palmolive and Marico '
        'in personal care and with Emami and Zydus Wellness in health and '
        'wellness. Its competitive position rests on the authenticity of its '
        'Ayurvedic credentials and on the depth of its rural distribution, '
        'both of which are genuine advantages that a competitor cannot '
        'replicate quickly. Its difficulty is that these advantages have not '
        'translated into financial growth: the company earns a reasonable '
        'margin, carries almost no debt and converts profit into cash better '
        'than either of the other two companies, but the capital employed in '
        'the business has grown faster than the profit earned on it.')
