# -*- coding: utf-8 -*-
"""Chapter 7 - conclusion, findings and suggestions."""

from docgen import Doc


def chapter_7(doc, fig):
    doc.new_page()
    doc.para('CHAPTER 7 :- CONCLUSION, FINDINGS & SUGGESTIONS', bold=True,
             align='left')
    doc.mark('CHAPTER 7 :- CONCLUSION, FINDINGS & SUGGESTIONS', 1)
    para = lambda t, **kw: doc.para(t, align='both', **kw)

    doc.para('CONCLUSION :-', bold=True, align='left', before=100)
    para(
        'The study titled \u201cFundamental Analysis of Selected Companies in '
        'the FMCG Sector\u201d was undertaken to evaluate and compare the '
        'financial performance of Hindustan Unilever Ltd., Britannia '
        'Industries Ltd. and Dabur India Ltd. for FY2023-24, FY2024-25 and '
        'FY2025-26. The study used secondary data drawn from the audited '
        'consolidated financial statements of the three companies and applied '
        'ratio analysis covering profitability, liquidity, solvency, '
        'efficiency, return and market valuation, supported by an economic and '
        'industry analysis of the sector in which they operate.')
    para(
        'The analysis shows that the three companies followed different '
        'financial paths during the period. Hindustan Unilever recorded the '
        'most stable performance and the strongest financial position. Its net '
        'profit margin remained between 16.21 and 17.40 per cent, its '
        'operating ratio was the lowest of the three in every year at 76.03 to '
        '76.67 per cent, it carried no borrowings at all, and its interest '
        'coverage of 34.19 times in FY2025-26 was the highest of the three. It '
        'also scored the highest number of points in the factor analysis. What '
        'the figures do not show is growth: revenue rose at only 2.1 per cent '
        'a year over the two years and normalised earnings per share was '
        'almost unchanged at about Rs. 44, so the company\u2019s strength lies '
        'in the quality of the business it already has rather than in its '
        'expansion.')
    para(
        'Britannia Industries emerged as the strongest company on every '
        'measure of return and of capital efficiency. Its return on capital '
        'employed of 52.63 per cent and return on equity of 49.68 per cent in '
        'FY2025-26 were far above those of the other two companies, its return '
        'on assets improved in each of the three years to 26.07 per cent, its '
        'earnings per share grew at 8.81 per cent a year, and it reduced its '
        'debt to equity ratio from 0.52 to 0.27 times while increasing '
        'interest coverage from 18.76 to 30.11 times. It earns the lowest net '
        'profit margin of the three, at 13.25 per cent, and the reason is that '
        'it earns that margin on a small capital base: total assets of '
        'Rs. 9,731.94 crore support a profit after tax of Rs. 2,537 crore. A '
        'part of the FY2025-26 improvement came from a lower effective tax '
        'rate, and the sustainability of the growth rate therefore depends on '
        'the operating improvement continuing.')
    para(
        'Dabur India was the weakest of the three on the measures of return. '
        'Its return on capital employed fell in each year from 22.52 to 20.55 '
        'per cent, its return on equity fell from 18.36 to 16.37 per cent, its '
        'return on assets fell from 11.98 to 10.69 per cent and its earnings '
        'per share grew at 1.34 per cent a year. The company is not weak in '
        'other respects: it carries the least debt after Hindustan Unilever, '
        'it has the highest current ratio of the three at 1.70 times, and its '
        'operating cash flow was 122 per cent of operating profit in '
        'FY2025-26, the best conversion of the three. Its difficulty is that '
        'capital employed rose by about Rs. 1,458 crore over three years while '
        'profit after tax rose by only Rs. 58 crore, which means that the cash '
        'the business generates is being accumulated as financial investments '
        'rather than deployed in the business at a return that would justify '
        'the retention.')
    para(
        'On the factor analysis, in which thirteen ratios were scored for '
        'FY2025-26 with ten points for the best performer on each ratio, '
        'Hindustan Unilever scored 120 points out of a possible 130, Britannia '
        'Industries 117 and Dabur India 114. The margins are narrow, and a '
        'reader who attached greater weight to the return ratios than to '
        'margin, leverage and liquidity would place Britannia first, because '
        'it ranked first on six of the thirteen ratios against four for '
        'Hindustan Unilever. The conclusion of the study is therefore stated '
        'in two parts: Hindustan Unilever has the strongest all-round '
        'financial position on the ratio set used here, and Britannia '
        'Industries earns the highest return on the capital it employs, by a '
        'substantial margin.')
    para(
        'The operational part of the study reached a conclusion of a different '
        'kind. The dealing function, observed over the period of the '
        'internship, is predominantly procedural rather than discretionary. A '
        'dealer cannot form and act on a view of a security; the dealer '
        'receives an instruction, verifies that it can be accepted within the '
        'limits, the collateral and the regulatory restrictions applicable to '
        'the client, executes it, and reconciles the result. Most of the work '
        'consists of preparation, verification and control rather than of '
        'execution, and competence is demonstrated by the absence of error '
        'rather than by skill in trading. The study also noted a distinction '
        'that is easily missed from outside the market: the attributes that '
        'determine how a security should be traded, such as its price band, '
        'its depth, its volatility and the segment in which it may be traded, '
        'have almost nothing in common with the attributes that determine '
        'whether the company behind it is a sound business. The two halves of '
        'this report address exactly those two questions, and the internship '
        'is what made the difference between them visible.')

    doc.para('FINDINGS', bold=True, align='left', before=180)
    doc.para('Overall Financial Performance', bold=True, align='left',
             before=120)
    para(
        'The comparative analysis shows that Hindustan Unilever Ltd. had the '
        'strongest overall financial performance among the three selected '
        'companies on the ratio set used, with a total score of 120 out of 130 '
        'in the factor analysis, followed by Britannia Industries Ltd. with '
        '117 points and Dabur India Ltd. with 114 points. On the return ratios '
        'taken separately, Britannia Industries was the strongest by a '
        'substantial margin in each of the three years.')
    doc.para('Profitability Performance', bold=True, align='left', before=120)
    para(
        'Hindustan Unilever maintained the highest net profit margin in each '
        'of the three years, at 16.61 per cent in FY2023-24, 17.40 per cent in '
        'FY2024-25 and 16.21 per cent in FY2025-26 on normalised profit. Dabur '
        'India was second, at 14.60, 13.85 and 14.17 per cent, and Britannia '
        'Industries third, at 12.73, 12.14 and 13.25 per cent. Britannia was '
        'the only one of the three whose margin in FY2025-26 was higher than '
        'in FY2023-24. On the reported profit, Hindustan Unilever\u2019s margin '
        'for FY2025-26 was 23.36 per cent, and that figure is not comparable '
        'with the earlier years because it includes the one-time gain of '
        'Rs. 4,611 crore on the demerger of the ice cream undertaking.')
    doc.para('Return on Equity (ROE)', bold=True, align='left', before=120)
    para(
        'Britannia Industries recorded the highest return on equity in all '
        'three years, at 54.14, 50.00 and 49.68 per cent, although the ratio '
        'declined over the period as retained earnings accumulated in the '
        'equity base. Hindustan Unilever was second, at 20.07, 21.60 and 21.44 '
        'per cent, and Dabur India third, at 18.36, 16.11 and 16.37 per cent. '
        'Hindustan Unilever\u2019s improvement was caused by a reduction in '
        'shareholders\u2019 funds rather than by an increase in profit, and '
        'Dabur\u2019s decline was caused by an increase in shareholders\u2019 '
        'funds that was not matched by an increase in profit.')
    doc.para('Return on Capital Employed', bold=True, align='left', before=120)
    para(
        'Britannia Industries improved its return on capital employed from '
        '51.43 per cent in FY2023-24 to 54.94 per cent in FY2024-25 and then '
        'reported 52.63 per cent in FY2025-26. Hindustan Unilever moved from '
        '27.83 to 29.96 and then to 28.76 per cent, and Dabur India declined '
        'in every year, from 22.52 to 21.00 and then to 20.55 per cent. Dabur '
        'was the only company of the three in which this ratio fell in each of '
        'the three years, which is the clearest indication in the study of a '
        'company whose capital is growing faster than the profit it earns.')
    doc.para('Debt and Solvency', bold=True, align='left', before=120)
    para(
        'Hindustan Unilever was effectively debt free throughout the period, '
        'with borrowings of Rs. 13 crore or less against shareholders\u2019 '
        'funds of about Rs. 48,700 crore, and a debt to equity ratio of 0.00 '
        'times in all three years. Britannia Industries reduced its debt to '
        'equity ratio from 0.52 to 0.27 times by repaying borrowings, which '
        'fell from Rs. 2,041.21 crore to Rs. 1,357.83 crore, and Dabur India '
        'moved from 0.12 to 0.09 times. None of the three companies carries '
        'financial risk of a kind that would concern a lender, and in all '
        'three the greater part of the working capital is financed by trade '
        'credit rather than by borrowing.')
    doc.para('Operating Efficiency', bold=True, align='left', before=120)
    para(
        'Hindustan Unilever had the lowest operating ratio in every year, at '
        '76.32, 76.03 and 76.67 per cent, which means it spends the smallest '
        'proportion of each rupee of revenue on producing and selling its '
        'goods. Dabur India was second at 80.65, 81.56 and 81.43 per cent and '
        'Britannia Industries third at 81.12, 82.29 and 81.65 per cent. All '
        'three companies absorbed a rise in input costs in FY2024-25 and '
        'recovered part of it in FY2025-26, and the movement in each case was '
        'within about one and a half percentage points over three years.')
    doc.para('Interest Coverage', bold=True, align='left', before=120)
    para(
        'Hindustan Unilever had the highest interest coverage in every year, '
        'although it declined from 42.69 to 34.19 times as interest expense '
        'rose against a flat normalised profit. Britannia Industries improved '
        'in each year from 18.76 to 30.11 times, the largest improvement of '
        'the three and a direct result of its debt reduction. Dabur India was '
        'the weakest, at 20.02, 14.77 and 17.69 times, and it was the only '
        'company whose coverage fell below its opening level.')
    doc.para('Liquidity Position', bold=True, align='left', before=120)
    para(
        'Dabur India had the highest current ratio in the final two years, at '
        '1.51 and 1.70 times, having moved from 1.45 times in FY2023-24, and '
        'the improvement was caused mainly by an increase in current '
        'investments rather than in operating assets. Hindustan Unilever\u2019s '
        'ratio declined in each year from 1.66 to 1.22 times and Britannia '
        'Industries had the lowest ratio of the three, at 1.19, 1.08 and 1.12 '
        'times. None of the three fell below one, and none faces a short-term '
        'liquidity problem on the evidence of the three years studied.')
    doc.para('Market Valuation', bold=True, align='left', before=120)
    para(
        'On the market price as at 12 October 2026, Dabur India was the '
        'cheapest of the three companies on both the price to earnings ratio, '
        'at 35.96 times, and the price to book ratio, at 5.97 times. '
        'Hindustan Unilever was valued at 41.68 times normalised earnings and '
        '8.92 times book value, and Britannia Industries at 45.71 times '
        'earnings and 22.68 times book value. The valuation ratios and the '
        'growth rates move in the same direction: the company valued the '
        'lowest has the slowest earnings growth at 1.34 per cent a year, and '
        'the company valued the highest has the fastest at 8.81 per cent. On '
        'the price to earnings growth ratio Britannia was the only one of the '
        'three whose multiple was supported by its growth rate, at 5.19 times, '
        'against 26.90 times for Dabur and 54.62 times for Hindustan Unilever; '
        'the two larger figures are largely an artefact of dividing by a '
        'growth rate close to zero and should not be read as measurements of '
        'value.')
    doc.para('Overall Finding', bold=True, align='left', before=120)
    para(
        'Based on the selected ratios, Hindustan Unilever appears to be the '
        'strongest company overall, Britannia Industries earns the highest '
        'return on the capital employed in its business, and Dabur India has '
        'the strongest short-term liquidity and the lowest market valuation '
        'but the weakest growth and the weakest returns. Investment decisions '
        'should not be based on any single ratio or on this analysis alone. '
        'The reasons lie partly in the nature of the study, which covers three '
        'years and three companies and uses no forward-looking estimate, and '
        'partly in the nature of valuation itself, which depends on the '
        'earnings that will be produced in the future rather than on those '
        'that have been produced in the past.')
    fig('fig7_1', 6.2, 3.0, before=160, after=70)
    doc.para('Figure 7.1: Composite factor analysis score of the three '
             'companies (out of 130)', bold=True, align='center', size=11.0)

    doc.para('SUGGESTIONS', bold=True, align='left', before=180)
    doc.para('1.  Suggestions for Hindustan Unilever Ltd.', bold=True,
             align='left', before=120)
    for b in [
        'The company should address the absence of revenue growth, which at '
        '2.1 per cent a year over the two years to FY2025-26 is below the rate '
        'of inflation. Growth in a company of this size will have to come from '
        'premiumisation and from categories outside the mature ones in which '
        'it already holds a large share.',
        'The decline in operating cash flow from Rs. 15,469 crore in '
        'FY2023-24 to Rs. 10,999 crore in FY2025-26, in a period in which '
        'operating profit rose slightly, should be examined. The change is '
        'explained by working capital rather than by profitability, and the '
        'company should consider whether the movement reflects a deliberate '
        'change in payment terms or a deterioration in collection.',
        'The reduction in reserves in two successive years indicates that '
        'distributions are being made in excess of profits. This is '
        'sustainable for a debt-free company with strong cash generation, but '
        'it leaves no reserve for an acquisition or for a period of '
        'unexpectedly weak trading, and the company may wish to retain a '
        'larger part of its earnings while it invests in the premium segments.',
        'The current ratio has fallen from 1.66 to 1.22 times over three '
        'years. The absence of debt means that this is not a risk of default, '
        'but the trend in working capital should be monitored.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)
    doc.para('2.  Suggestions for Britannia Industries Ltd.', bold=True,
             align='left', before=120)
    for b in [
        'The company should continue to reduce dependence on a single product '
        'category. Biscuits account for the greater part of revenue, and the '
        'concentration exposes the entire business to the prices of wheat '
        'flour, sugar and edible oil in a way that a more diversified '
        'portfolio would not.',
        'The improvement in operating profit in FY2025-26 should be '
        'consolidated. Since part of the increase in profit after tax in that '
        'year came from a lower effective tax rate, the company should '
        'demonstrate that the operating improvement can be repeated in a year '
        'in which the tax charge normalises.',
        'The current ratio, which has stayed between 1.08 and 1.19 times, '
        'should be reviewed against the company\u2019s own liquidity policy. '
        'A negative cash conversion cycle is a source of financial strength, '
        'but it also means that the company depends on continuing trade credit '
        'and on distributors continuing to pay in advance.',
        'Investment in the dairy and adjacent bakery businesses should '
        'continue, because those businesses use the existing distribution '
        'network and raise the value of each delivery without requiring a new '
        'one.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)
    doc.para('3.  Suggestions for Dabur India Ltd.', bold=True, align='left',
             before=120)
    for b in [
        'The company should identify why the return on the capital it employs '
        'is falling, and act on it. The ratio has declined in each of the '
        'three years because capital employed has grown faster than profit, '
        'and no amount of improvement in liquidity or in cash conversion will '
        'correct that if the capital continues to accumulate without being '
        'deployed.',
        'The balances held in financial investments, which were about '
        'Rs. 8,947 crore at the end of FY2025-26, should either be deployed in '
        'the business or returned to shareholders. Held as investments they '
        'earn a return below the company\u2019s cost of capital and they '
        'reduce the return on assets and the return on investment reported to '
        'shareholders.',
        'The company should reduce its dependence on other income, which '
        'contributed Rs. 584 crore of a profit before tax of Rs. 2,420 crore '
        'in FY2025-26. Income of this kind is volatile and is outside the '
        'control of the management of the operating business.',
        'The rural weighting of the portfolio, at 45 to 50 per cent of '
        'revenue, makes the company more exposed than its competitors to the '
        'slowdown in rural demand. The company should continue to invest in '
        'the foods and beverages vertical, which grew faster than the rest of '
        'the portfolio and is less dependent on rural purchasing power.',
        'The decline in interest coverage to 14.77 times in FY2024-25, though '
        'comfortable in absolute terms, should be monitored, because it '
        'coincided with a fall in profit rather than with a rise in '
        'borrowings.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)
    doc.para('4.  Suggestions for Investors', bold=True, align='left',
             before=120)
    for b in [
        'Investors should not base a decision on a single ratio. In this study '
        'the company with the highest net profit margin is not the company '
        'with the highest return on capital, and the company with the lowest '
        'price to earnings multiple is not the company with the best growth.',
        'Profitability, liquidity, solvency, efficiency and valuation ratios '
        'should be read together, and the direction of each ratio over time '
        'matters more than its level in one year.',
        'Reported figures should be checked for one-time items before any '
        'comparison is made. The earnings of Hindustan Unilever for FY2025-26 '
        'are 44 per cent higher than the preceding year on a reported basis '
        'and almost unchanged on a normalised basis, and an investor who used '
        'the reported figure would have formed the wrong impression of the '
        'company.',
        'A low price to earnings multiple or a high current ratio may reflect '
        'weakness rather than value. In this study the cheapest company on '
        'both valuation measures also has the lowest return on equity and the '
        'slowest growth in earnings per share.',
        'Investors should also consider the movement of agricultural commodity '
        'prices, the state of rural demand, changes in indirect tax rates, '
        'competition from digital-first brands and the shift of volume towards '
        'quick commerce, all of which affect the sector as a whole and cannot '
        'be seen from the financial statements of a single company.',
        'Historical ratios should be combined with an independent view of the '
        'company\u2019s future prospects, and with due attention to the '
        'valuation at which the shares are available, before any investment '
        'decision is taken.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)
    doc.para('5.  Suggestions Arising from the Internship', bold=True,
             align='left', before=120)
    for b in [
        'A written pre-market checklist should be maintained on the dealing '
        'desk. Most of the operational difficulties observed during the '
        'internship arose from an omission in the preparation made before the '
        'market opened rather than from an error during trading, and a signed '
        'checklist covering corporate actions, the ban list for derivative '
        'contracts, surveillance changes and limit confirmation would remove '
        'the largest single source of avoidable problems.',
        'A structured period of practice on a simulated order book should '
        'precede live access for a new dealer. Competence at the terminal is '
        'partly a motor skill acquired through repetition, and supervised '
        'practice shortens the period during which a new entrant is a risk to '
        'the desk and to the client.',
        'Clients should be given a pre-trade cost illustration. A delivery '
        'purchase and sale at the same price still produces a loss once '
        'brokerage, statutory charges and taxes are applied, and a one-page '
        'illustration issued before the trade would prevent the disputes that '
        'arise when a client sees the net figure on the contract note for the '
        'first time.',
        'A plain-language note on the asymmetry of margin and collateral '
        'should be issued to derivative clients. Collateral pledged against a '
        'position loses value at the same time as the margin requirement '
        'rises, so a shortfall can appear after a price movement much smaller '
        'than the client expects, and this is the root of most disputes about '
        'margin calls.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)
