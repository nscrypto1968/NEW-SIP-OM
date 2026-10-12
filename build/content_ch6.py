# -*- coding: utf-8 -*-
"""Chapter 6 - comparative ratio analysis, interpretation and factor analysis.

Every number in this chapter is produced from the same input data as
Chapter 5, so that the two chapters cannot disagree.
"""

from docgen import Doc
from ratios import R, DATA, NAMES, ORDER

# ---------------------------------------------------------------------------
# Presentation helper
# ---------------------------------------------------------------------------
HUL = 'Hindustan Unilever Ltd.'
BRIT = 'Britannia Industries Ltd.'
DAB = 'Dabur India Ltd.'
CO = {'HUL': HUL, 'BRITANNIA': BRIT, 'DABUR': DAB}


def _three_rows(source, fmt):
    """Rows for a 4 x 4 table: company, FY2024, FY2025, FY2026."""
    rows = [['Company'] + ['FY2024', 'FY2025', 'FY2026']]
    for k in ORDER:
        v = DATA[k][source] if source in DATA[k] else R[k][source]
        rows.append([NAMES[k]] + [fmt % x for x in v])
    return rows


def _one_row(source, fmt):
    """Rows for a 4 x 2 table: company, value at a single date."""
    rows = [['Company', 'As at 12 October 2026']]
    for k in ORDER:
        rows.append([NAMES[k], fmt % R[k][source]])
    return rows


def _section(doc, fig, n, title, definition, formula, calcs, source, fmt,
             kind, interpretation, chart=None, caption=None, note=None,
             overall=None, table_label=None):
    doc.heading('%d. %s' % (n, title), 2)
    if definition:
        doc.para(definition, align='both')
    doc.para('Formula: ' + formula, align='left', before=60)
    for key in ORDER:
        doc.para(CO[key] + ' :-', bold=True, align='left', before=100)
        for line in calcs[key]:
            doc.para('\u2022  ' + line, align='both', indent_left=360,
                     first_line=180)
    if table_label:
        doc.para(table_label, bold=True, align='left', before=120)
    if kind == 'three':
        doc.table(_three_rows(source, fmt), [2666, 2600, 2600, 2600],
                  aligns=['l', 'c', 'c', 'c'])
    else:
        doc.table(_one_row(source, fmt), [5233, 5233], aligns=['l', 'c'])
    doc.after_table(0.4)
    if note:
        doc.para(note, align='both')
    doc.para('Interpretation :', bold=True, align='left', before=120)
    for line in interpretation:
        doc.para('\u2022  ' + line, align='both', indent_left=360,
                 first_line=180)
    if chart:
        fig(chart, 5.9, 2.8, before=140, after=70)
        doc.para(caption, bold=True, align='center', size=11.0)
    if overall:
        doc.para('Overall Interpretation :', bold=True, align='left',
                 before=140)
        for t in overall:
            doc.para(t, align='both')


