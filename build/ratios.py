# -*- coding: utf-8 -*-
"""Single source of truth for every ratio used in Chapters 5, 6 and 7.

All figures are consolidated, in Rs. crore unless stated. Inputs are taken
from the companies' audited consolidated financial statements as collected
for the study. Ratios are computed here so that the narrative, the tables
and the charts cannot disagree.
"""

YR = ['FY2024', 'FY2025', 'FY2026']

DATA = {
    'HUL': dict(
        rev=[61896, 61328, 64468],
        op=[14659, 14698, 15039],
        oi=[817, 1355, 4923],
        interest=[334, 381, 410],
        dep=[1216, 1253, 1333],
        pbt=[13926, 14419, 18219],
        # FY2026 net of the one-time demerger gain
        pbt_n=[13926, 14419, 13608],
        pat=[10282, 10671, 15059],
        # FY2026 excludes the one-time demerger gain of Rs. 4,611 crore
        pat_n=[10282, 10671, 10448],
        shf=[51218.00, 49402.00, 48739.00],
        debt=[13.00, 1.00, 0.00],
        ta=[78499.00, 79880.00, 79752.00],
        ca=[21324.00, 22051.00, 19021.00],
        cl=[12876.00, 16537.00, 15549.00],
        equity=[235.00, 235.00, 235.00],
        shares=235.00,
        price=1850.90,
        eps=[43.74, 45.32, 64.01],
        eps_n=[43.74, 45.32, 44.41],
    ),
    'BRITANNIA': dict(
        rev=[16769, 17943, 19152],
        op=[3166, 3177, 3514],
        oi=[211, 202, 224],
        interest=[164, 139, 113],
        dep=[300, 313, 337],
        pbt=[2913, 2927, 3289],
        pbt_n=[2913, 2927, 3289],
        pat=[2134, 2178, 2537],
        pat_n=[2134, 2178, 2537],
        shf=[3941.52, 4355.72, 5106.56],
        debt=[2041.21, 1224.77, 1357.83],
        ta=[9073.56, 8838.55, 9731.94],
        ca=[4848.66, 3913.68, 4677.66],
        cl=[4084.41, 3618.26, 4179.99],
        equity=[24.09, 24.09, 24.09],
        shares=24.09,
        price=4808.10,
        eps=[88.84, 90.45, 105.18],
        eps_n=[88.84, 90.45, 105.18],
    ),
    'DABUR': dict(
        rev=[12404, 12563, 13193],
        op=[2400, 2316, 2450],
        oi=[482, 552, 584],
        interest=[124, 164, 145],
        dep=[399, 446, 469],
        pbt=[2359, 2258, 2420],
        pbt_n=[2359, 2258, 2420],
        pat=[1811, 1740, 1869],
        pat_n=[1811, 1740, 1869],
        shf=[9866.30, 10800.69, 11419.52],
        debt=[1158.07, 730.12, 1062.68],
        ta=[15122.68, 16232.28, 17479.91],
        ca=[5679.62, 6532.46, 8885.96],
        cl=[3930.43, 4318.44, 5239.08],
        equity=[177.20, 177.23, 177.37],
        shares=177.37,
        price=384.10,
        eps=[10.40, 9.97, 10.68],
        eps_n=[10.40, 9.97, 10.68],
    ),
}

NAMES = {'HUL': 'Hindustan Unilever', 'BRITANNIA': 'Britannia Industries',
         'DABUR': 'Dabur India'}
ORDER = ['HUL', 'BRITANNIA', 'DABUR']


def pct(a, b):
    return 100.0 * a / b


def ratios(key):
    d = DATA[key]
    out = {}
    out['NPM'] = [pct(d['pat_n'][i], d['rev'][i]) for i in range(3)]
    out['OPM'] = [pct(d['op'][i], d['rev'][i]) for i in range(3)]
    out['OPR'] = [pct(d['rev'][i] - d['op'][i], d['rev'][i]) for i in range(3)]
    out['ROCE'] = [pct(d['pbt_n'][i] + d['interest'][i],
                       d['shf'][i] + d['debt'][i]) for i in range(3)]
    out['ROE'] = [pct(d['pat_n'][i], d['shf'][i]) for i in range(3)]
    out['ROA'] = [pct(d['pat_n'][i], d['ta'][i]) for i in range(3)]
    out['ROI'] = [pct(d['pat_n'][i], d['shf'][i] + d['debt'][i])
                  for i in range(3)]
    out['DE'] = [d['debt'][i] / d['shf'][i] for i in range(3)]
    out['IC'] = [(d['pbt_n'][i] + d['interest'][i]) / d['interest'][i]
                 for i in range(3)]
    out['CR'] = [d['ca'][i] / d['cl'][i] for i in range(3)]
    out['BVPS'] = [d['shf'][i] / d['shares'] for i in range(3)]
    out['PE'] = d['price'] / d['eps_n'][2]
    out['PE_rep'] = d['price'] / d['eps'][2]
    out['PB'] = d['price'] / out['BVPS'][2]
    g = (d['eps_n'][2] / d['eps_n'][0]) ** 0.5 - 1.0
    out['EPS_CAGR'] = 100.0 * g
    out['PEG'] = out['PE'] / out['EPS_CAGR'] if g > 0 else float('inf')
    return out


