# -*- coding: utf-8 -*-
"""Chapters 1 to 4 of the report."""

from docgen import Doc, BODY_SIZE


def chapter_1(doc, fig=None):
    doc.new_page()
    doc.para('CHAPTER 1 :- INTRODUCTION', bold=True, align='left')
    doc.mark('CHAPTER 1 :- INTRODUCTION', 1)
    doc.heading('1.1 NEED OF THE STUDY', 2, '   1.1 Need of the Study')
    for b in [
        'To gain exposure to the corporate world and to the working of a live '
        'stock broking operation, in which a client instruction becomes a '
        'settled transaction within a fixed cycle of time.',
        'To understand the Indian secondary market from the inside, covering '
        'the trading mechanism, the two trading technologies used on a dealing '
        'desk, the margining framework and the settlement cycle, rather than '
        'only from a textbook description.',
        'To understand the futures and options segment, which now accounts for '
        'the larger part of turnover on Indian exchanges but receives limited '
        'practical attention in the classroom, and to compute for myself the '
        'quantities that govern a derivative transaction: contract value, '
        'margin, daily settlement, option premium and option sensitivities.',
        'To understand the fast-moving consumer goods sector fundamentally, '
        'including its importance to the economy, its growth drivers, its '
        'structural advantages and its challenges, and to relate the sector to '
        'current macroeconomic conditions in India.',
        'To apply financial statement analysis and ratio analysis to selected '
        'FMCG companies of the Indian listed universe and to interpret the '
        'results rather than merely compute them.',
        'To study how economic changes, inflation, interest rates and '
        'regulatory decisions affect a defensive consumption sector and the '
        'companies within it.',
        'To compare the financial performance of three leading FMCG companies '
        'over three financial years and to identify the company that performs '
        'relatively better on the selected ratios.',
        'To develop the discipline of sourcing every figure to a verifiable '
        'document and of separating reported figures from computed figures.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)

    doc.heading('1.2 OBJECTIVES OF THE STUDY', 2, '   1.2 Objectives of the Study')
    doc.para('The objectives of the study are stated below.', align='both')
    for b in [
        'To study the changes that the organisation has undergone or initiated '
        'in the recent past, and to understand the organisational context in '
        'which the internship was undertaken.',
        'To study the structure of the Indian capital market, the principal '
        'exchanges, the market participants and the regulatory framework '
        'administered by the Securities and Exchange Board of India.',
        'To study the equity trading mechanism, the order life cycle, the '
        'clearing and settlement process and the role of the depositories.',
        'To study the futures and options market, including contract '
        'specification, pricing by cost of carry, daily mark-to-market '
        'settlement, option payoff, premium decomposition and the computation '
        'of option sensitivities.',
        'To study the trading terminals used on a dealing desk, comprising the '
        'exchange-provided terminal and the member\u2019s Computer-to-Computer '
        'Link facility, together with the pre-trade risk controls and audit '
        'obligations attaching to each.',
        'To study risk management on a dealing desk, including margin '
        'computation in both segments, client-wise limits, margin-shortfall '
        'identification and square-off discipline.',
        'To carry out a fundamental analysis of the Indian FMCG sector and a '
        'comparative financial analysis of three selected FMCG companies for '
        'the three financial years from FY2023-24 to FY2025-26.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)

    doc.heading('1.3 SCOPE OF THE STUDY', 2, '   1.3 Scope of the Study')
    doc.para(
        'This project will allow investors and students to refer to the '
        'performance of FMCG companies, their relative growth and their '
        'relative valuation, and to decide whether the sector deserves a place '
        'in a portfolio. The project is limited to the fundamental analysis of '
        'the selected FMCG companies for a given period; technical analysis, '
        'portfolio construction and other sectors of the Indian market are not '
        'considered.', align='both')
    doc.para(
        'The analytical scope covers the Indian FMCG sector as it stood in '
        'October 2026 and three listed companies \u2014 Hindustan Unilever '
        'Ltd., Britannia Industries Ltd. and Dabur India Ltd. \u2014 for the '
        'financial years FY2023-24, FY2024-25 and FY2025-26. The study uses '
        'consolidated financial statements so that the figures of the three '
        'companies are on a comparable basis, and it relies entirely on '
        'secondary data drawn from annual reports, exchange filings, '
        'regulatory publications and published financial information.',
        align='both')
    doc.para(
        'The operational scope of the internship, which forms the second part '
        'of the report, covers the cash and equity derivatives segments of the '
        'Indian secondary market as they operated during the internship '
        'period. Functionally it is the dealing desk and the processes '
        'immediately adjacent to it, namely risk management, back-office '
        'settlement and compliance. The currency, commodity and debt segments '
        'are outside the scope, as are portfolio management and investment '
        'advisory. Every firm-specific detail has been generalised in '
        'accordance with the confidentiality undertaking referred to in '
        'Chapter 4, and every trading example in this report is illustrative.',
        align='both')


def chapter_2(doc, fig=None):
    doc.new_page()
    doc.para('CHAPTER 2 :- ORGANIZATIONAL BACKGROUND', bold=True, align='left')
    doc.mark('CHAPTER 2 :- ORGANIZATIONAL BACKGROUND', 1)

    doc.heading('2.1 ORGANISATIONAL INTRODUCTION', 2,
                '   2.1 Organisational Introduction (Rosy Blue Securities '
                'Pvt. Ltd.)')
    doc.para('About the Firm', bold=True, align='left', before=120)
    doc.para(
        'Rosy Blue Securities Pvt. Ltd. is the organisation at which the '
        'summer internship was undertaken. The firm operates as a stock broker '
        'in the Indian securities market, which means that it is registered '
        'with the Securities and Exchange Board of India, holds membership of '
        'a recognised stock exchange and executes transactions in securities '
        'on behalf of clients for a brokerage commission. The firm is a '
        'private limited company incorporated under the Companies Act.',
        align='both')
    doc.para(
        'A broking firm of this type performs four functions that are '
        'separated for regulatory and control reasons. The dealing function '
        'receives and executes client orders. The risk management function '
        'sets and monitors client-wise exposure against collateral. The '
        'back-office function computes obligations, issues contract notes and '
        'reconciles the firm\u2019s records against those of the exchange and '
        'the depositories. The compliance function maintains client '
        'registration documents, unique client code mappings and regulatory '
        'filings. The intern was attached to the dealing function but '
        'interacted with the other three daily, because an instruction that '
        'fails a risk check, or a trade that is not reconciled at the close of '
        'the day, becomes an immediate problem for the desk.', align='both')
    doc.para(
        'The corporate particulars of the firm are a matter of public record '
        'with the Registrar of Companies, the Securities and Exchange Board of '
        'India and the exchanges. They have been left for completion from the '
        'firm\u2019s own certificates rather than reconstructed, because no '
        'identifier in the table below has been assumed by the author.',
        align='both')
    doc.para('Table 2.1: Registration and corporate particulars of the firm',
             bold=True, align='left', before=120)
    doc.table([
        ['Particular', 'Entry to be confirmed from the firm\u2019s records'],
        ['Name of the entity', 'Rosy Blue Securities Pvt. Ltd.'],
        ['Constitution', 'Private limited company incorporated under the '
                         'Companies Act, 2013'],
        ['Year of incorporation', '[ADD: year of incorporation]'],
        ['Registered office', '[ADD: registered office address]'],
        ['SEBI stock-broker registration', '[ADD: SEBI registration number, '
                                           'INZ format]'],
        ['Other SEBI registrations', '[ADD: research analyst / investment '
                                      'adviser / depository participant, if '
                                      'held]'],
        ['Exchange membership \u2014 NSE', '[ADD: member code and segments, if '
                                            'a member]'],
        ['Exchange membership \u2014 BSE', '[ADD: member code and segments, if '
                                            'a member]'],
        ['Segments dealt in', '[ADD: cash / equity derivatives / currency / '
                               'commodity]'],
        ['Clearing arrangement', '[ADD: self-clearing or through a named '
                                  'clearing member]'],
        ['Depository participation', '[ADD: CDSL / NSDL registration, or '
                                     '\u2018not a depository participant\u2019]'],
        ['Investor grievance channel', '[ADD: e-mail address and SCORES '
                                        'registration details]'],
    ], [3600, 6866], aligns=['l', 'l'])
    doc.after_table(0.4)
    doc.para(
        'The registration and membership profile determines the boundary of '
        'everything a dealer may lawfully do. A member registered only in the '
        'cash segment cannot accept a derivatives order however insistent the '
        'client; a firm that is not a depository participant must route demat '
        'instructions through a separate entity, which lengthens the '
        'settlement chain; and a firm that clears through another member '
        'rather than self-clearing faces an additional layer in the margin and '
        'collateral process. The table is therefore not an administrative '
        'formality but the first thing a new dealer should read, because it '
        'defines the permissible universe of instructions.', align='both')

    doc.heading('2.2 DIRECTORS AND KEY MANAGEMENT PERSONNEL', 2,
                '   2.2 Directors and Key Management Personnel')
    doc.para(
        'The management of a broking firm is organised around the separation '
        'of business development from risk acceptance. The board determines '
        'the risk appetite of the firm, the compliance officer is responsible '
        'for registration, reporting and surveillance, and the heads of the '
        'dealing, risk management and back-office functions are accountable '
        'for the daily operation of that framework. The particulars of the '
        'individuals holding these offices at Rosy Blue Securities Pvt. Ltd. '
        'are to be reproduced from the firm\u2019s records and from its '
        'annual filings.', align='both')
    doc.para('Table 2.2: Directors and key management personnel of the firm',
             bold=True, align='left', before=120)
    doc.table([
        ['Designation', 'Name and particulars'],
        ['Director', '[ADD: name of director]'],
        ['Director', '[ADD: name of director]'],
        ['Chief Executive Officer or Managing Director',
         '[ADD: name and designation]'],
        ['Compliance Officer', '[ADD: name, qualification and SEBI '
                                'registration, if any]'],
        ['Head of Dealing', '[ADD: name and designation of the reporting '
                             'senior for the dealing desk]'],
        ['Head of Risk Management', '[ADD: name and designation]'],
        ['Head of Back Office and Settlement', '[ADD: name and designation]'],
    ], [4200, 6266], aligns=['l', 'l'])
    doc.after_table(0.4)
    doc.para(
        'The intern reported to the head of the dealing function and worked '
        'under the supervision of a registered dealer. No names have been '
        'assumed in this chapter: every entry that is not a matter of public '
        'record has been marked for completion from the firm\u2019s own '
        'documents.', align='both')

    doc.heading('2.3 ARRAY OF SERVICES', 2, '   2.3 Array of Services')
    doc.para(
        'The service range of a retail-facing broking firm is set out below. '
        'The entries marked for confirmation should be verified against the '
        'firm\u2019s own service brochure and its exchange membership '
        'certificates before submission. [ADD: confirm the list of services '
        'actually offered by the firm and delete any that are not offered.]',
        align='both')
    doc.para('Secondary Market Broking', bold=True, align='left', before=120)
    doc.para(
        'Execution of buy and sell orders in the equity cash segment on behalf '
        'of registered clients, against brokerage charged on turnover or on a '
        'per-order basis, with contract notes issued for every executed trade '
        'and settlement through the clearing corporation.', align='both')
    doc.para('Derivatives Broking', bold=True, align='left', before=120)
    doc.para(
        'Execution in equity futures and options, subject to the client having '
        'completed the additional documentation required for the segment, '
        'having been assigned a unique client code valid for derivatives, and '
        'having placed the margin required for the position.', align='both')
    doc.para('Depository Services', bold=True, align='left', before=120)
    doc.para(
        'Holding of client securities in dematerialised form where the firm is '
        'a depository participant, together with pledge and re-pledge '
        'instructions for collateral, delivery instructions and corporate '
        'action processing.', align='both')
    doc.para('Research and Advisory', bold=True, align='left', before=120)
    doc.para(
        'Dissemination of research output and advisory communication, which '
        'may be undertaken only to the extent permitted by the firm\u2019s '
        'registration as a research analyst or investment adviser under the '
        'regulations of the Securities and Exchange Board of India.',
        align='both')
    doc.para('Client Servicing and Support', bold=True, align='left', before=120)
    doc.para(
        'Client registration and know-your-customer verification, ledger and '
        'holding statements, funds pay-in and pay-out, queries relating to '
        'contract notes and charges, and grievance redressal through the '
        'exchange and SEBI SCORES platform.', align='both')

    doc.heading('2.4 VISION', 2, '   2.4 Vision')
    doc.para(
        '[ADD: reproduce the firm\u2019s published vision statement here. If '
        'the firm does not publish one, delete this section and renumber the '
        'sections that follow, together with the corresponding entry in the '
        'index.]', align='both')

    doc.heading('2.5 MISSION', 2, '   2.5 Mission')
    doc.para(
        '[ADD: reproduce the firm\u2019s published mission statement here, on '
        'the same basis as the preceding section.]', align='both')

    doc.heading('2.6 DEPARTMENTS', 2, '   2.6 Departments')
    doc.para(
        'The functional departments of a broking firm and the way each of them '
        'touches the dealing desk are set out in Table 2.3. The table is '
        'written from the point of view of the desk, which is the reason the '
        'last column records the interaction rather than the internal '
        'hierarchy of the department concerned.', align='both')
    doc.para('Table 2.3: Departments of a broking firm and their principal '
             'functions', bold=True, align='left', before=120)
    doc.table([
        ['Department', 'Principal functions',
         'Interaction with the dealing desk'],
        ['Dealing desk', 'Receives client instructions, enters and modifies '
                         'orders, confirms executions and communicates fills '
                         'to clients', 'The function itself'],
        ['Risk management', 'Sets client-wise limits, monitors margin '
                            'utilisation, raises shortfall alerts and '
                            'authorises square-off',
         'Releases or blocks limits in real time during market hours'],
        ['Back office and settlement', 'Computes obligations, generates '
                                       'contract notes, maintains client '
                                       'ledgers, handles pay-in and pay-out',
         'Supplies opening ledger balances and resolves trade mismatches'],
        ['Compliance', 'Client registration, unique client code mapping, '
                       'surveillance responses, regulatory filings and '
                       'reporting',
         'Confirms that a client code is active and permitted in a segment'],
        ['Information technology', 'Terminal provisioning, connectivity, user '
                                   'and terminal identifiers, business '
                                   'continuity arrangements',
         'Restores terminal access and connectivity when a session fails'],
        ['Accounts and treasury', 'Client fund transfers, bank reconciliation, '
                                  'settlement funding and collateral placement',
         'Confirms receipt of client funds that release additional limit'],
    ], [2300, 4600, 3566], aligns=['l', 'l', 'l'])
    doc.after_table(0.4)
    doc.para(
        'The separation of the dealing function from the risk management '
        'function is the single most important control in this structure, '
        'because it prevents the person with an incentive to execute from also '
        'being the person who decides whether execution is affordable. A '
        'dealer therefore cannot increase a client\u2019s limit, and an '
        'instruction that exceeds it must be refused at the desk and escalated '
        'to risk management. During the internship this separation was the '
        'most frequent source of friction with clients and at the same time '
        'the most frequent source of protection for the firm.', align='both')

    doc.heading('2.7 JOB DESCRIPTION', 2, '   2.7 Job Description')
    doc.para(
        'The intern was attached to the equity dealing desk in the capacity of '
        'an Equity Dealer for the period [ADD: internship start date] to '
        '[ADD: internship end date], working [ADD: working hours] and '
        'reporting to the head of the dealing function. The segments handled '
        'were [ADD: cash / equity derivatives / both] and the client '
        'categories dealt with were [ADD: retail / high net-worth / '
        'sub-broker \u2014 categories only]. All order entry was carried out '
        'under the supervision of a registered dealer, and no instruction was '
        'executed without a recorded client instruction and a confirmed '
        'limit.', align='both')
    doc.para('The principal duties performed were the following.', align='both')
    for b in [
        'Receiving client instructions by telephone, confirming the security, '
        'quantity, price and validity of each instruction, and recording the '
        'instruction before entry.',
        'Entering, modifying and cancelling orders on the exchange-provided '
        'trading terminal and on the member\u2019s Computer-to-Computer Link '
        'facility.',
        'Verifying the tradable limit available to each client against the '
        'collateral and margin recorded by the risk management system before '
        'releasing an order.',
        'Monitoring open orders and executed positions during the session, and '
        'informing clients of the status of their instructions.',
        'Responding to margin-shortfall alerts by informing the client, '
        'recording the communication and escalating the matter to risk '
        'management for further action.',
        'Following the firm\u2019s intraday square-off discipline for '
        'positions that cannot be carried forward under the client\u2019s '
        'available limit.',
        'Verifying the day\u2019s executions against the trade book after the '
        'close of the session, and reconciling discrepancies with the '
        'back office the same evening.',
        'Checking contract notes and charge computations, and answering client '
        'queries on brokerage, statutory charges and settlement obligations.',
        'Maintaining the desk\u2019s daily records in the form required by the '
        'firm\u2019s compliance policy, including the record of instructions '
        'received by telephone.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)
    doc.para(
        'The responsibilities fell into three time bands, corresponding to the '
        'periods before, during and after the continuous trading session, and '
        'are set out in Table 2.4.', align='both')
    doc.para('Table 2.4: Indicative working day of an equity dealer',
             bold=True, align='left', before=120)
    doc.table([
        ['Time', 'Activity', 'Purpose'],
        ['08:45 \u2013 09:00', 'Review of overnight news, corporate actions, '
                               'the exchange ban list and pending client '
                               'instructions',
         'To identify scrips that require special handling before the session '
         'opens'],
        ['09:00 \u2013 09:07', 'Verification of client-wise limits and '
                               'collateral uploaded by the risk management '
                               'system',
         'To confirm the tradable limit available to each client for the day'],
        ['09:07 \u2013 09:15', 'Observation of the pre-open session and the '
                               'indicative equilibrium price',
         'To assess the likely opening level and to prepare the order queue'],
        ['09:15 \u2013 12:30', 'Continuous trading: order entry, modification '
                               'and cancellation; confirmation of fills to '
                               'clients',
         'Execution of client instructions within the limits available'],
        ['12:30 \u2013 14:30', 'Mid-session monitoring, response to risk '
                               'alerts and follow-up on margin top-ups',
         'To prevent a margin shortfall from becoming a forced square-off'],
        ['14:30 \u2013 15:30', 'Intraday square-off discipline, closing '
                               'instructions and end-of-session order review',
         'To close positions that cannot be carried forward under the '
         'client\u2019s limit'],
        ['15:30 \u2013 17:30', 'Verification of the day\u2019s executions '
                               'against the trade book, reconciliation with '
                               'the back office and contract-note review',
         'To ensure that the client\u2019s records and the firm\u2019s '
         'records agree'],
    ], [1900, 4700, 3866], aligns=['l', 'l', 'l'])
    doc.after_table(0.4)
    doc.para(
        'The shape of the day shows that only about six of the nine working '
        'hours fall inside the continuous trading session, and that much of a '
        'dealer\u2019s effort is expended before the market opens and after it '
        'closes. The pre-market block determines how much can safely be '
        'executed; the post-market block determines whether what was executed '
        'has been recorded correctly. Order entry is thus the visible part of '
        'a process that is predominantly preparation and verification.',
        align='both')
    doc.para('The principal tools used during the internship were the '
             'following.', align='both')
    for b in [
        'The exchange-provided trading terminal: used for the market watch, '
        'order entry, and review of the order book and the trade book.',
        'The member\u2019s Computer-to-Computer Link terminal: used for order '
        'routing through the firm\u2019s own server, with pre-trade risk '
        'controls applied before the order reaches the exchange. [ADD: name of '
        'the Computer-to-Computer Link software used by the firm.]',
        'The risk management system console: used to read client-wise limit '
        'utilisation, available margin and shortfall alerts.',
        'The telephone recording system: used for the receipt of client '
        'instructions, retained as evidence of the instruction in accordance '
        'with the firm\u2019s compliance policy.',
    ]:
        doc.para('\u2022  ' + b, align='both', indent_left=360, first_line=180)

    doc.heading('2.8 LEARNING ACTIVITIES FROM ORGANISATION', 2,
                '   2.8 Learning Activities from Organisation')
    _learning(doc, fig)


def _learning(doc, fig=None):
    para = lambda t, **kw: doc.para(t, align='both', **kw)
    para(
        'The learning activities undertaken during the internship are set out '
        'below in the order in which they became relevant on the desk: the '
        'structure of the market, the rules that govern it, the mechanics of '
        'trading and settlement, risk management, derivatives and their '
        'margining, the two trading technologies used on the desk, and the '
        'costs and controls attaching to every transaction. Each regulatory '
        'statement carries the authority relied upon and the date on which it '
        'was checked; where verification against a primary source could not be '
        'completed, the statement is marked to be verified.')

    doc.para('A.  The financial system and the capital market in India',
             bold=True, align='left', before=160)
    para(
        'The financial system is the arrangement of markets, institutions, '
        'instruments and services through which savings are transferred to '
        'productive use. The financial markets component divides into the '
        'money market, which deals in instruments of original maturity up to '
        'one year, and the capital market, which deals in longer-dated '
        'instruments including equity. The capital market in turn divides into '
        'the primary market, in which securities are issued for the first '
        'time, and the secondary market, in which existing securities change '
        'hands. A stock broker\u2019s dealing desk operates almost entirely in '
        'the secondary segment of the capital market, which is why that is the '
        'focus of this report.')
    para(
        'The distinction matters operationally. In the primary market the '
        'broker is a distribution channel and the applicant\u2019s funds are '
        'blocked rather than debited; in the secondary market the broker is an '
        'execution intermediary with settlement obligations to the clearing '
        'corporation that arise within a fixed number of days regardless of '
        'whether the client pays. That asymmetry is the origin of the margin '
        'framework described later in this section.')
    doc.para('Table 2.5: Primary market and secondary market compared',
             bold=True, align='left', before=120)
    doc.table([
        ['Basis', 'Primary market', 'Secondary market'],
        ['Nature of transaction', 'Issue of new securities',
         'Transfer of existing securities'],
        ['Recipient of funds', 'The issuing company', 'The selling investor'],
        ['Effect on company capital', 'Capital is raised',
         'No change in company capital'],
        ['Price determination', 'Book-building or fixed price',
         'Continuous order matching'],
        ['Frequency', 'Occasional, issue by issue',
         'Continuous on every trading day'],
        ['Role of the broker', 'Distribution and application support',
         'Execution of orders'],
        ['Principal document', 'Prospectus or offer document',
         'Contract note'],
        ['Typical settlement', 'On allotment and listing',
         'Rolling settlement cycle'],
    ], [3400, 3500, 3566], aligns=['l', 'l', 'l'])
    doc.after_table(0.4)
    para(
        'The comparison indicates why a dealer\u2019s risk exposure is '
        'concentrated in the secondary market. In the primary market the '
        'intermediary\u2019s obligation ends when the application is '
        'forwarded, whereas an executed secondary-market trade creates an '
        'irrevocable obligation to deliver securities or funds on a fixed '
        'date. A client who does not pay does not cancel that obligation; the '
        'member must settle and then recover. This is the reason the '
        'pre-trade limit check is applied before an order is released rather '
        'than after it is executed.')

    doc.para('B.  Stock exchanges, indices and market participants',
             bold=True, align='left', before=160)
    para(
        'A stock exchange is a recognised body that provides the trading '
        'platform, the rules of trading and the framework of surveillance for '
        'securities transactions. India\u2019s two principal exchanges are the '
        'National Stock Exchange of India Limited and BSE Limited. Both '
        'operate fully electronic, order-driven markets with anonymous order '
        'matching. Each exchange supports several segments, of which the '
        'capital market segment, dealing in equity shares, and the equity '
        'derivatives segment, dealing in futures and options on indices and '
        'individual securities, are relevant to this report.')
    para(
        'An index is a statistical measure of the aggregate price movement of '
        'a defined basket of securities, computed on a free-float '
        'market-capitalisation basis for the principal Indian benchmarks. The '
        'Nifty 50 comprises fifty companies on the National Stock Exchange and '
        'the S&P BSE Sensex thirty on the BSE. For a dealer, indices matter in '
        'three ways: they are the underlying for the most liquid derivative '
        'contracts, they are the benchmark against which a client judges '
        'performance, and index levels define the market-wide circuit '
        'breakers that halt trading after specified falls.')
    doc.para('Table 2.6: Market participants and their role',
             bold=True, align='left', before=120)
    doc.table([
        ['Participant', 'Role in the market',
         'Point of contact with the dealing desk'],
        ['Retail investor', 'Buys and sells securities for a personal account '
                            'in modest size',
         'Places orders by telephone or through the firm\u2019s platform'],
        ['Stock broker', 'Executes orders as an intermediary and is a member '
                         'of the exchange', 'The employer of the dealer'],
        ['Clearing member', 'Assumes responsibility for settlement of trades '
                            'with the clearing corporation',
         'Determines the collateral that the broker must place'],
        ['Clearing corporation', 'Acts as central counterparty, computes '
                                 'obligations and margins',
         'Sets the margin that constrains every client limit'],
        ['Depository and depository participant',
         'Holds securities in electronic form and effects transfers',
         'Delivers pay-out and processes pledge instructions'],
        ['Institutional investor', 'Foreign portfolio investors and mutual '
                                   'funds investing under registered '
                                   'categories and stated mandates',
         'Rarely a retail desk\u2019s client; drives market direction and '
         'volume'],
    ], [2600, 4300, 3566], aligns=['l', 'l', 'l'])
    doc.after_table(0.4)
    para(
        'The table shows that a dealer deals directly with only two of the '
        'categories listed and indirectly with the rest through the '
        'constraints they impose. The clearing corporation is the most '
        'consequential participant that the dealer never speaks to, because '
        'its margin computation determines the limit that the risk management '
        'system will grant, which in turn determines what the dealer may '
        'execute.')

    doc.para('C.  The regulatory framework', bold=True, align='left',
             before=160)
    para(
        'The framework is hierarchical. Statute confers power on the '
        'regulator, the regulator makes regulations and issues circulars, and '
        'the exchanges and clearing corporations issue operating rules '
        'consistent with them. Table 2.7 lists the principal instruments '
        'relevant to a dealing desk. For a dealer the binding instruction on '
        'any given day is usually the most recent circular rather than the '
        'parent regulation, and circulars change frequently.')
    doc.para('Table 2.7: Principal statutes and regulations governing stock '
             'broking', bold=True, align='left', before=120)
    doc.table([
        ['Instrument', 'Principal subject matter',
         'Relevance to the dealing desk'],
        ['Securities Contracts (Regulation) Act, 1956',
         'Recognition of stock exchanges and regulation of contracts in '
         'securities',
         'Establishes that trades must occur on a recognised exchange'],
        ['Securities and Exchange Board of India Act, 1992',
         'Constitution and powers of SEBI',
         'Source of the regulator\u2019s authority over brokers'],
        ['Depositories Act, 1996',
         'Dematerialisation and electronic transfer of securities',
         'Underlies demat delivery and pledge of collateral'],
        ['SEBI (Stock Brokers) Regulations, 1992',
         'Registration, conduct, records and obligations of stock brokers',
         'Governs client registration, contract notes and record keeping'],
        ['Exchange bye-laws, rules and regulations',
         'Trading parameters, member obligations and discipline',
         'The day-to-day operating rules of the terminal'],
        ['Clearing corporation regulations',
         'Margining, settlement, default and close-out',
         'Determines margin rates and settlement timelines'],
    ], [3000, 4000, 3466], aligns=['l', 'l', 'l'])
    doc.after_table(0.4)
    para(
        'One example shows how quickly the operating routine can change '
        'without any alteration of the parent framework. The expiry days of '
        'the equity derivatives contracts of the two exchanges were separated '
        'with effect from 1 September 2025, so that contracts of the National '
        'Stock Exchange expire on Tuesday and those of the BSE on Thursday. '
        'The statutory framework was unaltered, but a single circular changed '
        'the week of every derivatives desk in the country. A dealer handling '
        'clients on both exchanges now manages two distinct expiry routines in '
        'the same week. The position stated here is as at 9 October 2026 and '
        'should be reconfirmed against the current exchange circulars before '
        'the report is submitted.')

    doc.para('D.  The equity trading mechanism and the order life cycle',
             bold=True, align='left', before=160)
    para(
        'The Indian cash market is an order-driven market. Buyers and sellers '
        'submit orders to a central electronic order book and the '
        'exchange\u2019s matching engine pairs them according to price-time '
        'priority: the order offering the best price is matched first, and '
        'among orders at the same price the one entered earlier is matched '
        'first. There is no obligation on any participant to provide a two-way '
        'quote in most securities, which means liquidity is a function of '
        'participation rather than of designated market making.')
    para(
        'The trading day is divided into defined sessions. The pre-open '
        'session collects orders without matching them, determines a single '
        'equilibrium price at which the maximum quantity can trade, and '
        'executes at that price; it exists to reduce the volatility that '
        'follows an overnight accumulation of information. The continuous '
        'trading session then operates on price-time priority until the close, '
        'followed by a closing session in which the closing price is computed. '
        'Indicative timings are set out in Table 2.8; the precise timings are '
        'notified by the exchanges and should be confirmed against the current '
        'exchange notice.')
    doc.para('Table 2.8: Equity trading sessions and indicative timings',
             bold=True, align='left', before=120)
    doc.table([
        ['Session', 'Indicative timing', 'What happens'],
        ['Pre-open order collection', '09:00 \u2013 09:08',
         'Orders are entered, modified and cancelled; no matching takes place'],
        ['Pre-open price determination', '09:08 \u2013 09:12',
         'The equilibrium price is computed and orders are matched at that '
         'price'],
        ['Continuous trading', '09:15 \u2013 15:30',
         'Order-driven matching on price-time priority'],
        ['Closing session', '15:30 \u2013 15:40',
         'The closing price is computed and the session closes'],
        ['Post-close session', '15:40 onwards',
         'Orders at the closing price are accepted for a limited period'],
    ], [2800, 2400, 5266], aligns=['l', 'l', 'l'])
    doc.after_table(0.4)
    para(
        'The order types available to a dealer, and the situation on the desk '
        'in which each was used during the internship, are set out in Table '
        '2.9. [ADD: confirm the order types actually used and delete any that '
        'were not.]')
    doc.para('Table 2.9: Order types and the situation calling for each',
             bold=True, align='left', before=120)
    doc.table([
        ['Order type', 'Validity', 'Situation in which it was used'],
        ['Limit order', 'Day',
         'The standard instruction where the client specifies a price'],
        ['Market order', 'Immediate',
         'Used only in liquid scrips where execution certainty was required'],
        ['Stop-loss limit order', 'Day',
         'To cap the loss on a carried position at a defined level'],
        ['Stop-loss market order', 'Day',
         'Where exit was required irrespective of the price obtained'],
        ['Immediate-or-cancel order', 'Immediate',
         'To avoid leaving a resting order in a fast market'],
        ['Disclosed quantity order', 'Day',
         'On larger orders, to limit visible size and market impact'],
    ], [3000, 2000, 5466], aligns=['l', 'l', 'l'])
    doc.after_table(0.4)
    para(
        'The order passes through a defined sequence of states. Each change of '
        'state either narrows or closes the dealer\u2019s discretion, and the '
        'whole of a dealer\u2019s judgement therefore lies between acceptance '
        'and execution.')
    doc.para('Table 2.10: Order states from entry to trade confirmation',
             bold=True, align='left', before=120)
    doc.table([
        ['State', 'What has happened', 'What the dealer can still do'],
        ['Instruction received', 'The client instruction has been captured and '
                                 'recorded',
         'Clarify quantity, price and validity before entry'],
        ['Risk-checked', 'The member\u2019s pre-trade controls have been '
                          'applied at the server',
         'Escalate to risk management if the order is rejected'],
        ['Accepted', 'The exchange has acknowledged the order and allotted an '
                     'order number', 'Modify or cancel the order'],
        ['Open', 'The order is resting in the book awaiting a counterparty',
         'Modify the price or quantity, or cancel'],
        ['Executed', 'The full quantity has traded and appears in the trade '
                     'book', 'Nothing; the trade is irrevocable'],
        ['Cancelled', 'The order was withdrawn before execution',
         'Re-enter if the client so instructs'],
        ['Rejected', 'The order failed a validation at the member or exchange '
                     'level', 'Correct the parameter or obtain the limit'],
    ], [2400, 4400, 3666], aligns=['l', 'l', 'l'])
    doc.after_table(0.4)
    para(
        'The sequence shows that a dealer\u2019s discretion is confined to a '
        'narrow window. Before acceptance the order is governed by validation '
        'rules, and after execution it is irrevocable, so the whole of a '
        'dealer\u2019s judgement lies in deciding what to enter and whether to '
        'modify a resting order. This is why the choice of order type is '
        'treated on the desk as a risk decision rather than a convenience.')

    doc.para('E.  Clearing, settlement and the depositories', bold=True,
             align='left', before=160)
    para(
        'Clearing is the process of computing what each member must deliver '
        'and receive; settlement is the process of actually delivering the '
        'securities and the funds. The clearing corporation interposes itself '
        'between the buyer and the seller and becomes the central counterparty '
        'to every trade, which is what allows anonymous matching to work: a '
        'member need not assess the credit of the member on the other side, '
        'only that of the clearing corporation. Obligations are netted, so a '
        'member that has both bought and sold the same security on the same '
        'day settles only the net quantity.')
    para(
        'Indian equity settlement operates on a rolling cycle. Under the T+1 '
        'cycle that applies to the cash segment, a trade executed on day T is '
        'settled on the next business day. The timeline is set out in Table '
        '2.11. The compression of the cycle is one of the reasons the '
        'operational discipline of the desk matters: there is no window in '
        'which a shortfall can be corrected by waiting.')
    doc.para('Table 2.11: Rolling settlement timeline under the T+1 cycle',
             bold=True, align='left', before=120)
    doc.table([
        ['Stage', 'Day', 'What happens'],
        ['Trade day', 'T',
         'The trade is executed and reported; obligations are recorded'],
        ['Confirmation and obligation', 'T (evening)',
         'The clearing corporation computes and downloads the obligations of '
         'each member'],
        ['Pay-in', 'T+1',
         'The member delivers securities to the clearing corporation by the '
         'stipulated time'],
        ['Pay-out', 'T+1',
         'The clearing corporation delivers securities and funds to the '
         'receiving member'],
        ['Funds settlement', 'T+1',
         'The client\u2019s ledger is adjusted and the net obligation is '
         'settled'],
    ], [3000, 2200, 5266], aligns=['l', 'l', 'l'])
    doc.after_table(0.4)
    para(
        'Securities are held in electronic form with a depository, either the '
        'Central Depository Services (India) Limited or the National '
        'Securities Depository Limited. A member that is also a depository '
        'participant can execute delivery instructions on behalf of its '
        'clients; a member that is not must route them through a separate '
        'participant. This distinction was the first entry a new dealer had to '
        'learn from the registration table of the firm, because it determines '
        'the length of the delivery chain and the point at which a delivery '
        'instruction can fail.')

    doc.para('F.  Risk management in the cash market and in the derivatives '
             'segment', bold=True, align='left', before=160)
    para(
        'Risk management in the Indian market operates on an upfront basis. '
        'The margin required for a position must be available before the order '
        'is released, and the requirement is computed by the clearing '
        'corporation and passed to the member, who passes it to the client. '
        'The principal constituents of margin in each segment are set out in '
        'Table 2.12. The rates themselves change and are notified by the '
        'exchange and the clearing corporation; the percentages shown are '
        'indicative and marked to be verified.')
    doc.para('Table 2.12: Principal components of margin by segment',
             bold=True, align='left', before=120)
    doc.table([
        ['Segment', 'Component', 'What it covers'],
        ['Cash market', 'Value at risk (VaR) margin',
         'Statistical loss that the position could suffer over a defined '
         'horizon at a defined confidence level'],
        ['Cash market', 'Extreme loss margin',
         'Additional cover against a loss beyond the value-at-risk estimate'],
        ['Cash market', 'Mark-to-market margin',
         'The notional loss on an open position, recomputed during the day'],
        ['Cash market', 'Delivery margin',
         'Cover against the risk of failure to deliver or pay on the '
         'settlement date'],
        ['Equity derivatives', 'SPAN margin',
         'A portfolio-based computation that stresses the portfolio across a '
         'range of prices and volatility scenarios'],
        ['Equity derivatives', 'Exposure margin',
         'A percentage of the notional contract value, charged in addition to '
         'the SPAN margin'],
        ['Equity derivatives', 'Mark-to-market settlement',
         'The daily cash settlement of the gain or loss on every open '
         'position'],
        ['Both segments', 'Peak margin reporting',
         'Reporting of the highest intraday margin requirement to the '
         'clearing corporation'],
    ], [2200, 3000, 5266], aligns=['l', 'l', 'l'])
    doc.after_table(0.4)
    para(
        'Two consequences follow from an upfront regime, and both were '
        'observed during the internship. First, the limit a client may use is '
        'determined by the collateral actually pledged and available, not by '
        'the client\u2019s standing. A dealer can therefore no longer '
        'accommodate a reliable client informally, and the absence of that '
        'discretion removes a large part of the discretion the role once had. '
        'Second, because the collateral is marked to market while the margin '
        'requirement changes with the position, collateral can fall faster '
        'than the requirement, turning a surplus into a shortfall without any '
        'trade being executed. This mechanism is worked through numerically '
        'later in this report.')

    doc.para('G.  The futures and options market', bold=True, align='left',
             before=160)
    para(
        'A derivative is a contract whose value is derived from an underlying '
        'asset. The two instruments relevant to an equity dealing desk are '
        'futures, which are obligations to buy or sell at a future date at a '
        'price agreed today, and options, which are rights rather than '
        'obligations and for which the buyer pays a premium. The distinction '
        'matters to a client because a futures position has symmetric exposure '
        'and no cost of entry beyond the margin, while an option has '
        'asymmetric exposure and a cost that is paid whether or not the option '
        'is exercised.')
    para(
        'Index futures are the most liquid contracts on the Indian exchanges '
        'and are quoted at a premium or discount to the spot index. That '
        'difference, called the basis, is explained by the cost of carrying '
        'the underlying position to expiry, comprising the cost of funds and '
        'the dividends receivable, less the convenience of holding the '
        'underlying itself. The relationship is:')
    doc.para('F = S \u00d7 (1 + r \u2212 d)^T, where F is the fair futures '
             'price, S the spot price, r the cost of funds, d the dividend '
             'yield and T the time to expiry expressed in years.',
             bold=True, align='center', before=120, after=120)
    para(
        'A dealer uses this relationship in two ways. A price materially above '
        'fair value creates a cash-and-carry opportunity, in which the '
        'underlying is bought and the futures sold, and a price materially '
        'below fair value creates the reverse. Neither is usually actionable '
        'for a retail client after transaction costs, but both explain why the '
        'basis narrows as expiry approaches and why it widens when the cost of '
        'funds rises.')
    para(
        'Every futures position is settled daily rather than at expiry alone. '
        'The difference between the previous settlement price and the current '
        'settlement price is credited to, or debited from, the margin account '
        'of the position holder at the close of each session. Daily settlement '
        'does not change the total result of a position held to expiry, but it '
        'changes when the cash flows occur, and it is the reason a client with '
        'a profitable position can still be required to pay money on a '
        'particular day. The mechanics are demonstrated numerically in the '
        'analysis chapter.')
    para(
        'Option premiums decompose into intrinsic value and time value. The '
        'intrinsic value of a call is the amount by which the spot price '
        'exceeds the strike; the remainder of the premium is time value, which '
        'decays as expiry approaches and decays fastest in the final days. '
        'The rate of change of the premium with respect to each of the '
        'principal inputs is measured by the option sensitivities, or Greeks: '
        'delta for the underlying price, gamma for the rate of change of '
        'delta, theta for the passage of time, vega for the change in '
        'volatility and rho for the change in the rate of interest. For a '
        'dealer the practical importance of these quantities is that they '
        'explain why a client\u2019s position can lose value while the '
        'underlying price has not moved in the adverse direction, which is by '
        'far the most common misunderstanding encountered on the desk.')

    doc.para('H.  The trading terminals used on the desk', bold=True,
             align='left', before=160)
    para(
        'Two trading technologies are used on a dealing desk. The first is the '
        'terminal provided by the exchange, on which orders are entered '
        'directly into the exchange\u2019s trading system under the '
        'member\u2019s credentials. The second is the member\u2019s own '
        'Computer-to-Computer Link facility, under which orders are entered '
        'into the member\u2019s server and routed to the exchange from there, '
        'with the member\u2019s own pre-trade risk controls applied on the way. '
        'The two are compared in Table 2.13.')
    doc.para('Table 2.13: The exchange terminal and the Computer-to-Computer '
             'Link facility compared', bold=True, align='left', before=120)
    doc.table([
        ['Basis of comparison', 'Exchange-provided terminal',
         'Computer-to-Computer Link facility'],
        ['Where the order is entered', 'Directly into the exchange trading '
                                        'system',
         'Into the member\u2019s server, which routes it to the exchange'],
        ['Point of risk control', 'Exchange validations only',
         'Member-level pre-trade checks before the order leaves the server, '
         'followed by exchange validations'],
        ['Identification', 'User identifier issued by the exchange',
         'User and terminal identifiers issued by the member and registered '
         'with the exchange'],
        ['Software approval', 'Provided by the exchange',
         'Software must be approved by the exchange and the configuration '
         'registered'],
        ['Flexibility', 'Limited to the functions offered by the exchange',
         'Can be integrated with the member\u2019s risk and ledger systems'],
        ['Typical use on the desk', 'Standard order entry and market watch',
         'High-volume desks and clients needing immediate limit updates'],
    ], [2800, 3700, 3966], aligns=['l', 'l', 'l'])
    doc.after_table(0.4)
    para(
        'The audit obligation attaching to the Computer-to-Computer Link '
        'facility is greater, because the member is responsible for the '
        'controls applied to orders before they reach the exchange. Every '
        'order must be capable of being traced to a specific user and terminal '
        'identifier, and the records must be retained and produced on demand. '
        'Six of the eight pre-trade checks observed on the desk tested the '
        'client\u2019s standing rather than the parameters of the order, which '
        'is a statement about what the facility actually is: a credit control '
        'that happens to be a trading terminal, rather than a trading terminal '
        'that happens to have controls.')

    doc.para('I.  Transaction costs and statutory charges', bold=True,
             align='left', before=160)
    para(
        'Every executed trade attracts a ladder of charges which, taken '
        'together, determine whether a nominally profitable transaction is in '
        'fact profitable. The components are set out in Table 2.14. The rates '
        'are notified by the Government, the regulator and the exchanges and '
        'change from time to time; the percentages and amounts shown below are '
        'the rates applied during the internship and are marked to be '
        'reconfirmed before submission.')
    doc.para('Table 2.14: Statutory charges and transaction costs on a trade',
             bold=True, align='left', before=120)
    doc.table([
        ['Component', 'Levied on', 'Borne by', 'Nature'],
        ['Brokerage', 'Turnover of the trade', 'Client',
         'Firm\u2019s charge; negotiable and disclosed in the tariff sheet'],
        ['Securities transaction tax', 'Turnover of the trade', 'Client',
         'Statutory; rates differ between delivery and intraday, and between '
         'the two segments'],
        ['Exchange transaction charge', 'Turnover of the trade', 'Client',
         'Statutory; charged by the exchange and passed on'],
        ['SEBI turnover fee', 'Turnover of the trade', 'Client',
         'Statutory; a small fraction of turnover'],
        ['Stamp duty', 'Turnover of the trade', 'Client',
         'State levy; collected by the exchange and paid to the state'],
        ['Goods and services tax', 'Brokerage and transaction charges',
         'Client', 'Statutory; levied at the prescribed rate on the service '
                   'component'],
        ['Securities and Exchange Board of India investor protection fund',
         'Turnover of the trade', 'Client',
         'Statutory; credited to the investor protection fund'],
    ], [3000, 2500, 1400, 3566], aligns=['l', 'l', 'l', 'l'])
    doc.after_table(0.4)
    para(
        'The practical significance of the ladder is that the break-even move '
        'required on a round trip is larger than most clients assume, and that '
        'the difference between delivery and intraday is material. The '
        'computation is worked through on two illustrative transactions in '
        'Section 2.8, sub-section Q.')

    doc.para('J.  Investor protection, compliance and surveillance',
             bold=True, align='left', before=160)
    para(
        'Investor protection in the Indian market operates through '
        'registration, disclosure, segregation of client funds, and '
        'surveillance. A client\u2019s funds and securities must be kept '
        'separate from those of the member, and the member must report the '
        'balances held. Every client must be assigned a unique client code '
        'that is used consistently across exchanges, so that the activity of a '
        'person cannot be split across identifiers. Surveillance is conducted '
        'by the exchanges and by the regulator, and its main effect on the '
        'desk is through the imposition of additional margins, price bands and '
        'restrictions on the securities under surveillance. Table 2.15 sets '
        'out the principal frameworks and their operational effect.')
    doc.para('Table 2.15: Surveillance frameworks and their effect on trading',
             bold=True, align='left', before=120)
    doc.table([
        ['Framework', 'What it covers', 'Effect at the dealing desk'],
        ['Price bands', 'A permitted range of price movement around the '
                        'previous closing price',
         'Orders outside the band are rejected; a security may have a wider or '
         'narrower band depending on its category'],
        ['Graded surveillance measure', 'Securities showing unusual price or '
                                        'volume behaviour',
         'Additional margin and, at higher stages, restriction of intraday '
         'trading and of derivative positions'],
        ['Additional surveillance measure',
         'Securities with specific market-integrity concerns',
         'Higher margin and trade-for-trade settlement in some cases'],
        ['Periodic call auction', 'Securities with limited liquidity',
         'Trading only in defined call auction windows rather than '
         'continuously'],
        ['Ban on fresh derivative positions',
         'Contracts in which open interest has crossed the prescribed limit',
         'Only positions reducing exposure may be taken in that contract'],
    ], [3000, 3800, 3666], aligns=['l', 'l', 'l'])
    doc.after_table(0.4)
    para(
        'The operational lesson from this part of the learning is that the '
        'status of a security is not a fixed property. A scrip can move '
        'between categories between one session and the next, and the pre-'
        'market check of the exchange\u2019s daily list of securities under '
        'surveillance is therefore not a formality but a requirement that '
        'changes what can lawfully be offered to a client on that day.')

    # The worked examples prepared on the desk during the internship, and the
    # learning outcomes drawn from them, complete the learning section.
    from content_examples import examples
    examples(doc, fig)
