# -*- coding: utf-8 -*-
"""Worked examples from the internship, folded into Chapter 2 Section 2.8.

These are the author's own computations prepared on the dealing desk. Every
price, rate, lot size and percentage used is an illustration chosen to
demonstrate a mechanism and is labelled as such; none of the figures is a
market observation or an internal parameter of the firm.
"""

from docgen import Doc


def examples(doc, fig):
    para = lambda t, **kw: doc.para(t, align='both', **kw)

    # ------------------------------------------------------------------ K
    doc.para('K.  The working day of a dealer', bold=True, align='left',
             before=160)
    para(
        'The dealing day is organised around a fixed sequence of tasks that '
        'begins before the market opens and ends after it closes. Table 2.16 '
        'records the sequence as it was followed during the internship, with '
        'the control applied at each stage and the output produced.')
    doc.table_title('Table 2.16: Timeline of a dealing-desk day, task by task')
    doc.table([
        ['Phase', 'Task performed', 'Control applied', 'Output'],
        ['Pre-market', 'Review of news, corporate actions and the derivative '
                       'ban list',
         'Cross-check against the exchange circular published that morning',
         'List of restricted scrips'],
        ['Pre-market', 'Verification of client-wise limits released by the '
                       'risk system',
         'Limit must be read before, not after, an instruction is accepted',
         'Tradable limit per client'],
        ['Continuous', 'Order entry against a verified client instruction',
         'Client code, quantity, price and segment confirmed before release',
         'Order number'],
        ['Continuous', 'Response to margin-shortfall alerts',
         'Escalation to risk management; no limit is granted at the desk',
         'Top-up or square-off'],
        ['Pre-close', 'Intraday square-off of positions that cannot be '
                      'carried',
         'Executed before the cut-off time set by the firm',
         'Flat intraday book'],
        ['Post-close', 'Verification of executions against the trade book',
         'Every fill matched to an instruction', 'Confirmed trade list'],
        ['Post-close', 'Reconciliation with the back office and check of the '
                       'contract note',
         'Discrepancy reported the same evening', 'Reconciled client position'],
    ], [1400, 3400, 3300, 2366], aligns=['l', 'l', 'l', 'l'])
    doc.after_table(0.4)
    para(
        'Seven of the nine tasks in this sequence are preparation, control or '
        'verification, and only two involve execution. The dealing function is '
        'therefore better understood as a controlled process with an execution '
        'step inside it than as an execution function with controls attached. '
        'It also explains an observation that recurred during the internship: '
        'the problems that had to be escalated arose more often from something '
        'missed in the pre-market block than from anything that went wrong '
        'during trading.')

    # ------------------------------------------------------------------ L
    doc.para('L.  Pre-trade risk checks applied before an order leaves the '
             'member\u2019s server', bold=True, align='left', before=160)
    para(
        'When an order is placed through the Computer-to-Computer Link '
        'facility it is first tested at the member\u2019s own server. The checks '
        'are listed in Table 2.17. They matter because a rejection at this '
        'stage is within the firm\u2019s control and can be resolved by the '
        'desk, whereas a rejection at the exchange cannot.')
    doc.table_title('Table 2.17: Pre-trade risk checks applied to an order at the '
             'member\u2019s server')
    doc.table([
        ['Check', 'What is tested', 'Consequence of failure'],
        ['Client code validity',
         'That the code is registered, active and permitted in the segment',
         'Order rejected; compliance consulted'],
        ['Available margin',
         'That collateral and free balance cover the margin requirement',
         'Order rejected; the client is asked to fund or pledge'],
        ['Order value limit',
         'That the value of a single order is within the client\u2019s ceiling',
         'Order rejected; it may be split only with authority'],
        ['Price reasonability',
         'That the price is within a band around the last traded price',
         'Order rejected; protects against a keying error'],
        ['Scrip permission',
         'That the scrip is not restricted, suspended or under a ban',
         'Order rejected, or permitted only to reduce a position'],
        ['Segment permission',
         'That the client is authorised for the cash or derivatives segment',
         'Order rejected'],
        ['Terminal and user validity',
         'That the order originates from a registered terminal and user',
         'Order rejected and the attempt logged'],
    ], [2400, 4300, 3766], aligns=['l', 'l', 'l'])
    doc.after_table(0.4)

    # ------------------------------------------------------------------ M
    doc.para('M.  Illustrative computation: the fair value of a futures '
             'contract', bold=True, align='left', before=160)
    para(
        'A futures price is not a forecast. It is the spot price plus the cost '
        'of carrying the underlying until the contract expires, so that a '
        'position in the futures contract and a financed position in the '
        'underlying produce the same result. Applying the cost-of-carry '
        'relationship to an illustrative spot price of Rs. 1,250.00 at a '
        'financing rate of 7 per cent with thirty days to expiry gives the '
        'fair value computed in Table 2.18.')
    doc.table_title('Table 2.18: Cost-of-carry fair value of a futures contract '
             '(illustrative)')
    doc.table([
        ['Input or output', 'Symbol', 'Value', 'Basis'],
        ['Spot price', 'S', 'Rs. 1,250.00', 'Illustrative'],
        ['Risk-free rate, continuously compounded', 'r', '7.00 per cent',
         'Illustrative'],
        ['Days to expiry', 't', '30 days', 'Illustrative'],
        ['Time in years', 't', '0.0822', 'Author\u2019s computation'],
        ['Theoretical futures price', 'F', 'Rs. 1,257.21',
         'Author\u2019s computation: F = S \u00d7 e^(r \u00d7 t)'],
        ['Basis', 'F \u2212 S', 'Rs. 7.21', 'Author\u2019s computation'],
        ['Basis as a percentage of spot', '\u2014', '0.577 per cent',
         'Author\u2019s computation'],
    ], [3000, 1200, 2400, 3866], aligns=['l', 'c', 'r', 'l'])
    doc.after_table(0.4)
    para(
        'The theoretical price exceeds the spot price by Rs. 7.21, or 0.577 '
        'per cent over thirty days. In practice a futures contract trades '
        'above or below this value, and the difference between the observed '
        'price and the theoretical price is what a dealer watches when a '
        'client asks whether a contract is expensive.')

    # ------------------------------------------------------------------ N
    doc.para('N.  Illustrative computation: daily mark-to-market settlement',
             bold=True, align='left', before=160)
    para(
        'Futures contracts in India are settled in cash every day. The '
        'position is marked to the daily settlement price and the difference '
        'is debited from or credited to the client\u2019s ledger the same '
        'evening. Table 2.19 traces the settlement of one long lot of 1,000 '
        'units opened at Rs. 1,257.00 over five trading days.')
    doc.table_title('Table 2.19: Five-day mark-to-market settlement on one long lot '
             '(illustrative)')
    doc.table([
        ['Day', 'Previous settlement price', 'Settlement price',
         'Price change', 'Daily MTM on 1,000 units', 'Cumulative MTM'],
        ['Day 1', 'Rs. 1,257.00', 'Rs. 1,262.00', 'Rs. 5.00', 'Rs. 5,000',
         'Rs. 5,000'],
        ['Day 2', 'Rs. 1,262.00', 'Rs. 1,255.50', 'Rs. (6.50)', 'Rs. (6,500)',
         'Rs. (1,500)'],
        ['Day 3', 'Rs. 1,255.50', 'Rs. 1,248.00', 'Rs. (7.50)', 'Rs. (7,500)',
         'Rs. (9,000)'],
        ['Day 4', 'Rs. 1,248.00', 'Rs. 1,259.25', 'Rs. 11.25', 'Rs. 11,250',
         'Rs. 2,250'],
        ['Day 5', 'Rs. 1,259.25', 'Rs. 1,266.00', 'Rs. 6.75', 'Rs. 6,750',
         'Rs. 9,000'],
        ['Total', '\u2014', '\u2014', 'Rs. 9.00', 'Rs. 9,000', 'Rs. 9,000'],
    ], [900, 2000, 1700, 1400, 2400, 2066], aligns=['l', 'r', 'r', 'r', 'r',
                                                     'r'])
    doc.after_table(0.4)
    fig('fig2_1', 6.1, 2.8, before=120, after=70)
    doc.caption('Figure 2.1: Daily mark-to-market cash flow on the illustrative '
             'position')
    para(
        'The five daily flows sum to Rs. 9,000, which is exactly the price '
        'change of Rs. 9.00 multiplied by the lot size of 1,000 units. Daily '
        'settlement therefore redistributes the final result across the days '
        'of the contract without altering it. The redistribution is what '
        'matters to a client: the position ends with a profit of Rs. 9,000, '
        'but the client had to fund two adverse days of Rs. 6,500 and '
        'Rs. 7,500 in cash while the position was open. A client who cannot '
        'fund those intermediate days does not reach the profitable end.')

    # ------------------------------------------------------------------ O
    doc.para('O.  Illustrative computation: value and sensitivities of an '
             'option', bold=True, align='left', before=160)
    para(
        'An option premium has to be estimated rather than derived from the '
        'spot price, because part of its value is the possibility that the '
        'underlying will move before expiry. An illustrative thirty-day call '
        'on the same underlying, struck at Rs. 1,260 with the spot at '
        'Rs. 1,250, is valued in Table 2.20 using the Black-Scholes-Merton '
        'model. Volatility of 28 per cent a year and a risk-free rate of 7 per '
        'cent are assumptions, not observations.')
    doc.table_title('Table 2.20: Black-Scholes inputs, computed price and '
             'sensitivities (illustrative)')
    doc.table([
        ['Item', 'Symbol', 'Value', 'Basis'],
        ['Spot price', 'S', 'Rs. 1,250.00', 'Illustrative'],
        ['Strike price', 'K', 'Rs. 1,260.00', 'Illustrative'],
        ['Time to expiry', 't', '0.0822 years (30 days)', 'Illustrative'],
        ['Risk-free rate', 'r', '7.00 per cent', 'Illustrative'],
        ['Volatility', '\u03c3', '28.00 per cent', 'Illustrative'],
        ['d\u2081', 'd\u2081', '0.0125', 'Author\u2019s computation'],
        ['d\u2082', 'd\u2082', '(0.0677)', 'Author\u2019s computation'],
        ['Call price', 'C', 'Rs. 38.69', 'Author\u2019s computation'],
        ['Put price at the same strike', 'P', 'Rs. 41.47',
         'Author\u2019s computation'],
        ['Delta of the call', '\u0394', '0.5050',
         'Author\u2019s computation'],
        ['Gamma', '\u0393', '0.003976', 'Author\u2019s computation'],
        ['Theta of the call, per day', '\u0398', 'Rs. (0.7808)',
         'Author\u2019s computation'],
        ['Vega, per one point of volatility', '\u03bd', 'Rs. 1.4296',
         'Author\u2019s computation'],
        ['Premium outlay on one lot of 1,000', '\u2014', 'Rs. 38,690',
         'Illustrative'],
        ['Break-even at expiry', 'K + C', 'Rs. 1,298.69',
         'Author\u2019s computation'],
    ], [3400, 1200, 2400, 3466], aligns=['l', 'c', 'r', 'l'])
    doc.after_table(0.4)
    para(
        'The payoff of the position at expiry is set out in Table 2.21. The '
        'buyer of the call loses the whole premium of Rs. 38,690 if the '
        'underlying is at or below Rs. 1,260 at expiry, and the position turns '
        'profitable only above Rs. 1,298.69.')
    doc.table_title('Table 2.21: Payoff of the long call at expiry (illustrative, '
             'one lot of 1,000 units)')
    doc.table([
        ['Underlying at expiry (Rs.)', 'Intrinsic value per unit (Rs.)',
         'Premium paid per unit (Rs.)',
         'Net profit or loss on one lot (Rs.)'],
        ['1,150', '0.00', '38.69', '(38,690)'],
        ['1,200', '0.00', '38.69', '(38,690)'],
        ['1,250', '0.00', '38.69', '(38,690)'],
        ['1,260', '0.00', '38.69', '(38,690)'],
        ['1,280', '20.00', '38.69', '(18,690)'],
        ['1,301', '41.00', '38.69', '2,310'],
        ['1,320', '60.00', '38.69', '21,310'],
        ['1,360', '100.00', '38.69', '61,310'],
        ['1,400', '140.00', '38.69', '1,01,310'],
    ], [2600, 2600, 2600, 2666], aligns=['r', 'r', 'r', 'r'])
    doc.after_table(0.4)
    fig('fig2_2', 6.0, 2.8, before=120, after=70)
    doc.caption('Figure 2.2: Payoff of the long call at expiry, with the '
             'break-even marked')
    para(
        'Two features of the computation are worth recording because they are '
        'counter-intuitive to a client who is new to options. The first is the '
        'break-even. The option is bought at Rs. 38.69 and the strike is '
        'Rs. 1,260, so the underlying must rise by 3.9 per cent from the spot '
        'price before the position is even; a correct view on the direction of '
        'the market is not by itself sufficient. The second is the decay of '
        'the premium. With thirty days remaining the option is worth '
        'Rs. 38.69, and with five days remaining the same option, with the '
        'spot price unchanged, is worth about Rs. 12.38. Roughly 68 per cent '
        'of the premium is therefore lost in the final five days of the '
        'contract, and this is the mechanism behind the ordinary experience '
        'that an option can be held through a correct market move and still '
        'lose money.')
    para(
        'A straddle illustrates the same point from the opposite direction. '
        'Buying both the call and the put struck at Rs. 1,250 costs Rs. 80.01 '
        'per unit, so a movement of about 6.40 per cent in either direction is '
        'required before the position breaks even. Strategies designed to '
        'profit from volatility are therefore considerably less forgiving than '
        'they appear when the two premiums are considered separately.')

    # ------------------------------------------------------------------ P
    doc.para('P.  Illustrative computation: margin build-up and the mechanics '
             'of a shortfall', bold=True, align='left', before=160)
    para(
        'The margin required on a position is prescribed by the clearing '
        'corporation and is not a matter of negotiation between the firm and '
        'the client. Table 2.22 builds up the requirement on the futures '
        'position described above using illustrative percentages, because the '
        'parameters actually applied by the clearing corporation are '
        'proprietary and are revised daily.')
    doc.table_title('Table 2.22: Margin build-up on one long futures lot '
             '(illustrative)')
    doc.table([
        ['Component', 'Basis', 'Rate', 'Amount (Rs.)'],
        ['Contract value', 'Entry price Rs. 1,257.00 \u00d7 lot of 1,000',
         '\u2014', '12,57,000'],
        ['Initial margin', 'Contract value \u00d7 rate', '9.50 per cent',
         '1,19,415'],
        ['Exposure margin', 'Contract value \u00d7 rate', '3.50 per cent',
         '43,995'],
        ['Total margin required', 'Initial margin + exposure margin',
         '13.00 per cent', '1,63,410'],
        ['Margin as a percentage of contract value',
         'Total margin \u00f7 contract value', '\u2014', '13.00 per cent'],
    ], [3200, 4000, 1500, 1766], aligns=['l', 'l', 'r', 'r'])
    doc.after_table(0.4)
    para(
        'The client in this illustration has placed collateral of Rs. 1,75,000, '
        'which is comfortably above the requirement at entry. Table 2.23 '
        'shows what happens if the underlying falls to Rs. 1,232.00, a fall of '
        '1.99 per cent.')
    doc.table_title('Table 2.23: Margin shortfall and square-off scenario '
             '(illustrative)')
    doc.table([
        ['Step', 'Computation', 'Amount (Rs.)'],
        ['Collateral placed by the client', 'Given', '1,75,000'],
        ['Margin required at entry', 'From Table 2.22', '1,63,410'],
        ['Surplus at entry', '1,75,000 \u2212 1,63,410', '11,590'],
        ['Mark-to-market loss on the fall to Rs. 1,232.00',
         '(1,232.00 \u2212 1,257.00) \u00d7 1,000', '(25,000)'],
        ['Collateral after the loss is debited', '1,75,000 \u2212 25,000',
         '1,50,000'],
        ['Margin required at the lower price',
         '1,232.00 \u00d7 1,000 \u00d7 13.00 per cent', '1,60,160'],
        ['Shortfall', '1,60,160 \u2212 1,50,000', '10,160'],
    ], [4400, 3800, 2266], aligns=['l', 'l', 'r'])
    doc.after_table(0.4)
    para(
        'At entry the client held a surplus of Rs. 11,590 over a requirement '
        'of Rs. 1,63,410, which looks comfortable. A fall of 1.99 per cent in '
        'the underlying converts that surplus into a shortfall of Rs. 10,160. '
        'The reason is an asymmetry that every new dealer has to understand: '
        'the mark-to-market loss is debited from the collateral in full, while '
        'the requirement falls only slightly, from Rs. 1,63,410 to '
        'Rs. 1,60,160, because the requirement is itself computed on a '
        'contract value that has fallen. Collateral therefore declines faster '
        'than the margin requirement, and the gap widens as the adverse move '
        'continues. This is why the response to a margin alert is '
        'time-critical and why the desk is not permitted to grant an '
        'extension.')

    # ------------------------------------------------------------------ Q
    doc.para('Q.  Illustrative computation: transaction costs on a delivery '
             'and an intraday round trip', bold=True, align='left', before=160)
    para(
        'A trade that shows a profit before costs may show a loss after them. '
        'The first illustration is a delivery round trip of 100 shares bought '
        'and sold at Rs. 1,000 with brokerage at 0.05 per cent on each side.')
    doc.table_title('Table 2.24: Charge computation on an illustrative delivery '
             'round trip')
    doc.table([
        ['Charge', 'Rate applied', 'Base', 'Amount (Rs.)'],
        ['Buy value', '100 shares \u00d7 Rs. 1,000', '\u2014', '1,00,000'],
        ['Sell value', '100 shares \u00d7 Rs. 1,000', '\u2014', '1,00,000'],
        ['Brokerage', '0.05 per cent each side', 'Buy + sell value', '100.00'],
        ['Securities transaction tax', '0.10 per cent each side',
         'Buy + sell value', '200.00'],
        ['Exchange transaction charges', '0.00297 per cent',
         'Buy + sell value', '5.94'],
        ['SEBI turnover fee', '0.0001 per cent', 'Buy + sell value', '0.20'],
        ['Stamp duty', '0.015 per cent', 'Buy value only', '15.00'],
        ['Goods and services tax', '18 per cent',
         'Brokerage + exchange charges + SEBI fee', '19.11'],
        ['Total charges', '\u2014', '\u2014', '340.25'],
        ['Break-even move required per share',
         'Total charges \u00f7 100 shares', '\u2014', 'Rs. 3.40'],
    ], [2900, 2900, 3200, 1466], aligns=['l', 'l', 'l', 'r'])
    doc.after_table(0.4)
    para(
        'The second illustration is an intraday trade of Rs. 5,00,000 bought '
        'and Rs. 5,02,500 sold on the same day, at a flat brokerage of Rs. 20 '
        'for each executed order.')
    doc.table_title('Table 2.25: Charge computation on an illustrative intraday trade')
    doc.table([
        ['Charge', 'Rate applied', 'Base', 'Amount (Rs.)'],
        ['Brokerage', 'Rs. 20 per executed order, two orders', '\u2014',
         '40.00'],
        ['Securities transaction tax', '0.025 per cent', 'Sell value only',
         '125.62'],
        ['Exchange transaction charges', '0.00297 per cent',
         'Buy + sell value', '29.77'],
        ['SEBI turnover fee', '0.0001 per cent', 'Buy + sell value', '1.00'],
        ['Stamp duty', '0.003 per cent', 'Buy value only', '15.00'],
        ['Goods and services tax', '18 per cent',
         'Brokerage + exchange charges + SEBI fee', '12.74'],
        ['Total charges', '\u2014', '\u2014', '224.14'],
        ['Gross profit on the trade', '5,02,500 \u2212 5,00,000', '\u2014',
         '2,500.00'],
        ['Net profit after charges', '2,500.00 \u2212 224.14', '\u2014',
         '2,275.86'],
        ['Charges as a percentage of gross profit',
         '224.14 \u00f7 2,500.00', '\u2014', '8.97 per cent'],
    ], [2900, 2900, 3200, 1466], aligns=['l', 'l', 'l', 'r'])
    doc.after_table(0.4)
    fig('fig2_3', 5.8, 2.8, before=120, after=70)
    doc.caption('Figure 2.3: Composition of the charges on the illustrative '
             'delivery round trip')
    para(
        'On the delivery round trip the total cost of Rs. 340.25 requires the '
        'share to move Rs. 3.40, or about 0.34 per cent, before the client is '
        'even. The securities transaction tax of Rs. 200.00 is twice the '
        'brokerage of Rs. 100.00, so the statutory component rather than the '
        'firm\u2019s charge is the larger part of the cost. On the intraday '
        'trade the charges of Rs. 224.14 absorb 8.97 per cent of a gross '
        'profit of Rs. 2,500. The lesson that follows is that the frequency of '
        'trading, rather than the size of any single trade, determines what a '
        'client pays in total.')

    # ------------------------------------------------------------------ R
    doc.para('R.  Learning outcomes from the internship', bold=True,
             align='left', before=160)
    para(
        'The internship produced four durable outcomes. The first is an '
        'operational understanding of the Indian secondary market that runs '
        'from a client instruction to a settled credit in the demat account, '
        'including the points at which the process can fail. The second is the '
        'ability to compute, rather than describe, the quantities that govern '
        'a dealing decision: the fair value of a futures contract, a '
        'mark-to-market obligation, an option premium and its sensitivities, a '
        'margin requirement and the ladder of statutory charges. The third is '
        'familiarity with the two trading technologies in use on an Indian '
        'dealing desk, the exchange terminal and the member\u2019s '
        'Computer-to-Computer Link facility, and with the difference between '
        'the two in practice. The fourth is the discipline of sourcing: every '
        'regulatory statement in this report carries the authority on which it '
        'rests and the date on which it was checked, and every figure is '
        'identified as reported, computed or illustrative.')
    para(
        'The wider conclusion drawn from the operational part of the '
        'internship is that the competence expected of an equity dealer is not '
        'the ability to form a view on a security. It is the ability to '
        'execute an instruction correctly within a dense framework of limits, '
        'timings and statutory obligations, and to recognise immediately when '
        'that framework has been breached. The attributes that determine how a '
        'security should be traded, such as its price band, its depth and its '
        'volatility, are almost entirely separate from the attributes that '
        'determine whether the company behind it is a sound business, which is '
        'the question addressed in the second half of this report.')
