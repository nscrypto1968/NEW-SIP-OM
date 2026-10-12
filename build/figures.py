"""Chart generation for the FMCG report.

The visual language deliberately matches the reference report: plain white
backgrounds, thin grey gridlines, a restrained blue palette, no chart junk.
"""

import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figs')
os.makedirs(OUT, exist_ok=True)

BLUE = '#2F5496'
MID = '#8FAADC'
LIGHT = '#C9D7EE'
GREY = '#A6A6A6'
GREEN = '#548235'
ORANGE = '#C55A11'

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.edgecolor': '#BFBFBF',
    'axes.linewidth': 0.8,
    'axes.labelcolor': '#404040',
    'text.color': '#404040',
    'xtick.color': '#404040',
    'ytick.color': '#404040',
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'savefig.facecolor': 'white',
})


def _finish(fig, name, tight=True):
    for ax in fig.axes:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(axis='y', color='#E0E0E0', linewidth=0.7)
        ax.set_axisbelow(True)
    if tight:
        fig.tight_layout()
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, dpi=200)
    plt.close(fig)
    return path


def grouped_bar(name, categories, series, ylabel, colours=None,
                fmt='{:.0f}', value_labels=True, width=6.4, height=3.1,
                ylim=None, rotation=0):
    fig, ax = plt.subplots(figsize=(width, height))
    colours = colours or [BLUE, MID, LIGHT, GREY]
    n = len(series)
    total_w = 0.78
    bw = total_w / n
    import numpy as np
    xs = np.arange(len(categories))
    for i, (label, vals) in enumerate(series.items()):
        off = -total_w / 2 + bw / 2 + i * bw
        bars = ax.bar(xs + off, vals, width=bw, label=label,
                      color=colours[i % len(colours)], edgecolor='white',
                      linewidth=0.4)
        if value_labels and len(categories) * n <= 24:
            for b, v in zip(bars, vals):
                off = (0, 3) if v >= 0 else (0, -9)
                va = 'bottom' if v >= 0 else 'top'
                ax.annotate(fmt.format(v), (b.get_x() + b.get_width() / 2, v),
                            textcoords='offset points', xytext=off, va=va,
                            ha='center', fontsize=6.5, color='#404040')
    ax.set_xticks(xs)
    ax.set_xticklabels(categories, rotation=rotation,
                       ha='right' if rotation else 'center')
    ax.set_ylabel(ylabel, fontsize=8.5)
    if ylim:
        ax.set_ylim(*ylim)
    if n > 1:
        ax.legend(frameon=False, fontsize=8, ncol=min(n, 3), loc='best')
    return _finish(fig, name)


def line_chart(name, categories, series, ylabel, colours=None, fmt='{:.1f}',
               width=6.4, height=3.1, marker='o', value_labels=False,
               legend_loc='best'):
    fig, ax = plt.subplots(figsize=(width, height))
    colours = colours or [BLUE, MID, LIGHT, GREEN, ORANGE, GREY]
    for i, (label, vals) in enumerate(series.items()):
        ax.plot(categories, vals, marker=marker, markersize=5, linewidth=1.8,
                color=colours[i % len(colours)], label=label)
        if value_labels:
            for x, v in zip(categories, vals):
                ax.annotate(fmt.format(v), (x, v), textcoords='offset points',
                            xytext=(0, 6), ha='center', fontsize=6.5)
    ax.set_ylabel(ylabel, fontsize=8.5)
    if len(series) > 1:
        ax.legend(frameon=False, fontsize=8, ncol=min(len(series), 4),
                  loc=legend_loc)
    return _finish(fig, name)


def pie_chart(name, labels, values, colours=None, width=6.0, height=3.1,
              fmt='{:.1f}%', startangle=90):
    fig, ax = plt.subplots(figsize=(width, height))
    colours = colours or [BLUE, MID, LIGHT, GREY, '#D9E2F3', '#7F7F7F']
    wedges, texts, autotexts = ax.pie(
        values, labels=None, autopct=lambda p: fmt.format(p),
        startangle=startangle,
        colors=colours[:len(values)], wedgeprops=dict(width=0.45,
                                                      edgecolor='white'),
        pctdistance=0.79, textprops=dict(fontsize=8))
    for t in autotexts:
        t.set_color('white')
        t.set_fontsize(8)
    ax.legend(wedges, labels, frameon=False, fontsize=8, loc='center left',
              bbox_to_anchor=(0.92, 0.5))
    ax.set_aspect('equal')
    return _finish(fig, name, tight=False)