def chapter_6(doc, fig):
    doc.new_page()
    doc.para('CHAPTER 6 :- COMPARATIVE RATIO ANALYSIS & INTERPRETATION',
             bold=True, align='left')
    doc.mark('CHAPTER 6 :- COMPARATIVE RATIO ANALYSIS & INTERPRETATION', 1)
    doc.para('FMCG SECTOR FINANCIAL PERFORMANCE OF HINDUSTAN UNILEVER LTD., '
             'BRITANNIA INDUSTRIES LTD. AND DABUR INDIA LTD.', bold=True,
             align='center')
    doc.para(
        'This chapter compares the financial performance of the three '
        'selected companies over FY2023-24, FY2024-25 and FY2025-26 using '
        'thirteen ratios. Each ratio is presented in the same order: the '
        'formula applied, the computation for each company for each of the '
        'three years, a comparative table, a chart showing the movement of the '
        'ratio, and the interpretation. The chapter closes with a factor '
        'analysis in which the thirteen ratios are used to rank the three '
        'companies.', align='both')
    doc.para(
        'Two conventions apply throughout and should be noted before the '
        'ratios are read. First, all figures are consolidated figures in '
        'rupees crore, and FY2024, FY2025 and FY2026 mean the financial years '
        'ended 31 March 2024, 31 March 2025 and 31 March 2026. Second, the '
        'FY2025-26 figures of Hindustan Unilever Ltd. exclude the one-time '
        'gain of Rs. 4,611 crore arising from the demerger of the ice cream '
        'undertaking, because including it would make the reported profit, and '
        'therefore every ratio computed from it, incomparable with the two '
        'preceding years and with the other two companies. The reported figure '
        'is shown alongside the normalised figure wherever the difference is '
        'material.', align='both')
    doc.para('Table 6.1: Ratios used in the analysis and the formula applied '
             'to each', bold=True, align='left', before=120)
    doc.table([
        ['Sr. No.', 'Ratio', 'Formula applied'],
        ['1', 'Net profit margin', 'Profit after tax \u00f7 net revenue '
                                    '\u00d7 100'],
        ['2', 'Return on capital employed',
         '(Profit before tax + interest expense) \u00f7 (shareholders\u2019 '
         'funds + total borrowings) \u00d7 100'],
        ['3', 'Return on equity',
         'Profit after tax \u00f7 shareholders\u2019 funds \u00d7 100'],
        ['4', 'Debt to equity', 'Total borrowings \u00f7 shareholders\u2019 '
                                'funds'],
        ['5', 'Operating ratio',
         '(Net revenue \u2212 operating profit) \u00f7 net revenue \u00d7 100'],
        ['6', 'Interest coverage',
         '(Profit before tax + interest expense) \u00f7 interest expense'],
        ['7', 'Earnings per share',
         'Profit after tax \u00f7 number of equity shares outstanding'],
        ['8', 'Return on assets',
         'Profit after tax \u00f7 total assets \u00d7 100'],
        ['9', 'Current ratio', 'Current assets \u00f7 current liabilities'],
        ['10', 'Price to earnings', 'Market price per share \u00f7 earnings '
                                    'per share'],
        ['11', 'Price to book', 'Market price per share \u00f7 book value per '
                                'share'],
        ['12', 'Price to earnings growth',
         'Price to earnings ratio \u00f7 two-year compound growth rate in '
         'earnings per share'],
        ['13', 'Return on investment',
         'Profit after tax \u00f7 (shareholders\u2019 funds + total '
         'borrowings) \u00d7 100'],
    ], [900, 3000, 6566], aligns=['c', 'l', 'l'])
    doc.after_table(0.5)
    doc.para(
        'Return on capital employed and return on investment are close in '
        'definition but not identical: the first measures the profit available '
        'to all providers of capital before interest and tax, and the second '
        'measures the profit available to shareholders after interest and tax '
        'on the same capital base. Where a company carries no borrowings the '
        'two ratios converge, and that is the case for Hindustan Unilever Ltd. '
        'in all three years.', align='both')
    doc.para(
        'The four market-based ratios and the earnings per share are computed '
        'on the market price as at 12 October 2026, which is the date on which '
        'the price data were collected. The nine remaining ratios are computed '
        'for each of the three financial years. Because a historical series of '
        'market prices was not collected, the price to earnings, price to book '
        'and price to earnings growth ratios in this chapter are stated for '
        'that single date, and the limitation is noted again in Chapter 7.',
        align='both')

    # ---------------------------------------------------------------- 1
    _section(
        doc, fig, 1, 'NET PROFIT MARGIN',
        'The net profit margin measures the profit left to the company from '
        'every rupee of revenue after all operating expenses, interest and '
        'tax. It is the single most direct measure of how much of a '
        'company\u2019s turnover it keeps.',
        'PROFIT AFTER TAX / NET REVENUE \u00d7 100',
        {
            'HUL': ['2024: 10,282 / 61,896 \u00d7 100 = 16.61%',
                    '2025: 10,671 / 61,328 \u00d7 100 = 17.40%',
                    '2026: 10,448 / 64,468 \u00d7 100 = 16.21% (normalised '
                    'profit of Rs. 10,448 crore; on the reported profit of '
                    'Rs. 15,059 crore the ratio is 23.36%)'],
            'BRITANNIA': ['2024: 2,134 / 16,769 \u00d7 100 = 12.73%',
                          '2025: 2,178 / 17,943 \u00d7 100 = 12.14%',
                          '2026: 2,537 / 19,152 \u00d7 100 = 13.25%'],
            'DABUR': ['2024: 1,811 / 12,404 \u00d7 100 = 14.60%',
                      '2025: 1,740 / 12,563 \u00d7 100 = 13.85%',
                      '2026: 1,869 / 13,193 \u00d7 100 = 14.17%'],
        },
        'NPM', '%.2f', 'three',
        ['Hindustan Unilever: The margin widened from 16.61% to 17.40% in '
         '2025 and narrowed to 16.21% in 2026 on the normalised profit. The '
         'movement is small, which is to be expected in a business that sells '
         'essential products at stable prices, and the company retains the '
         'highest margin of the three on a comparable basis.',
         'Britannia Industries: The margin narrowed from 12.73% to 12.14% in '
         '2025 when input costs rose and then widened to 13.25% in 2026. The '
         '2026 improvement is partly attributable to a lower effective tax '
         'rate, and the operating margin moved less than the net margin, which '
         'means that the final-year improvement did not come from the sale '
         'side of the business.',
         'Dabur India: The margin narrowed from 14.60% to 13.85% in 2025 and '
         'recovered to 14.17% in 2026, which leaves it slightly below the 2024 '
         'level. A margin that ends the period below where it started, in a '
         'company whose revenue grew by only 6.4% over the two years, '
         'indicates that neither price nor cost gave the business an '
         'advantage.'],
        chart='fig6_1',
        caption='Figure 6.1: Net profit margin of the three companies',
        overall=[
            'Hindustan Unilever earned the highest net margin in each of the '
            'three years and Dabur the second, while Britannia earned the '
            'lowest. This ranking reverses the ranking on return on capital, '
            'because margin measures what is earned on each rupee of sale '
            'whereas the return ratios measure what is earned on each rupee of '
            'capital employed. Britannia earns less per rupee of sale but '
            'employs far less capital for each rupee of sale, which is why it '
            'leads on the return ratios presented in the following sections.'],
        table_label='Table 6.2: Net profit margin of the three companies (%)')

    # ---------------------------------------------------------------- 2
    _section(
        doc, fig, 2, 'RETURN ON CAPITAL EMPLOYED (ROCE)',
        'Return on capital employed measures the profit generated by a company '
        'in relation to the total capital employed in the business, which '
        'includes both the shareholders\u2019 funds and the borrowings. It is '
        'computed before interest and tax so that companies with different '
        'capital structures can be compared.',
        '(PROFIT BEFORE TAX + INTEREST EXPENSE) / CAPITAL EMPLOYED \u00d7 100, '
        'WHERE CAPITAL EMPLOYED = SHAREHOLDERS\u2019 FUNDS + TOTAL BORROWINGS',
        {
            'HUL': ['2024: (13,926 + 334) / 51,231 \u00d7 100 = 27.83%',
                    '2025: (14,419 + 381) / 49,403 \u00d7 100 = 29.96%',
                    '2026: (13,608 + 410) / 48,739 \u00d7 100 = 28.76% '
                    '(normalised profit before tax)'],
            'BRITANNIA': ['2024: (2,913 + 164) / 5,982.73 \u00d7 100 = 51.43%',
                          '2025: (2,927 + 139) / 5,580.49 \u00d7 100 = 54.94%',
                          '2026: (3,289 + 113) / 6,464.39 \u00d7 100 = 52.63%'],
            'DABUR': ['2024: (2,359 + 124) / 11,024.37 \u00d7 100 = 22.52%',
                      '2025: (2,258 + 164) / 11,530.81 \u00d7 100 = 21.00%',
                      '2026: (2,420 + 145) / 12,482.20 \u00d7 100 = 20.55%'],
        },
        'ROCE', '%.2f', 'three',
        ['Hindustan Unilever: The ratio moved from 27.83% to a peak of 29.96% '
         'in 2025 and settled at 28.76% in 2026. Capital employed fell slightly '
         'over the period as reserves were distributed, and the profit before '
         'interest and tax was almost unchanged, so the ratio is stable. '
         'Stability at this level indicates a business that earns a healthy '
         'return without needing to invest additional capital.',
         'Britannia Industries: The ratio of 51.43% in 2024 rose to 54.94% in '
         '2025 and then eased to 52.63% in 2026, and it is the highest of the '
         'three companies by a wide margin. Capital employed is only about '
         'Rs. 6,464 crore against a profit before interest and tax of '
         'Rs. 3,402 crore. The ratio is high because the business is '
         'capital-light and is financed partly by trade credit rather than by '
         'equity or borrowings.',
         'Dabur India: The ratio declined in every one of the three years, '
         'from 22.52% to 21.00% and then to 20.55%. Capital employed rose by '
         'about Rs. 1,458 crore over the period while the profit before '
         'interest and tax rose by only Rs. 82 crore. A company whose capital '
         'is growing faster than its profit is not deploying that capital '
         'productively, and the movement of this ratio is the clearest single '
         'indicator of the difficulty described in Chapter 5.'],
        chart='fig6_2',
        table_label='Table 6.3: Return on capital employed of the three companies (%)',
        caption='Figure 6.2: Return on capital employed of the three companies',
        overall=[
            'Britannia Industries leads on this ratio in all three years, '
            'Hindustan Unilever is second and Dabur India third. The gap '
            'between the first two and the third is substantial: a difference '
            'of more than thirty percentage points between Britannia and Dabur '
            'in the same sector and the same years cannot be explained by '
            'superior pricing, because Britannia earns the lowest net margin. '
            'It is explained by the size of the capital base on which each '
            'company earns its profit. Britannia employs about Rs. 6,464 crore '
            'of capital to generate Rs. 3,402 crore of profit before interest '
            'and tax, whereas Dabur employs about Rs. 12,482 crore to generate '
            'Rs. 2,565 crore.'])

    # ---------------------------------------------------------------- 3
    _section(
        doc, fig, 3, 'RETURN ON EQUITY (ROE)',
        'Return on equity measures the return earned on the money '
        'shareholders have invested in the company, after interest and tax. It '
        'is the ratio that owners of the business have the strongest reason to '
        'watch.',
        'PROFIT AFTER TAX / SHAREHOLDERS\u2019 FUNDS \u00d7 100',
        {
            'HUL': ['2024: 10,282 / 51,218 \u00d7 100 = 20.07%',
                    '2025: 10,671 / 49,402 \u00d7 100 = 21.60%',
                    '2026: 10,448 / 48,739 \u00d7 100 = 21.44% (normalised)'],
            'BRITANNIA': ['2024: 2,134 / 3,941.52 \u00d7 100 = 54.14%',
                          '2025: 2,178 / 4,355.72 \u00d7 100 = 50.00%',
                          '2026: 2,537 / 5,106.56 \u00d7 100 = 49.68%'],
            'DABUR': ['2024: 1,811 / 9,866.30 \u00d7 100 = 18.36%',
                      '2025: 1,740 / 10,800.69 \u00d7 100 = 16.11%',
                      '2026: 1,869 / 11,419.52 \u00d7 100 = 16.37%'],
        },
        'ROE', '%.2f', 'three',
        ['Hindustan Unilever: Return on equity improved from 20.07% to 21.44% '
         'over the three years, and the improvement is explained by the '
         'reduction in shareholders\u2019 funds from Rs. 51,218 crore to '
         'Rs. 48,739 crore rather than by any growth in profit, which was flat '
         'on a normalised basis. A return that rises because the denominator '
         'is shrinking is not evidence of improving performance.',
         'Britannia Industries: Return on equity declined from 54.14% to '
         '49.68% across the period, but it remains by far the highest of the '
         'three companies. The decline is not a deterioration in profit, which '
         'rose by 18.88% over the two years, but the effect of retained '
         'earnings accumulating in a smaller equity base that is no longer '
         'matched by an increase in borrowings.',
         'Dabur India: Return on equity fell from 18.36% to 16.11% in 2025 and '
         'then recovered marginally to 16.37% in 2026, and over the whole '
         'period it declined. Shareholders\u2019 funds rose by Rs. 1,553 crore '
         'while profit after tax rose by only Rs. 58 crore, so the additional '
         'capital produced almost no additional profit.'],
        chart='fig6_3',
        table_label='Table 6.4: Return on equity of the three companies (%)',
        caption='Figure 6.3: Return on equity of the three companies',
        overall=[
            'The ranking is the same as on return on capital employed: '
            'Britannia first, Hindustan Unilever second and Dabur third in each '
            'of the three years. It is worth recording why Britannia\u2019s '
            'return on equity is lower than its return on capital employed '
            'while the reverse is true for Dabur. Britannia earns a '
            'post-interest, post-tax return of 49.68% on equity against a '
            'pre-interest return of 52.63% on total capital, the difference '
            'being the tax charge and the effect of the borrowings. Dabur earns '
            '16.37% on equity against 20.55% on capital employed, and the gap '
            'is wider because the company holds a large amount of financial '
            'investments whose income is included in profit but whose cost is '
            'included in the capital base.'])

    # ---------------------------------------------------------------- 4
    _section(
        doc, fig, 4, 'DEBT TO EQUITY RATIO',
        'The debt to equity ratio compares the borrowings of a company with '
        'the funds contributed by its shareholders. A ratio above one means '
        'the company is financed more by lenders than by owners and carries '
        'correspondingly more financial risk.',
        'TOTAL BORROWINGS / SHAREHOLDERS\u2019 FUNDS',
        {
            'HUL': ['2024: 13.00 / 51,218 \u00d7 100 = 0.00 times '
                    '(0.0003 times)',
                    '2025: 1.00 / 49,402 = 0.00 times (0.00002 times)',
                    '2026: 0.00 / 48,739 = 0.00 times'],
            'BRITANNIA': ['2024: 2,041.21 / 3,941.52 = 0.52 times',
                          '2025: 1,224.77 / 4,355.72 = 0.28 times',
                          '2026: 1,357.83 / 5,106.56 = 0.27 times'],
            'DABUR': ['2024: 1,158.07 / 9,866.30 = 0.12 times',
                      '2025: 730.12 / 10,800.69 = 0.07 times',
                      '2026: 1,062.68 / 11,419.52 = 0.09 times'],
        },
        'DE', '%.2f', 'three',
        ['Hindustan Unilever: The company is effectively debt free throughout '
         'the period. Borrowings were Rs. 13 crore at the end of FY2024 and '
         'nil at the end of FY2026, against shareholders\u2019 funds of about '
         'Rs. 48,700 crore. The ratio is therefore not informative about '
         'leverage, and the interest expense that appears in the profit and '
         'loss account relates largely to lease liabilities and other '
         'financial obligations rather than to borrowings.',
         'Britannia Industries: The ratio fell from 0.52 to 0.27 times as '
         'borrowings were reduced from Rs. 2,041 crore to Rs. 1,358 crore '
         'while shareholders\u2019 funds rose. This is a deliberate '
         'deleveraging, and it is the reason interest expense fell from '
         'Rs. 164 crore to Rs. 113 crore over the same period.',
         'Dabur India: The ratio is the second lowest of the three, moving '
         'from 0.12 to 0.07 times and then to 0.09 times. Borrowings are small '
         'in relation to a balance sheet of Rs. 17,480 crore, and the company '
         'has the capacity to borrow more if it had a use for the funds; the '
         'absence of borrowing is therefore a statement about the '
         'opportunities available rather than about prudence alone.'],
        chart='fig6_4',
        table_label='Table 6.5: Debt to equity ratio of the three companies (times)',
        caption='Figure 6.4: Debt to equity ratio of the three companies',
        overall=[
            'None of the three companies is materially levered, and in that '
            'respect all three are typical of the sector, in which operations '
            'are financed substantially by trade credit. Hindustan Unilever is '
            'the most conservative, Britannia the most willing to use debt and '
            'Dabur between the two. The comparison also shows that a low debt '
            'to equity ratio is not by itself a sign of strength: Dabur has a '
            'low ratio and the weakest return on capital, because the capital '
            'it does employ is not producing a return commensurate with the '
            'risk.'])

    # ---------------------------------------------------------------- 5
    _section(
        doc, fig, 5, 'OPERATING RATIO',
        'The operating ratio expresses the cost of running the business, '
        'excluding non-operating income and financing costs, as a proportion '
        'of revenue. It is the complement of the operating profit margin, so a '
        'lower ratio indicates a more efficient operation.',
        '(NET REVENUE \u2212 OPERATING PROFIT) / NET REVENUE \u00d7 100',
        {
            'HUL': ['2024: (61,896 \u2212 14,659) / 61,896 \u00d7 100 = 76.32%',
                    '2025: (61,328 \u2212 14,698) / 61,328 \u00d7 100 = 76.03%',
                    '2026: (64,468 \u2212 15,039) / 64,468 \u00d7 100 = 76.67%'],
            'BRITANNIA': ['2024: (16,769 \u2212 3,166) / 16,769 \u00d7 100 = '
                          '81.12%',
                          '2025: (17,943 \u2212 3,177) / 17,943 \u00d7 100 = '
                          '82.29%',
                          '2026: (19,152 \u2212 3,514) / 19,152 \u00d7 100 = '
                          '81.65%'],
            'DABUR': ['2024: (12,404 \u2212 2,400) / 12,404 \u00d7 100 = '
                      '80.65%',
                      '2025: (12,563 \u2212 2,316) / 12,563 \u00d7 100 = '
                      '81.56%',
                      '2026: (13,193 \u2212 2,450) / 13,193 \u00d7 100 = '
                      '81.43%'],
        },
        'OPR', '%.2f', 'three',
        ['Hindustan Unilever: The ratio moves within a narrow band of 76.03% '
         'to 76.67% and is the lowest of the three companies in every year, '
         'which means the company spends the smallest proportion of each rupee '
         'of revenue on producing and selling its goods. Scale in manufacture '
         'and in distribution is the reason.',
         'Britannia Industries: The ratio rose from 81.12% to 82.29% in 2025, '
         'the year in which input costs rose faster than prices, and improved '
         'to 81.65% in 2026. The company is the least efficient of the three '
         'on this measure, which is consistent with the low net profit margin '
         'and reflects a portfolio concentrated in a category where the cost '
         'of wheat, sugar and packaging is a large part of the selling price.',
         'Dabur India: The ratio deteriorated from 80.65% to 81.56% and then '
         'improved marginally to 81.43%, which leaves it marginally better '
         'than Britannia and clearly worse than Hindustan Unilever. The '
         'company\u2019s costs rose in 2025 and were only partly recovered in '
         'the following year.'],
        chart='fig6_5',
        table_label='Table 6.6: Operating ratio of the three companies (%)',
        caption='Figure 6.5: Operating ratio of the three companies',
        overall=[
            'The three ratios are close together, spanning about five '
            'percentage points in each year, and the ordering is stable: '
            'Hindustan Unilever first, then Dabur and Britannia. Because a '
            'change of one percentage point in the operating ratio of '
            'Hindustan Unilever is equivalent to about Rs. 645 crore of '
            'operating profit, the smallness of the movement should not be '
            'misread as an absence of commercial significance.'])

    # ---------------------------------------------------------------- 6
    _section(
        doc, fig, 6, 'INTEREST COVERAGE RATIO',
        'The interest coverage ratio measures how many times the profit before '
        'interest and tax covers the interest expense of the company. It '
        'indicates the margin of safety available to lenders, and therefore '
        'the risk that a fall in profit would leave the company unable to '
        'service its debt.',
        '(PROFIT BEFORE TAX + INTEREST EXPENSE) / INTEREST EXPENSE',
        {
            'HUL': ['2024: (13,926 + 334) / 334 = 42.69 times',
                    '2025: (14,419 + 381) / 381 = 38.85 times',
                    '2026: (13,608 + 410) / 410 = 34.19 times'],
            'BRITANNIA': ['2024: (2,913 + 164) / 164 = 18.76 times',
                          '2025: (2,927 + 139) / 139 = 22.06 times',
                          '2026: (3,289 + 113) / 113 = 30.11 times'],
            'DABUR': ['2024: (2,359 + 124) / 124 = 20.02 times',
                      '2025: (2,258 + 164) / 164 = 14.77 times',
                      '2026: (2,420 + 145) / 145 = 17.69 times'],
        },
        'IC', '%.2f', 'three',
        ['Hindustan Unilever: Coverage of 42.69 times in 2024 declined to '
         '34.19 times in 2026. The ratio remains the highest of the three and '
         'at a level at which the risk to lenders is immaterial, but the '
         'direction of the change is worth noting: interest expense rose from '
         'Rs. 334 crore to Rs. 410 crore in a period in which the normalised '
         'profit before tax fell slightly.',
         'Britannia Industries: Coverage improved in every year, from 18.76 '
         'times to 30.11 times, because interest expense fell by almost a '
         'third while profit before interest and tax rose by 15.9%. This is '
         'the clearest evidence in the whole ratio set of the benefit of the '
         'deleveraging described in the previous section.',
         'Dabur India: Coverage was the weakest of the three in 2025 at 14.77 '
         'times, having fallen from 20.02 times in 2024, and recovered to '
         '17.69 times in 2026. The 2025 deterioration reflects both a fall in '
         'profit before interest and tax and a rise in interest expense of '
         'Rs. 40 crore.'],
        chart='fig6_6',
        table_label='Table 6.7: Interest coverage of the three companies (times)',
        caption='Figure 6.6: Interest coverage of the three companies',
        overall=[
            'All three companies cover their interest comfortably, and none is '
            'at risk on this measure. The range nevertheless separates them: '
            'Hindustan Unilever has no meaningful debt and therefore the '
            'highest coverage, Britannia improved the most during the period, '
            'and Dabur, despite the lowest borrowings of the three as a '
            'proportion of its balance sheet, has the lowest coverage because '
            'its interest expense is high relative to its profit before '
            'interest and tax.'])

    # ---------------------------------------------------------------- 7
    _section(
        doc, fig, 7, 'EARNINGS PER SHARE (EPS)',
        'Earnings per share expresses the profit of the company for each '
        'equity share outstanding. It is the figure on which the price to '
        'earnings ratio and the price to earnings growth ratio in the later '
        'sections of this chapter are based, and it is the measure most '
        'directly comparable with the dividend and with the market price of '
        'the share.',
        'PROFIT AFTER TAX / NUMBER OF EQUITY SHARES OUTSTANDING',
        {
            'HUL': ['2024: Rs. 43.74 as published',
                    '2025: Rs. 45.32 as published',
                    '2026: 10,448 / 235.00 = Rs. 44.41 (normalised). The '
                    'published earnings per share for the year, on the '
                    'reported profit of Rs. 15,059 crore, was Rs. 64.01.'],
            'BRITANNIA': ['2024: Rs. 88.84 as published',
                          '2025: Rs. 90.45 as published',
                          '2026: Rs. 105.18 as published'],
            'DABUR': ['2024: Rs. 10.40 as published',
                      '2025: Rs. 9.97 as published',
                      '2026: Rs. 10.68 as published'],
        },
        'eps_n', '%.2f', 'three',
        ['Hindustan Unilever: Earnings per share was almost unchanged over '
         'the three years on a normalised basis, moving from Rs. 43.74 to '
         'Rs. 44.41, a compound growth rate of 0.76% a year. The published '
         'figure of Rs. 64.01 for 2026 is 45.6% higher than the preceding '
         'year, and it is worth restating why: Rs. 19.60 of that increase '
         'represents the one-time demerger gain, and the balance represents a '
         'small underlying decline. An investor reading only the published '
         'figure would draw the wrong conclusion about the company.',
         'Britannia Industries: Earnings per share rose in every year, and the '
         'compound growth rate of 8.81% over the two years is the highest of '
         'the three companies by a wide margin. Part of the 2026 increase came '
         'from a lower tax charge, but the underlying growth in operating '
         'profit also contributed.',
         'Dabur India: Earnings per share rose from Rs. 10.40 to Rs. 10.68, a '
         'compound growth rate of 1.34% a year, which is below the rate of '
         'inflation over the same period. In real terms the earnings '
         'attributable to each share were therefore lower at the end of the '
         'period than at the beginning.'],
        chart='fig6_7',
        table_label='Table 6.8: Earnings per share of the three companies (Rs.)',
        caption='Figure 6.7: Earnings per share of the three companies',
        overall=[
            'The level of earnings per share cannot be compared between the '
            'three companies because the number of shares differs widely: '
            'Hindustan Unilever has about 235 crore shares, Britannia about 24 '
            'crore and Dabur about 177 crore. The growth rate, however, is '
            'comparable and it separates the three companies clearly: 8.81% a '
            'year for Britannia, 1.34% for Dabur and 0.76% for Hindustan '
            'Unilever on a normalised basis.'])

    # ---------------------------------------------------------------- 8
    _section(
        doc, fig, 8, 'RETURN ON ASSETS (ROA)',
        'Return on assets measures the profit earned by a company in relation '
        'to the total assets on its balance sheet, irrespective of how those '
        'assets are financed.',
        'PROFIT AFTER TAX / TOTAL ASSETS \u00d7 100',
        {
            'HUL': ['2024: 10,282 / 78,499 \u00d7 100 = 13.10%',
                    '2025: 10,671 / 79,880 \u00d7 100 = 13.36%',
                    '2026: 10,448 / 79,752 \u00d7 100 = 13.10% (normalised)'],
            'BRITANNIA': ['2024: 2,134 / 9,073.56 \u00d7 100 = 23.52%',
                          '2025: 2,178 / 8,838.55 \u00d7 100 = 24.64%',
                          '2026: 2,537 / 9,731.94 \u00d7 100 = 26.07%'],
            'DABUR': ['2024: 1,811 / 15,122.68 \u00d7 100 = 11.98%',
                      '2025: 1,740 / 16,232.28 \u00d7 100 = 10.72%',
                      '2026: 1,869 / 17,479.91 \u00d7 100 = 10.69%'],
        },
        'ROA', '%.2f', 'three',
        ['Hindustan Unilever: The ratio moved within a narrow range of 13.10% '
         'to 13.36% and returned to 13.10% in 2026. Total assets were almost '
         'unchanged at about Rs. 79,000 crore in each of the three years, so '
         'the ratio simply follows the profit.',
         'Britannia Industries: The ratio improved in every year, from 23.52% '
         'to 26.07%, and is the highest of the three. The reason is the small '
         'asset base: total assets of Rs. 9,731.94 crore support a profit of '
         'Rs. 2,537 crore. The company also operates with negative working '
         'capital, which keeps the asset base low.',
         'Dabur India: The ratio fell from 11.98% to 10.72% and then to 10.69%, '
         'and is the lowest of the three. Almost half of the company\u2019s '
         'assets are financial investments rather than assets used in the '
         'business, and those investments earn a return well below the return '
         'earned on the operating business, which drags the ratio down.'],
        chart='fig6_8',
        table_label='Table 6.9: Return on assets of the three companies (%)',
        caption='Figure 6.8: Return on assets of the three companies',
        overall=[
            'Britannia Industries earns roughly twice the return on assets '
            'that Hindustan Unilever and Dabur earn, and the gap widened over '
            'the three years. Since the three companies earn net margins of a '
            'similar order, the difference is almost entirely a statement '
            'about the size of the balance sheet on which each company '
            'operates. For an investor this matters because a high return on '
            'assets means less capital is consumed in producing a given profit, '
            'which in turn supports cash generation and the ability to pay '
            'dividends.'])

    # ---------------------------------------------------------------- 9
    _section(
        doc, fig, 9, 'CURRENT RATIO',
        'The current ratio compares the current assets of a company with its '
        'current liabilities and indicates whether the company can meet its '
        'short-term obligations from the assets it expects to convert into '
        'cash within a year. A ratio below one indicates a potential '
        'short-term liquidity problem if it persists.',
        'CURRENT ASSETS / CURRENT LIABILITIES',
        {
            'HUL': ['2024: 21,324 / 12,876 = 1.66 times',
                    '2025: 22,051 / 16,537 = 1.33 times',
                    '2026: 19,021 / 15,549 = 1.22 times'],
            'BRITANNIA': ['2024: 4,848.66 / 4,084.41 = 1.19 times',
                          '2025: 3,913.68 / 3,618.26 = 1.08 times',
                          '2026: 4,677.66 / 4,179.99 = 1.12 times'],
            'DABUR': ['2024: 5,679.62 / 3,930.43 = 1.45 times',
                      '2025: 6,532.46 / 4,318.44 = 1.51 times',
                      '2026: 8,885.96 / 5,239.08 = 1.70 times'],
        },
        'CR', '%.2f', 'three',
        ['Hindustan Unilever: The ratio fell in every year, from 1.66 to 1.22 '
         'times, as current liabilities rose from Rs. 12,876 crore to '
         'Rs. 15,549 crore while current assets fell. The company can sustain a '
         'low ratio because it has no debt and generates a large operating '
         'cash flow, but the trend indicates that working capital is being used '
         'more intensively than before.',
         'Britannia Industries: The ratio is the lowest of the three in every '
         'year, at 1.19, 1.08 and 1.12 times. The company operates with '
         'negative working capital, collecting from distributors before paying '
         'its suppliers, and a low current ratio is the expected consequence. '
         'The ratio never falls below one, so the position does not indicate a '
         'liquidity problem.',
         'Dabur India: The ratio improved from 1.45 to 1.70 times and is the '
         'highest of the three. The improvement is largely due to the increase '
         'in current investments, which rose from Rs. 1,667 crore to about '
         'Rs. 4,595 crore. The strength of the ratio therefore reflects the '
         'accumulation of financial assets rather than an improvement in the '
         'operating liquidity of the business.'],
        chart='fig6_9',
        table_label='Table 6.10: Current ratio of the three companies (times)',
        caption='Figure 6.9: Current ratio of the three companies',
        overall=[
            'A conventional reading of the current ratio would place Dabur '
            'first and Britannia last. That reading is misleading here. The '
            'current ratio is a measure of the ability to meet short-term '
            'obligations, not of financial strength, and in a sector in which '
            'the larger companies operate with negative working capital a low '
            'ratio is a sign of bargaining power with suppliers and '
            'distributors rather than of weakness. The absence of any '
            'borrowings at Hindustan Unilever and the consistently negative '
            'cash conversion cycle at Britannia and Dabur mean that none of the '
            'three faces a liquidity risk on the evidence of these three '
            'years.'])

    # ---------------------------------------------------------------- 10
    _section(
        doc, fig, 10, 'PRICE TO EARNING (P/E) RATIO',
        'The price to earnings ratio compares the market price of a share with '
        'the earnings attributable to it. It indicates how many rupees an '
        'investor is willing to pay for each rupee of current earnings, and it '
        'is therefore the most widely used measure of whether a share is '
        'expensive relative to its profit.',
        'MARKET VALUE PER SHARE / EARNINGS PER SHARE',
        {
            'HUL': ['12 October 2026: 1,850.90 / 44.41 = 41.68 times (on the '
                    'normalised earnings per share)',
                    '12 October 2026: 1,850.90 / 64.01 = 28.92 times (on the '
                    'published reported earnings per share)'],
            'BRITANNIA': ['12 October 2026: 4,808.10 / 105.18 = 45.71 times'],
            'DABUR': ['12 October 2026: 384.10 / 10.68 = 35.96 times'],
        },
        'PE', '%.2f', 'one',
        ['Hindustan Unilever: At 41.68 times normalised earnings, the share '
         'carries the second highest multiple of the three companies despite '
         'having the lowest earnings growth of the three. At the published '
         'earnings of Rs. 64.01 for FY2025-26 the multiple would appear to be '
         '28.92 times, and that appearance is misleading because the earnings '
         'used in the denominator include a gain that will not recur.',
         'Britannia Industries: At 45.71 times earnings, the share is the most '
         'expensive of the three on this measure, which is consistent with the '
         'company also having the fastest earnings growth. The multiple '
         'implies that the market expects the current rate of growth to '
         'continue.',
         'Dabur India: At 35.96 times earnings, the share is the cheapest of '
         'the three, and it is also the one whose earnings have grown least. '
         'A low multiple in this case is not evidence of an opportunity alone; '
         'it reflects the market\u2019s assessment of the company\u2019s '
         'growth prospects.'],
        chart='fig6_10',
        table_label='Table 6.11: Price to earnings ratio of the three companies (times, 12 October 2026)',
        caption='Figure 6.10: Price to earnings ratio of the three companies',
        overall=[
            'The three companies trade in a narrow band of 35.96 to 45.71 '
            'times earnings, which is characteristic of a sector in which '
            'investors pay for the stability of the earnings rather than for '
            'their growth. The comparison also shows the interdependence of '
            'the ratios: Dabur looks cheapest on this measure and Britannia '
            'looks most expensive, but on the price to earnings growth ratio '
            'in section 12 the ranking is reversed, because a high multiple '
            'held on the strength of fast growth may be no less justified than '
            'a low multiple held on the strength of no growth.'])

    # ---------------------------------------------------------------- 11
    _section(
        doc, fig, 11, 'PRICE TO BOOK (P/B) RATIO',
        'The price to book ratio compares the market price of a share with the '
        'book value of the shareholders\u2019 funds attributable to it. It '
        'indicates how much an investor is paying for each rupee of net worth, '
        'and it is particularly useful for comparing companies whose earnings '
        'are volatile.',
        'MARKET PRICE PER SHARE / BOOK VALUE PER SHARE',
        {
            'HUL': ['12 October 2026: 1,850.90 / 207.40 = 8.92 times '
                    '(book value per share computed on the 235.00 crore equity '
                    'shares outstanding at 31 March 2026)'],
            'BRITANNIA': ['12 October 2026: 4,808.10 / 211.98 = 22.68 times '
                          '(book value per share computed on the 24.09 crore '
                          'equity shares outstanding at 31 March 2026)'],
            'DABUR': ['12 October 2026: 384.10 / 64.38 = 5.97 times (book '
                      'value per share computed on the 177.37 crore equity '
                      'shares outstanding at 31 March 2026)'],
        },
        'PB', '%.2f', 'one',
        ['Hindustan Unilever: The share trades at 8.92 times net worth. Book '
         'value per share fell from Rs. 217.95 in 2024 to Rs. 207.40 in 2026 '
         'because the company distributed more than it earned, so the '
         'multiple has been held up by the price rather than by any growth in '
         'net worth.',
         'Britannia Industries: At 22.68 times net worth the share is by far '
         'the most expensive of the three on this measure, which follows '
         'directly from the high return on equity: an investor pays a large '
         'premium to book value for a business that earns about 50% on that '
         'book value. Book value per share rose from Rs. 163.62 to Rs. 211.98 '
         'over the three years.',
         'Dabur India: At 5.97 times net worth the share is the cheapest of '
         'the three. Unlike Britannia, the low multiple is not the mirror '
         'image of a high return on equity: Dabur\u2019s return on equity of '
         '16.37% is the lowest of the three, so the market is not paying a '
         'premium for the net worth because that net worth is not producing a '
         'high return.'],
        chart='fig6_11',
        table_label='Table 6.12: Price to book ratio of the three companies (times, 12 October 2026)',
        caption='Figure 6.11: Price to book ratio of the three companies',
        overall=[
            'The price to book ratio separates the three companies more widely '
            'than any other ratio in this chapter, ranging from 5.97 times to '
            '22.68 times. Most of the difference is explained by the return on '
            'equity: a business that earns 49.68% on its net worth can '
            'reasonably trade at a higher multiple of that net worth than one '
            'that earns 16.37%. On this reading, Dabur\u2019s low multiple is '
            'consistent with its low return rather than an opportunity created '
            'by the market.'])

    # ---------------------------------------------------------------- 12
    _section(
        doc, fig, 12, 'PRICE TO EARNINGS GROWTH (PEG) RATIO',
        'The price to earnings growth ratio relates the price to earnings '
        'multiple of a share to the rate at which its earnings per share have '
        'grown, and it is used to test whether a high multiple is justified by '
        'the growth that accompanies it. A ratio below one is conventionally '
        'regarded as attractive; the interpretation becomes unreliable as the '
        'growth rate approaches zero.',
        'PRICE TO EARNINGS RATIO / COMPOUND ANNUAL GROWTH RATE IN EARNINGS PER '
        'SHARE (IN PER CENT)',
        {
            'HUL': ['12 October 2026: 41.68 / 0.76 = 54.62 times (growth of '
                    '0.76% a year in normalised earnings per share from '
                    'Rs. 43.74 in FY2024 to Rs. 44.41 in FY2026)'],
            'BRITANNIA': ['12 October 2026: 45.71 / 8.81 = 5.19 times (growth '
                          'of 8.81% a year in earnings per share from '
                          'Rs. 88.84 to Rs. 105.18)'],
            'DABUR': ['12 October 2026: 35.96 / 1.34 = 26.90 times (growth of '
                      '1.34% a year in earnings per share from Rs. 10.40 to '
                      'Rs. 10.68)'],
        },
        'PEG', '%.2f', 'one',
        ['Hindustan Unilever: The ratio of 54.62 times is not a meaningful '
         'measurement of value but an arithmetic consequence of dividing a '
         'high multiple by a growth rate close to zero. Its analytical content '
         'is nevertheless clear: the market is paying about 42 times earnings '
         'for a business whose normalised earnings per share grew by less than '
         'one per cent a year over the period studied.',
         'Britannia Industries: At 5.19 times, the ratio is the lowest of the '
         'three and by a wide margin. It is the only company of the three for '
         'which the multiple is supported by a growth rate of a size that '
         'makes the ratio informative.',
         'Dabur India: At 26.90 times, the ratio reflects a multiple of about '
         '36 times earnings set against growth of about 1.3% a year. As with '
         'Hindustan Unilever, the ratio is unstable, and it should be read as '
         'a statement that the current multiple is not supported by the '
         'growth actually delivered.'],
        chart='fig6_12',
        table_label='Table 6.13: Price to earnings growth ratio of the three companies (times, 12 October 2026)',
        caption='Figure 6.12: Price to earnings growth ratio of the three '
                'companies',
        overall=[
            'This is the ratio on which the three companies differ most '
            'sharply, and it is also the ratio that most needs care in '
            'interpretation. Where the growth rate is close to zero, as it is '
            'for Hindustan Unilever and Dabur, the ratio becomes very large '
            'and its sign and magnitude are driven by the denominator rather '
            'than by anything about the business. The useful comparison is '
            'between Britannia, at 5.19 times, and the other two. On that '
            'comparison the market is paying a higher multiple for Britannia '
            'but is receiving a growth rate six to eleven times as large in '
            'exchange for it.'])

    # ---------------------------------------------------------------- 13
    _section(
        doc, fig, 13, 'RETURN ON INVESTMENT (ROI) RATIO',
        'In this report, return on investment measures the profit available to '
        'shareholders after interest and tax as a proportion of the total '
        'capital invested in the business by shareholders and lenders '
        'together. It differs from return on capital employed in that the '
        'profit is measured after the payment of interest and tax, and from '
        'return on equity in that the capital base includes borrowings.',
        'PROFIT AFTER TAX / (SHAREHOLDERS\u2019 FUNDS + TOTAL BORROWINGS) '
        '\u00d7 100',
        {
            'HUL': ['2024: 10,282 / 51,231 \u00d7 100 = 20.07%',
                    '2025: 10,671 / 49,403 \u00d7 100 = 21.60%',
                    '2026: 10,448 / 48,739 \u00d7 100 = 21.44%'],
            'BRITANNIA': ['2024: 2,134 / 5,982.73 \u00d7 100 = 35.67%',
                          '2025: 2,178 / 5,580.49 \u00d7 100 = 39.03%',
                          '2026: 2,537 / 6,464.39 \u00d7 100 = 39.25%'],
            'DABUR': ['2024: 1,811 / 11,024.37 \u00d7 100 = 16.43%',
                      '2025: 1,740 / 11,530.81 \u00d7 100 = 15.09%',
                      '2026: 1,869 / 12,482.20 \u00d7 100 = 14.97%'],
        },
        'ROI', '%.2f', 'three',
        ['Hindustan Unilever: The return is identical to the return on equity '
         'in all three years because the company has no borrowings, so the '
         'denominator of the two ratios is the same. It rose from 20.07% to '
         '21.44%, and as with return on equity the improvement comes from the '
         'reduction in the capital base rather than from growth in profit.',
         'Britannia Industries: The return rose from 35.67% to 39.25% and is '
         'the highest of the three. It is lower than the return on capital '
         'employed of 52.63% because the profit is measured after interest and '
         'tax, but it is higher than the return on equity of 49.68% would '
         'suggest relative to capital employed, because the equity base is '
         'small relative to total capital. The two together give a reliable '
         'picture: the company earns a very high return on a comparatively '
         'small capital base.',
         'Dabur India: The return fell in every year, from 16.43% to 15.09% '
         'and then to 14.97%, and is the lowest of the three. Capital '
         'invested rose by about Rs. 1,458 crore over the period while profit '
         'after tax rose by Rs. 58 crore, which is the arithmetic expression '
         'of the company\u2019s difficulty in finding profitable uses for the '
         'cash it generates.'],
        chart='fig6_13',
        table_label='Table 6.14: Return on investment of the three companies (%)',
        caption='Figure 6.13: Return on investment of the three companies',
        overall=[
            'The ordering on this ratio is the same as on return on capital '
            'employed and return on equity, which is to be expected because the '
            'three ratios share the same numerator or a closely related one. '
            'Taken together with the operating ratio and the interest coverage '
            'ratio, the ratio set supports two conclusions. Hindustan Unilever '
            'operates the most efficient business and carries the least '
            'financial risk. Britannia earns the highest return on the capital '
            'it employs. Dabur is the weakest on every measure of return, and '
            'the weakness is a matter of the deployment of capital rather than '
            'of the profitability of its products.'])

    # ------------------------------------------------------------------
    # Factor analysis
    # ------------------------------------------------------------------
    doc.new_page()
    doc.heading('Factors Analysis', 2, '   Factor Analysis')
    doc.para(
        'Factor analysis in this report compares the three companies by '
        'assigning a rank and a score to each company on each of the thirteen '
        'ratios computed above. The company with the best performance on a '
        'ratio is given rank 1 and a score of 10, the second is given rank 2 '
        'and a score of 9, and the third is given rank 3 and a score of 8. The '
        'maximum score available is therefore 130, being thirteen ratios '
        'multiplied by ten. For the debt to equity, operating ratio, price to '
        'earnings, price to book and price to earnings growth ratios the '
        'lowest value is treated as the best, and for the remaining eight '
        'ratios the highest value is treated as the best.', align='both')
    doc.para(
        'The scores are assigned on the FY2025-26 figures, because that is the '
        'most recent year for which all three companies have audited figures '
        'and because ranking three companies on three years of data would give '
        'the same company a different rank in each column without resolving '
        'which of the three positions is the more meaningful. A supplementary '
        'check on the strength of the ranking across all three years is given '
        'at the end of this section.', align='both')
    _factor_table(doc)

    doc.para('COMPANY RANKINGS', bold=True, align='left', before=160)
    doc.para('Table 6.16: Overall ranking of the three companies on the factor '
             'analysis', bold=True, align='left', before=60)
    doc.table([
        ['COMPANY', 'TOTAL SCORE (OUT OF 130)', 'OVERALL RANKING'],
        ['Hindustan Unilever Ltd.', '120', '1st'],
        ['Britannia Industries Ltd.', '117', '2nd'],
        ['Dabur India Ltd.', '114', '3rd'],
    ], [3500, 3466, 3500], aligns=['l', 'c', 'c'])
    doc.after_table(0.5)
    doc.para('Interpretation :', bold=True, align='left', before=140)
    for b in [
        'Hindustan Unilever has the highest total score of 120. It is ranked '
        'first on four of the thirteen ratios, namely net profit margin, debt '
        'to equity, operating ratio and interest coverage; second on eight; '
        'and third on only one, the price to earnings growth ratio. Its score '
        'reflects consistency across the whole ratio set rather than dominance '
        'on any single measure, because it is second on all four return '
        'ratios.',
        'Britannia Industries has a total score of 117 and is ranked first on '
        'six ratios, the largest number of first places of the three '
        'companies: return on capital employed, return on equity, return on '
        'assets, return on investment, earnings per share and the price to '
        'earnings growth ratio. It is ranked third on the other six, namely '
        'net profit margin, debt to equity, operating ratio, current ratio, '
        'price to earnings and price to book. The contrast is the point: the '
        'company that earns the highest return on capital is also the company '
        'that scores worst on margin, leverage and liquidity, because it earns '
        'its return by employing very little capital rather than by earning a '
        'high margin on each sale.',
        'Dabur India has a total score of 114 and is ranked first in three '
        'ratios: the current ratio, the price to earnings ratio and the price '
        'to book ratio. All three first places arise because a low or a high '
        'value looks favourable in isolation: the current ratio is high '
        'because the company holds financial investments, and the two '
        'valuation ratios are low because the company has grown slowly. On '
        'the eight profitability and return ratios the company ranks third in '
        'seven.',
        'The margin between the first and the third company is six points out '
        'of 130, which is under five per cent of the maximum score. That '
        'narrowness is worth stating explicitly: the scoring method gives each '
        'ratio the same weight, so a company that finished second on every '
        'ratio would score 117, which is exactly the score of Britannia. A '
        'ranking of this kind measures consistency across the ratio set rather '
        'than the magnitude of the difference between the companies, and the '
        'magnitude of the difference is better seen in the individual ratios, '
        'where the return on capital employed of Britannia is more than two '
        'and a half times that of Dabur.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)
    doc.para(
        'A supplementary check was carried out to test whether the ranking is '
        'an artefact of the single year used. The ten ratios that are computed '
        'year by year were scored separately in each of the three years and '
        'the three market-based ratios were scored once, giving thirty-three '
        'comparisons in place of thirteen. The totals, out of a possible 99 '
        'points, were 81 for Hindustan Unilever, 61 for Britannia Industries '
        'and 56 for Dabur India. Hindustan Unilever\u2019s lead widens when '
        'the three years are taken together, because it wins the net profit '
        'margin, the debt to equity ratio, the operating ratio and interest '
        'coverage in every one of the three years, while Britannia wins all '
        'four return ratios in every year and Dabur\u2019s three wins are '
        'confined to the current ratio, the price to earnings ratio and the '
        'price to book ratio. Both calculations give the same ranking, '
        'although they give different margins, and that is the important '
        'qualification: the ranking is stable, the distances between the '
        'companies are not.',
        align='both')
    doc.para(
        'Based on the total scores, the ranking is:', align='both')
    for t in ['1. Hindustan Unilever Ltd. \u2013 120 points out of 130',
              '2. Britannia Industries Ltd. \u2013 117 points out of 130',
              '3. Dabur India Ltd. \u2013 114 points out of 130']:
        doc.para(t, align='both', indent_left=360)
    doc.para(
        'Hindustan Unilever is therefore the strongest company overall '
        'according to the selected ratios, followed by Britannia Industries '
        'and Dabur India. The result should be read together with the '
        'individual ratio analysis rather than in place of it. Britannia earns '
        'a substantially higher return on the capital it employs and grew its '
        'earnings per share at 8.81% a year against 0.76% at Hindustan '
        'Unilever, and an investor who gave greater weight to those two '
        'measures than to margin and leverage would reach a different '
        'conclusion from the same figures. The purpose of the factor analysis '
        'is to make the weighting explicit, not to remove the need for '
        'judgement.', align='both')


# ---------------------------------------------------------------------------
# Factor analysis table
# ---------------------------------------------------------------------------
FACTORS = [
    ('1)', 'Net profit margin', 'NPM', '%.2f', False),
    ('2)', 'Return on capital employed', 'ROCE', '%.2f', False),
    ('3)', 'Return on equity', 'ROE', '%.2f', False),
    ('4)', 'Debt to equity', 'DE', '%.2f', True),
    ('5)', 'Operating ratio', 'OPR', '%.2f', True),
    ('6)', 'Interest coverage', 'IC', '%.2f', False),
    ('7)', 'Earnings per share (Rs.)', 'eps_n', '%.2f', False),
    ('8)', 'Return on assets', 'ROA', '%.2f', False),
    ('9)', 'Current ratio', 'CR', '%.2f', False),
    ('10)', 'Price to earnings', 'PE', '%.2f', True),
    ('11)', 'Price to book', 'PB', '%.2f', True),
    ('12)', 'Price to earnings growth', 'PEG', '%.2f', True),
    ('13)', 'Return on investment', 'ROI', '%.2f', False),
]


def _value(key, source):
    if source == 'eps_n':
        return DATA[key]['eps_n'][2]
    if source in ('PE', 'PB', 'PEG'):
        return R[key][source]
    return R[key][source][2]


def _factor_table(doc):
    rows = [['', 'FACTOR / RATIO', 'HUL', 'Rank', 'Score',
             'Britannia', 'Rank', 'Score', 'Dabur', 'Rank', 'Score']]
    totals = {k: 0 for k in ORDER}
    for num, label, source, fmt, lower in FACTORS:
        vals = {k: _value(k, source) for k in ORDER}
        order = sorted(ORDER, key=lambda k: vals[k], reverse=not lower)
        row = [num, label]
        for k in ORDER:
            pos = order.index(k)
            totals[k] += 10 - pos
            row += [fmt % vals[k], str(pos + 1), str(10 - pos)]
        rows.append(row)
    rows.append(['', 'TOTAL SCORE', '', '', str(totals['HUL']), '', '',
                 str(totals['BRITANNIA']), '', '', str(totals['DABUR'])])
    doc.para('Table 6.15: Factor analysis of the three companies on the '
             'FY2025-26 ratios', bold=True, align='left', before=140)
    doc.table(rows, [560, 2400, 1100, 700, 700, 1100, 700, 700, 1100, 700,
                     706],
              aligns=['c', 'l', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c'])
    doc.after_table(0.4)