R = {k: ratios(k) for k in ORDER}

# Ratios where a higher value is better; the rest are 'lower is better'
HIGHER = ['NPM', 'OPM', 'ROCE', 'ROE', 'ROA', 'ROI', 'IC', 'CR']
LOWER = ['OPR', 'DE', 'PE', 'PB', 'PEG']
THREE_YEAR = HIGHER + LOWER[:2]          # 10 ratios x 3 years = 30 cells
ONE_DATE = LOWER[2:]                      # 3 ratios x 1 date   = 3 cells


def rank_cells():
    """Return {(ratio, period): {company: points}} with 3/2/1 points."""
    cells = {}
    for r in THREE_YEAR:
        for i, y in enumerate(YR):
            vals = {k: R[k][r][i] for k in ORDER}
            cells[(r, y)] = _points(vals, r in HIGHER)
    for r in ONE_DATE:
        vals = {k: R[k][r] for k in ORDER}
        cells[(r, 'Oct-2026')] = _points(vals, r in HIGHER)
    return cells


def _points(vals, higher_better):
    ordered = sorted(vals, key=lambda k: vals[k], reverse=higher_better)
    return {k: (len(ORDER) - j) for j, k in enumerate(ordered)}


CELLS = rank_cells()
TOTAL = {k: 0 for k in ORDER}
BEST = {k: 0 for k in ORDER}
for key, pts in CELLS.items():
    for k, p in pts.items():
        TOTAL[k] += p
        if p == 3:
            BEST[k] += 1
MAXP = 3 * len(CELLS)

LABEL = {
    'NPM': 'Net profit margin', 'OPM': 'Operating profit margin',
    'OPR': 'Operating ratio', 'ROCE': 'Return on capital employed',
    'ROE': 'Return on equity', 'ROA': 'Return on assets',
    'ROI': 'Return on investment', 'DE': 'Debt to equity',
    'IC': 'Interest coverage', 'CR': 'Current ratio',
    'BVPS': 'Book value per share', 'PE': 'Price to earnings',
    'PE_rep': 'Price to earnings (reported)',
    'PB': 'Price to book', 'PEG': 'Price to earnings growth',
    'EPS_CAGR': 'EPS compound growth (%)',
}


def show():
    for r in ['NPM', 'OPM', 'OPR', 'ROCE', 'ROE', 'ROA', 'ROI', 'DE',
              'IC', 'CR', 'BVPS', 'EPS_CAGR', 'PE', 'PE_rep', 'PB', 'PEG']:
        line = '%-34s' % LABEL[r]
        vals = []
        for k in ORDER:
            v = R[k][r]
            if isinstance(v, list):
                vals.append(' / '.join('%7.2f' % x for x in v))
            else:
                vals.append('%7.2f' % v)
        print(line + '  ' + '   '.join(vals))
    print()
    print('cells:', len(CELLS), ' max points:', MAXP)
    for k in ORDER:
        print('%-22s points %3d   first places %2d' %
              (NAMES[k], TOTAL[k], BEST[k]))
    print()
    # per-ratio winners over the three years
    for r in THREE_YEAR:
        w = []
        for i, y in enumerate(YR):
            winner = max(ORDER, key=lambda k: R[k][r][i]
                         if r in HIGHER else -R[k][r][i])
            w.append(NAMES[winner].split()[0])
        print('%-28s %s' % (LABEL[r], ' / '.join(w)))
    for r in ONE_DATE:
        winner = min(ORDER, key=lambda k: R[k][r])
        print('%-28s %s' % (LABEL[r], NAMES[winner]))


if __name__ == '__main__':
    show()