def single_bar(name, categories, values, ylabel, colour=BLUE, fmt='{:.0f}',
               width=6.4, height=3.1, value_labels=True, rotation=0):
    return grouped_bar(name, categories, {'': values}, ylabel,
                       colours=[colour], fmt=fmt, value_labels=value_labels,
                       width=width, height=height, rotation=rotation)


def two_panel(name, categories, left, right, left_ylabel, right_ylabel,
              left_title, right_title, width=6.4, height=2.9, fmt='{:.0f}'):
    fig, axes = plt.subplots(1, 2, figsize=(width, height))
    for ax, vals, ylab, title, colour in (
            (axes[0], left, left_ylabel, left_title, BLUE),
            (axes[1], right, right_ylabel, right_title, MID)):
        xs = range(len(categories))
        bars = ax.bar(xs, vals, width=0.55, color=colour, edgecolor='white',
                      linewidth=0.4)
        ax.set_xticks(list(xs))
        ax.set_xticklabels(categories, fontsize=7.5)
        ax.set_ylabel(ylab, fontsize=8.5)
        ax.set_title(title, fontsize=9, color='#404040', pad=6)
        for b, v in zip(bars, vals):
            off = (0, 3) if v >= 0 else (0, -9)
            va = 'bottom' if v >= 0 else 'top'
            ax.annotate(fmt.format(v), (b.get_x() + b.get_width() / 2, v),
                        textcoords='offset points', xytext=off, va=va,
                        ha='center', fontsize=6.5, color='#404040')
    return _finish(fig, name)


def build_internship():
    """Worked-example charts for Chapter 2, Section 2.8."""
    single_bar('fig2_1', ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'],
               [5000, -6500, -7500, 11250, 6750],
               'Daily mark-to-market cash flow (Rs.)', fmt='{:.0f}')

    line_chart('fig2_2', ['1,150', '1,200', '1,250', '1,260', '1,280',
                          '1,301', '1,320', '1,360', '1,400'],
               {'Net profit or loss on one lot (Rs.)':
                [-38690, -38690, -38690, -38690, -18690, 2310, 21310, 61310,
                 101310]},
               'Rs. per lot', fmt='{:.0f}', marker='o', height=2.9)

    pie_chart('fig2_3', ['Securities transaction tax', 'Brokerage',
                         'Goods and services tax', 'Stamp duty',
                         'Exchange charges and SEBI fee'],
              [200.00, 100.00, 19.11, 15.00, 6.14])


# ---------------------------------------------------------------------------
# Chapter 3 and 5.2 : sector charts
# ---------------------------------------------------------------------------
def build_sector():
    # Indian FMCG market size, US$ billion
    single_bar('fig3_1', ['2025', '2030 (projected)'], [289.1, 642.87],
               'US$ billion', fmt='{:.1f}')

    pie_chart('fig3_2', ['Urban', 'Rural'], [62.0, 38.0])

    # NielsenIQ value and volume growth, %
    grouped_bar('fig5_1', ['Q1 FY26', 'Q2 FY26', 'CY2025 (full year)'],
                {'Value growth': [13.9, 12.9, 0.0],
                 'Volume growth': [6.0, 5.4, 4.1]},
                'Growth over the previous year (%)', fmt='{:.1f}',
                value_labels=True)

    single_bar('fig5_2', ['Household and\npersonal care',
                          'Food and\nbeverages',
                          'Health and\nwellness',
                          'Others'],
               [50, 30, 12, 8], 'Share of FMCG sales (%)',
               fmt='{:.0f}', rotation=0)


# ---------------------------------------------------------------------------
# Chapter 5 : company revenue and profit
# ---------------------------------------------------------------------------
def build_company_charts():
    yrs = ['FY2023-24', 'FY2024-25', 'FY2025-26']
    two_panel('fig5_3', yrs, [61896, 61328, 64468], [10282, 10671, 15059],
              'Net revenue (Rs. crore)', 'Profit after tax (Rs. crore)',
              'Hindustan Unilever \u2014 net revenue',
              'Hindustan Unilever \u2014 profit after tax')
    two_panel('fig5_4', yrs, [16769, 17943, 19152], [2134, 2178, 2537],
              'Net revenue (Rs. crore)', 'Profit after tax (Rs. crore)',
              'Britannia Industries \u2014 net revenue',
              'Britannia Industries \u2014 profit after tax')
    two_panel('fig5_5', yrs, [12404, 12563, 13193], [1811, 1740, 1869],
              'Net revenue (Rs. crore)', 'Profit after tax (Rs. crore)',
              'Dabur India \u2014 net revenue',
              'Dabur India \u2014 profit after tax')


