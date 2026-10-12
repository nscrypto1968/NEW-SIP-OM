# -*- coding: utf-8 -*-
"""Driver: assemble the report, generate the charts, and write the .docx.

Usage:  python3 render.py [output.docx]
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from docgen import Doc, FRAME_W, LINE, CAPACITY          # noqa: E402
import figures                                            # noqa: E402
import pack                                               # noqa: E402

from content_front import (title_page, certificate, declaration,           # noqa: E402
                           acknowledgement, executive_summary)
from content_ch1_4 import chapter_1, chapter_2                             # noqa: E402
from content_ch3_4 import chapter_3, chapter_4                             # noqa: E402
from content_ch5 import chapter_5                                          # noqa: E402
from content_ch6 import chapter_6                                          # noqa: E402
from content_ch7 import chapter_7                                          # noqa: E402
from references import references                                          # noqa: E402
from appendix import appendix                                              # noqa: E402

TEMPLATE = '/tmp/ref/x/word'
ASSETS = os.path.join(HERE, 'assets')
OUT = os.path.join(os.path.dirname(HERE),
                   'Fundamental Analysis of the FMCG Sector - SIP Research '
                   'Report.docx')


class Media(object):
    """Collects the image files and hands out relationship ids."""

    def __init__(self):
        self.items = []          # (rid, filename, bytes)
        self.by_name = {}
        self.next_rid = 200

    def __contains__(self, key):
        return key in self.by_name

    def __getitem__(self, key):
        return self.by_name[key]

    def add_file(self, name, path, key=None):
        key = key or name
        if key in self.by_name:
            return self.by_name[key]
        with open(path, 'rb') as fh:
            data = fh.read()
        fname = name + os.path.splitext(path)[1]
        rid = 'rId%d' % self.next_rid
        self.next_rid += 1
        self.items.append((rid, fname, data))
        self.by_name[key] = rid
        return rid


def make_figure_adder(doc, media):
    def fig(name, width_pt, height_pt, before=120, after=60):
        rid = media.by_name.get(name)
        if rid is None:
            path = os.path.join(figures.OUT, name + '.png')
            if not os.path.exists(path):
                raise SystemExit('missing chart: ' + path)
            rid = media.add_file(name, path)
        return doc.image(rid, width_pt, height_pt, before=before, after=after)
    return fig


def check_tables(doc, problems):
    """Wrap Doc.table so that any mis-sized table is reported."""
    original = doc.table

    def guarded(rows, widths, **kw):
        if sum(widths) not in (FRAME_W, 10456):
            problems.append('table width %d (expected %d) in row %r'
                            % (sum(widths), FRAME_W,
                               (rows[0][0] if rows else '')[:40]))
        return original(rows, widths, **kw)
    doc.table = guarded


def index_rows(labels, numbers, pages, front, index_span=None):
    """Rows of the index table.

    ``labels`` fixes the structure (chapter and sub-section titles in order);
    ``numbers`` supplies the page numbers, which are blank on the first pass
    so that the table occupies the same space before and after they are
    filled in.
    """
    def pg(value):
        if numbers is None or value is None:
            return ''
        return str(value)

    pages_by_label = {}
    if numbers:
        for lv, label, page in numbers:
            pages_by_label[(lv, label)] = page

    rows = [['CHAPTER NO.', 'CHAPTER TITLE / SUB-SECTION', 'PAGE NO.']]
    bold = set()
    for label, page in front:
        rows.append(['', label, pg(page)])
    if index_span is not None:
        span = ('%s-%s' % (pg(index_span[0]), pg(index_span[1])))
    else:
        span = ''
    rows.append(['', 'TABLE OF CONTENTS', span])

    levels = [i for i, (lv, _) in enumerate(labels) if lv == 1]
    for pos, i in enumerate(levels):
        label = labels[i][1]
        start = pages_by_label.get((1, label))
        end = None
        if pos + 1 < len(levels):
            nxt = pages_by_label.get((1, labels[levels[pos + 1]][1]),
                                     pages + 1)
            if nxt is not None:
                end = nxt - 1
        if end is None:
            end = pages
        if label.startswith('CHAPTER'):
            first_col = 'CHAPTER ' + label.split(' ')[1]
            title = label.split(':-', 1)[1].strip()
        elif label.startswith('APPENDICES'):
            first_col = 'APPENDICES'
            title = ('HINDUSTAN UNILEVER LTD. \u2013 COMPANY RESEARCH '
                     'REPORT')
        else:
            first_col = ''
            title = label
        span = '%s-%s' % (pg(start), pg(end)) if start is not None else ''
        bold.add(len(rows))
        rows.append([first_col, title, span])
        for j in range(i + 1, len(labels)):
            lv, sub = labels[j]
            if lv == 1:
                break
            rows.append(['', sub.strip(),
                         pg(pages_by_label.get((2, sub)))])
    return rows, bold


def build(media, index_labels=None, index_numbers=None, collect=None,
          total_pages=None, index_span=None):
    """One complete pass over the document.

    ``index_labels`` is ``None`` when the index is to be omitted, which is how
    the first pass discovers the structure of the report; otherwise it is the
    toc list collected by an earlier pass.
    """
    doc = Doc()
    problems = []
    check_tables(doc, problems)
    fig = make_figure_adder(doc, media)

    front_pages = []
    title_page(doc, media)
    front_pages.append(('TITLE PAGE', doc.page))

    def front(name, fn):
        """Run a preliminary page and record the page it opens on.

        Every one of these sections begins with a page break, so the page it
        appears on is the page the document is on just before the break plus
        one -- *not* the page reached after the section has been laid out,
        which would be wrong whenever a section runs to more than one page.
        """
        before = doc.page
        fn(doc)
        front_pages.append((name, before + 1))

    front('CERTIFICATION', lambda d: certificate(d, media))
    front('DECLARATION', declaration)
    front('ACKNOWLEDGEMENT', acknowledgement)
    front('EXECUTIVE SUMMARY', executive_summary)

    # the index itself
    index_page = index_end = doc.page
    if index_labels is not None:
        doc.new_page()
        index_page = doc.page
        doc.para('INDEX', size=14.0, bold=True, align='center',
                 underline=True, tab_stops=[4364], after=0, keep_next=True)
        rows, bold = index_rows(index_labels, index_numbers,
                                total_pages or 0, front_pages, index_span)
        doc.table(rows, [1750, 6508, 2198], aligns=['l', 'l', 'c'],
                  border_color='auto', border_sz=4, head_fill=None,
                  cell_before=200, cell_after=120, cell_keep_next=True,
                  head_height=800, table_pos=True, bold_rows=bold)
        doc.after_table(0.3)
        index_end = doc.page

    chapter_1(doc, fig)
    chapter_2(doc, fig)
    chapter_3(doc, fig)
    chapter_4(doc)
    chapter_5(doc, fig)
    chapter_6(doc, fig)
    chapter_7(doc, fig)
    references(doc)
    appendix(doc, fig)

    if collect is not None:
        collect.append(dict(pages=doc.page, index=(index_page, index_end),
                            front=front_pages, toc=list(doc.toc),
                            problems=problems))
    return doc, media


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else OUT

    # charts -----------------------------------------------------------------
    figures.build_internship()
    figures.build_sector()
    figures.build_company_charts()
    figures.build_ratios()
    figures.build_conclusion_figures()
    figures.build_appendix()

    media = Media()
    crest = os.path.join(ASSETS, 'des_crest.jpg')
    if os.path.exists(crest):
        media.add_file('des_crest', crest, key='logo')
    letterhead = os.path.join(ASSETS, 'des_letterhead.jpg')
    if os.path.exists(letterhead):
        media.add_file('des_letterhead', letterhead, key='letterhead')

    # pass 1: discover the structure of the report, with no index at all
    info = []
    build(media, collect=info)
    labels = [(lv, label) for lv, label, _ in info[-1]['toc']]

    # pass 2: the index is present but its page numbers are blank, so that it
    # occupies exactly the space it will occupy once they are filled in
    info2 = []
    build(media, index_labels=labels, index_numbers=None, collect=info2)
    numbers = info2[-1]['toc']

    # pass 3: the real page numbers
    info3 = []
    build(media, index_labels=labels, index_numbers=numbers,
          total_pages=info2[-1]['pages'], index_span=info2[-1]['index'],
          collect=info3)
    second = info3[-1]

    if [(lv, l) for lv, l, _ in second['toc']] != labels:
        raise SystemExit('the structure changed between passes')
    if second['toc'] != numbers:
        raise SystemExit('pagination is not stable between passes')

    doc, media = build(media, index_labels=labels,
                       index_numbers=second['toc'],
                       total_pages=second['pages'],
                       index_span=second['index'])
    body = ''.join(doc.body)
    pack.write_package(out, body, media.items, TEMPLATE)

    print('index pages       :', second['index'])
    print('front matter      :', second['front'])
    print('total pages       :', second['pages'])
    print('images            :', len(media.items))
    print('table-width notes :', second['problems'] or 'none')
    print('written           :', out)
    for lv, label, page in second['toc']:
        if lv == 1:
            print('   %-58s %s' % (label[:58], page))


if __name__ == '__main__':
    main()