# ---------------------------------------------------------------------------
# Chapter 6 : one comparison chart per ratio
# ---------------------------------------------------------------------------
COMPANIES = ['Hindustan\nUnilever', 'Britannia\nIndustries', 'Dabur\nIndia']
YEARS = ['FY2024', 'FY2025', 'FY2026']


def _ratio(name, data, ylabel, fmt='{:.1f}', ylim=None, suffix=''):
    grouped_bar(name, COMPANIES, data, ylabel, fmt=fmt, ylim=ylim)


RATIO_CHARTS = [
    ('fig6_1', 'NPM', 'Net profit margin (%)', '{:.2f}', 3),
    ('fig6_2', 'ROCE', 'Return on capital employed (%)', '{:.2f}', 3),
    ('fig6_3', 'ROE', 'Return on equity (%)', '{:.2f}', 3),
    ('fig6_4', 'DE', 'Debt to equity (times)', '{:.2f}', 3),
    ('fig6_5', 'OPR', 'Operating ratio (%)', '{:.2f}', 3),
    ('fig6_6', 'IC', 'Interest coverage (times)', '{:.2f}', 3),
    ('fig6_7', 'eps', 'Earnings per share (Rs.)', '{:.2f}', 3),
    ('fig6_8', 'ROA', 'Return on assets (%)', '{:.2f}', 3),
    ('fig6_9', 'CR', 'Current ratio (times)', '{:.2f}', 3),
    ('fig6_10', 'PE', 'Price to earnings (times)', '{:.2f}', 1),
    ('fig6_11', 'PB', 'Price to book (times)', '{:.2f}', 1),
    ('fig6_12', 'PEG', 'Price to earnings growth (times)', '{:.2f}', 1),
    ('fig6_13', 'ROI', 'Return on investment (%)', '{:.2f}', 3),
]


def build_ratios():
    """One comparison chart per ratio, taken from ratios.py."""
    from ratios import R, DATA, ORDER

    def val(k, source, kind, i=None):
        if source == 'eps':
            return DATA[k]['eps_n'][i] if i is not None else DATA[k]['eps_n'][2]
        if kind == 1:
            return R[k][source]
        return R[k][source][i]

    for name, source, ylabel, fmt, kind in RATIO_CHARTS:
        if kind == 3:
            data = {y: [val(k, source, kind, i) for k in ORDER]
                    for i, y in enumerate(YEARS)}
            grouped_bar(name, COMPANIES, data, ylabel, fmt=fmt)
        else:
            single_bar(name, COMPANIES, [val(k, source, kind) for k in ORDER],
                       ylabel, fmt=fmt, rotation=0)


def build_conclusion_figures():
    single_bar('fig7_1', ['Hindustan Unilever', 'Britannia Industries',
                          'Dabur India'], [120, 117, 114],
               'Composite score out of 130', fmt='{:.0f}')


# ---------------------------------------------------------------------------
# Appendix charts
# ---------------------------------------------------------------------------
def build_appendix():
    """Five-year trend and valuation charts for the appendix."""
    single_bar('figA_1', ['FY2022', 'FY2023', 'FY2024', 'FY2025', 'FY2026'],
               [58154, 60580, 61896, 61328, 64468], 'Net revenue (Rs. crore)',
               fmt='{:.0f}')
    pie_chart('figA_2', ['Home care', 'Beauty and wellbeing',
                         'Personal care', 'Foods', 'Others'],
              [34.0, 22.0, 22.0, 20.0, 2.0])
    single_bar('figA_3', ['FY2022', 'FY2023', 'FY2024', 'FY2025', 'FY2026'],
               [8892, 10143, 10282, 10671, 15059],
               'Profit after tax (Rs. crore)', colour=MID, fmt='{:.0f}')
    grouped_bar('figA_4',
                ['Hindustan Unilever', 'Britannia Industries', 'Dabur India'],
                {'Price to earnings (times)': [41.68, 45.71, 35.96]},
                'Times', fmt='{:.2f}', ylim=(0, 50))
    single_bar('figA_5', ['52 week high', 'Price on 12.10.2026',
                          '52 week low'],
               [2667.20, 1850.90, 1826.90], 'Rs. per share', fmt='{:.0f}',
               rotation=0)


if __name__ == '__main__':
    build_internship()
    build_sector()
    build_company_charts()
    build_ratios()
    build_conclusion_figures()
    build_appendix()
    print('charts written to', OUT)
