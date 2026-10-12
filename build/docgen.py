"""A small, deterministic WordprocessingML writer with a built-in layout model.

The metrics are those measured from the approved reference report
("Om Misal ... Final Approved SIP Research Report"):  A4 paper, half-inch
margins, page borders, Times New Roman 12 pt, 1.5-line spacing written the way
Word writes it -- ``w:line="360" w:lineRule="auto"`` -- paragraphs separated by
4 pt, chapter titles centred bold 14 pt underlined, section titles justified
bold 12 pt in capitals with 7 pt above and 4 pt below, tables with grey
borders, a pale blue header row and 12 pt justified cell text.

Because the report uses one type size for the body, a paragraph of *n* lines
occupies a predictable height, so hard page breaks can be placed at the right
points and the index can be printed with real page numbers.  With 1.5-line
spacing at 12 pt, Word advances the pen by 1.5 x (ascender + descender +
lineGap) / unitsPerEm x 12 pt = 1.5 x 1.1499 x 12 = 20.70 pt, that is 414
twips per line; the model works with 415 and allows 37 lines against a
physical capacity of 37.1.  The wrapping model measures text at 98 per cent of
the true frame width.  Both choices over-estimate height, which can only leave
a little white space at the foot of a page; an under-estimate would displace
everything that follows.
"""

from afm import text_width_tw

# ---------------------------------------------------------------------------
# Geometry, in twentieths of a point (twips)
# ---------------------------------------------------------------------------
PAGE_W = 11906          # A4 width
PAGE_H = 16838          # A4 height
MARGIN = 720            # 0.5 inch on every side, as in the reference report
FRAME_W = PAGE_W - 2 * MARGIN          # 10466 twips of usable width
FRAME_H = PAGE_H - 2 * MARGIN          # 15398 twips of usable height

LINE = 360              # w:line="360" w:lineRule="auto" = 1.5 lines, as in
RULE = 'auto'           # ... the reference;  the *model* uses PITCH below
PITCH12 = 415           # twips advanced by one line of 12 pt text at 1.5 line
SAFE_LINES = 37         # lines placed on a page, against a physical 37.1
CAPACITY = SAFE_LINES * PITCH12        # 15355 twips
WRAP_W = int(FRAME_W * 0.980)          # conservative measure width

BODY_SIZE = 12.0        # points;  Times New Roman 12 pt throughout
SMALL_SIZE = 11.0
TINY_SIZE = 9.0

AFTER = 80              # 4 pt after every paragraph, as in the reference
CHAPTER_BEFORE = 200    # 10 pt above a chapter title
CHAPTER_AFTER = 120     # 6 pt below it
SECTION_BEFORE = 140    # 7 pt above a section title
SECTION_AFTER = 80

BORDER_XML = (
    '<w:tblBorders>'
    '<w:top w:val="single" w:sz="6" w:space="0" w:color="A6A6A6"/>'
    '<w:left w:val="single" w:sz="6" w:space="0" w:color="A6A6A6"/>'
    '<w:bottom w:val="single" w:sz="6" w:space="0" w:color="A6A6A6"/>'
    '<w:right w:val="single" w:sz="6" w:space="0" w:color="A6A6A6"/>'
    '<w:insideH w:val="single" w:sz="6" w:space="0" w:color="A6A6A6"/>'
    '<w:insideV w:val="single" w:sz="6" w:space="0" w:color="A6A6A6"/>'
    '</w:tblBorders>'
)
BORDER_COLOR = 'A6A6A6'    # grey rules of every body table
HEAD_FILL = 'D9EAF7'       # the pale blue used for every table header row
TITLE_COLOR = '102C57'     # the dark blue of a table or chart title
CELL_MARGIN = 108          # twips of left/right cell padding (Word default)
CELL_MARGIN_V = 0          # the reference uses no top/bottom padding

FONT = 'Times New Roman'


def pitch(size=BODY_SIZE):
    """Height of one line of text, in twips, at the reference line spacing."""
    return int(round(PITCH12 * size / 12.0))


# ---------------------------------------------------------------------------
# Inline markup:  **bold**,  *italic*,  __underline__
# ---------------------------------------------------------------------------
def parse_runs(text):
    """Split a string into (text, bold, italic, underline) runs."""
    runs = []
    buf = []
    bold = italic = underline = False
    i = 0
    n = len(text)
    while i < n:
        if text.startswith('**', i):
            if buf:
                runs.append((''.join(buf), bold, italic, underline))
                buf = []
            bold = not bold
            i += 2
        elif text.startswith('__', i):
            if buf:
                runs.append((''.join(buf), bold, italic, underline))
                buf = []
            underline = not underline
            i += 2
        elif text[i] == '*' and not text.startswith('**', i):
            if buf:
                runs.append((''.join(buf), bold, italic, underline))
                buf = []
            italic = not italic
            i += 1
        else:
            buf.append(text[i])
            i += 1
    if buf:
        runs.append((''.join(buf), bold, italic, underline))
    return [r for r in runs if r[0]]


def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


def rpr(bold=False, italic=False, underline=False, size=BODY_SIZE, color=None):
    parts = ['<w:rFonts w:ascii="%s" w:eastAsia="%s" w:hAnsi="%s" w:cs="%s"/>'
             % (FONT, FONT, FONT, FONT)]
    if bold:
        parts.append('<w:b/><w:bCs/>')
    if italic:
        parts.append('<w:i/><w:iCs/>')
    if underline:
        parts.append('<w:u w:val="single"/>')
    if color:
        parts.append('<w:color w:val="%s"/>' % color)
    parts.append('<w:sz w:val="%d"/><w:szCs w:val="%d"/>'
                 % (int(round(size * 2)), int(round(size * 2))))
    return '<w:rPr>' + ''.join(parts) + '</w:rPr>'


def runs_xml(text, size=BODY_SIZE, force_bold=False, force_italic=False,
             color=None):
    out = []
    for chunk, b, i, u in parse_runs(text):
        out.append('<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>'
                   % (rpr(b or force_bold, i or force_italic, u, size, color),
                      esc(chunk)))
    return ''.join(out)


def measure_runs(text, size=BODY_SIZE):
    w = 0.0
    for chunk, b, i, u in parse_runs(text):
        w += text_width_tw(chunk, size, b, i)
    return w


def wrap_text(text, width_tw, size=BODY_SIZE, first_prefix=''):
    """Greedy line breaking, matching Word's default behaviour for this font."""
    lines = []
    words = text.split(' ')
    cur = ''
    cur_w = 0.0
    prefix_w = measure_runs(first_prefix, size) if first_prefix else 0.0
    limit = width_tw - prefix_w
    for word in words:
        ww = measure_runs(word, size)
        space_w = measure_runs(' ', size)
        if cur == '':
            cand, cand_w = word, ww
        else:
            cand, cand_w = cur + ' ' + word, cur_w + space_w + ww
        if cand_w <= limit or cur == '':
            cur, cur_w = cand, cand_w
        else:
            lines.append(cur)
            cur, cur_w = word, ww
            limit = width_tw
    if cur != '' or not lines:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------------------
# Document builder
# ---------------------------------------------------------------------------
class Doc(object):
    def __init__(self, start_page=1):
        self.body = []
        self.page = start_page
        self.used = 0
        self.toc = []
        self.pending_break = False
        self.in_table = False
        self.table_header_h = 0
        self.last_y = 0

    # -- page handling ------------------------------------------------------
    def _break_xml(self):
        return ('<w:r>%s<w:br w:type="page"/></w:r>'
                % rpr(size=TINY_SIZE))

    def new_page(self):
        self.pending_break = True
        self.page += 1
        self.used = 0

    def ensure(self, height, keep_header=False):
        if self.used + height > CAPACITY and self.used > 0:
            self.new_page()
            if keep_header and self.in_table:
                self.used += self.table_header_h

    def _take_break(self):
        """Return True if a page break is pending, and clear it."""
        if self.pending_break:
            self.pending_break = False
            return True
        return False

    # -- paragraphs ---------------------------------------------------------
    def para(self, text, size=BODY_SIZE, bold=False, italic=False,
             underline=False, align='both', indent_left=0, first_line=0,
             before=0, after=AFTER, space_after_lines=0, keep_next=False,
             color=None, line=LINE, tab_stops=None):
        lines = wrap_text(text, WRAP_W - indent_left - first_line, size)
        n = len(lines)
        h = n * (pitch(size) if line == LINE else line) + before + after
        if space_after_lines:
            h = n * pitch(size) + int(space_after_lines * pitch(size))
        if keep_next:
            self.ensure(h + 2 * pitch(size))
        else:
            self.ensure(h)

        brk = self._take_break()
        rule = RULE if line == LINE else 'exact'
        ppr = ['<w:spacing w:before="%d" w:after="%d" w:line="%d" '
               'w:lineRule="%s"/>' % (before, after, line, rule)]
        if keep_next:
            ppr.append('<w:keepNext/>')
        ppr.append('<w:jc w:val="%s"/>' % align)
        ind = []
        if indent_left:
            ind.append('w:left="%d"' % indent_left)
        if first_line:
            ind.append('w:hanging="%d"' % first_line)
        if ind:
            ppr.append('<w:ind %s/>' % ' '.join(ind))
        if tab_stops:
            ppr.append('<w:tabs>' + ''.join(
                '<w:tab w:val="left" w:pos="%d"/>' % t for t in tab_stops)
                + '</w:tabs>')
        run = (self._break_xml() if brk else '') + runs_xml(
            text, size, bold, italic, color)
        if underline:
            run = run.replace('<w:rPr>', '<w:rPr><w:u w:val="single"/>')
        self.body.append('<w:p><w:pPr>%s</w:pPr>%s</w:p>'
                         % (''.join(ppr), run))
        self.used += h
        self.last_y = self.used
        return h

    def blank(self, lines=1):
        """``lines`` empty paragraphs, each separated like body text."""
        for i in range(max(1, int(lines))):
            self.para('', size=BODY_SIZE)

    # -- headings -----------------------------------------------------------
    def chapter(self, text, toc_label=None, level=1):
        """Chapter title:  centred, bold, 14 pt, underlined, as the reference."""
        h = self.para(text, size=14.0, bold=True, align='center',
                      before=CHAPTER_BEFORE, after=CHAPTER_AFTER,
                      keep_next=True, underline=True)
        self.toc.append((level, toc_label if toc_label is not None else text,
                         self.page))
        return h

    def section(self, text, toc_label=None):
        """Section title:  justified, bold, 12 pt, capitals with 7 pt above."""
        h = self.para(text, size=BODY_SIZE, bold=True, align='both',
                      before=SECTION_BEFORE, after=SECTION_AFTER,
                      keep_next=True)
        if toc_label is not None:
            self.toc.append((2, toc_label, self.page))
        return h

    def subsection(self, text, toc_label=None):
        """The bold 12 pt run-in heading Word calls "Normal (Web)"."""
        h = self.para(text, size=BODY_SIZE, bold=True, align='both',
                      before=SECTION_BEFORE, after=SECTION_AFTER,
                      keep_next=True)
        if toc_label is not None:
            self.toc.append((2, toc_label, self.page))
        return h

    def heading(self, text, level=1, toc_label=None, align='both',
                underline=False, before=0, center=False):
        """Backwards-compatible dispatch onto the three heading levels."""
        if level == 1:
            return self.subsection(text, toc_label)
        if level == 2:
            return self.subsection(text, toc_label)
        return self.subsection(text, toc_label)

    def mark(self, label, level):
        """Record a table-of-contents entry at the current position."""
        self.toc.append((level, label, self.page))

    def centre_title(self, text, size=14.0, bold=True, underline=False,
                     before=CHAPTER_BEFORE, after=CHAPTER_AFTER,
                     toc_label=None, level=None):
        h = self.para(text, size=size, bold=bold, align='center',
                      before=before, after=after, keep_next=True,
                      underline=underline)
        if toc_label is not None:
            self.toc.append((level if level is not None else 1, toc_label,
                             self.page))
        return h

    def table_title(self, text):
        """Title above a table:  bold 12 pt in the reference's dark blue."""
        return self.para(text, size=BODY_SIZE, bold=True, align='both',
                         before=200, after=120, keep_next=True,
                         color=TITLE_COLOR)

    def caption(self, text):
        """Caption below a chart, in the same dark blue as a table title."""
        return self.para(text, size=BODY_SIZE, bold=True, align='center',
                         before=80, after=140, color=TITLE_COLOR)

    # -- images -------------------------------------------------------------
    def image(self, rel_id, width_pt, height_pt, align='center', before=120,
              after=60, keep_next=False):
        cx = int(width_pt * 12700)
        cy = int(height_pt * 12700)
        self.pic_id = getattr(self, 'pic_id', 1000) + 1
        h = int(height_pt * 20) + before + after
        self.ensure(h)
        brk = self._take_break()
        drawing = (
            '<w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
            '<wp:extent cx="%d" cy="%d"/>'
            '<wp:effectExtent l="0" t="0" r="0" b="0"/>'
            '<wp:docPr id="%d" name="Picture %d"/>'
            '<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
            '<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            '<pic:nvPicPr><pic:cNvPr id="%d" name="Picture %d"/><pic:cNvPicPr/></pic:nvPicPr>'
            '<pic:blipFill><a:blip r:embed="%s"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
            '<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="%d" cy="%d"/></a:xfrm>'
            '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>'
            '</pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing>'
            % (cx, cy, self.pic_id, self.pic_id, self.pic_id, self.pic_id,
               rel_id, cx, cy))
        ppr = ('<w:spacing w:before="%d" w:after="%d" w:line="240" '
               'w:lineRule="auto"/><w:jc w:val="%s"/>' % (before, after, align))
        if keep_next:
            ppr = '<w:keepNext/>' + ppr
        self.body.append('<w:p><w:pPr>%s</w:pPr><w:r>%s%s</w:r></w:p>'
                         % (ppr, self._break_xml() if brk else '', drawing))
        self.used += h
        return h

    # -- tables -------------------------------------------------------------
    def table(self, rows, widths, header=True, aligns=None, size=BODY_SIZE,
              bold_first_col=False, keep_next_first=False, border_color=None,
              head_fill=HEAD_FILL, cell_before=0, cell_after=0,
              cell_keep_next=False, head_height=None, table_pos=False,
              border_sz=6, cell_size=None, bold_rows=None):
        """``rows`` is a list of lists of strings; the first row is the header.

        ``cell_size`` allows a different type size inside the cells than in the
        surrounding text.  ``table_pos`` floats the table the way the reference
        index does;  ``cell_keep_next`` keeps every row with the next one.
        """
        total = sum(widths)
        aligns = aligns or ['l'] * len(widths)
        amap = {'l': 'both', 'c': 'center', 'r': 'right', 'j': 'both'}
        csize = cell_size if cell_size else size
        line_h = pitch(csize)

        def cell_para(text, w, al, bold=False, fill=None, vcenter=True):
            inner_w = w - 2 * CELL_MARGIN
            lines = wrap_text(text, inner_w, csize)
            tcpr = ['<w:tcW w:w="%d" w:type="dxa"/>' % w]
            if fill:
                tcpr.append('<w:shd w:val="clear" w:color="auto" w:fill="%s"/>'
                            % fill)
            if vcenter:
                tcpr.append('<w:vAlign w:val="center"/>')
            ps = []
            for ln in lines:
                ppr = ['<w:spacing w:before="%d" w:after="%d" w:line="%d" '
                       'w:lineRule="%s"/>' % (cell_before, cell_after, LINE,
                                              RULE)]
                if cell_keep_next:
                    ppr.append('<w:keepNext/>')
                ppr.append('<w:jc w:val="%s"/>' % amap[al])
                ps.append('<w:p><w:pPr>%s</w:pPr>%s</w:p>'
                          % (''.join(ppr), runs_xml(ln if ln else ' ', csize,
                                                    bold)))
            return ('<w:tc><w:tcPr>%s</w:tcPr>%s</w:tc>'
                    % (''.join(tcpr), ''.join(ps)),
                    len(lines) * line_h + cell_before + cell_after)

        def row_xml(cells, bold=False, fill=None, header_row=False, height=None):
            tcs = []
            h = 0
            for idx, txt in enumerate(cells):
                boldcell = bold or (bold_first_col and idx == 0)
                cx, ch = cell_para(txt, widths[idx], aligns[idx], boldcell, fill)
                tcs.append(cx)
                h = max(h, ch)
            if height:
                h = max(h, height)
            trpr = '<w:trPr>'
            if header_row:
                trpr += '<w:tblHeader/>'
            if height:
                trpr += '<w:trHeight w:val="%d"/>' % height
            trpr += '</w:trPr>'
            return '<w:tr>%s%s</w:tr>' % (trpr, ''.join(tcs)), h

        borders = BORDER_XML
        if border_color:
            borders = BORDER_XML.replace(BORDER_COLOR, border_color)
        if border_sz != 6:
            borders = borders.replace('w:sz="6"', 'w:sz="%d"' % border_sz)
        tblp = ('<w:tblpPr w:leftFromText="180" w:rightFromText="180" '
                'w:vertAnchor="text" w:horzAnchor="margin" w:tblpY="126"/>'
                if table_pos else '')
        tblpr = (
            '<w:tblPr><w:tblStyle w:val="TableGridLight"/>'
            '%s'
            '<w:tblW w:w="%d" w:type="dxa"/>'
            '%s'
            '<w:tblCellMar><w:top w:w="%d" w:type="dxa"/>'
            '<w:left w:w="%d" w:type="dxa"/><w:bottom w:w="%d" w:type="dxa"/>'
            '<w:right w:w="%d" w:type="dxa"/></w:tblCellMar>'
            '<w:tblLayout w:type="fixed"/>'
            '<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" '
            'w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>'
            '</w:tblPr>' % (tblp, total, borders, CELL_MARGIN_V, CELL_MARGIN,
                            CELL_MARGIN_V, CELL_MARGIN))
        grid = '<w:tblGrid>' + ''.join(
            '<w:gridCol w:w="%d"/>' % w for w in widths) + '</w:tblGrid>'

        pieces = []
        self.in_table = True
        for i, r in enumerate(rows):
            is_head = bool(header and i == 0)
            xml, h = row_xml(r, bold=(is_head or (bold_rows and i in bold_rows)),
                             fill=(head_fill if is_head else None),
                             header_row=is_head,
                             height=(head_height if is_head else None))
            if is_head:
                self.table_header_h = h
            self.ensure(h, keep_header=(i > 0))
            if self._take_break():
                pieces.append('<w:p><w:pPr><w:spacing w:before="0" '
                              'w:after="0" w:line="20" w:lineRule="exact"/>'
                              '</w:pPr><w:r>%s<w:br w:type="page"/></w:r>'
                              '</w:p>' % rpr(size=TINY_SIZE))
            pieces.append(xml)
            self.used += h
        self.in_table = False
        self.body.append('<w:tbl>%s%s%s</w:tbl>' % (tblpr, grid,
                                                    ''.join(pieces)))
        return sum(1 for _ in rows)

    def after_table(self, lines=0.4):
        self.used += int(lines * PITCH12)


def build_sectpr():
    return (
        '<w:sectPr>'
        '<w:headerReference w:type="default" r:id="rId100"/>'
        '<w:footerReference w:type="default" r:id="rId101"/>'
        '<w:pgSz w:w="%d" w:h="%d"/>'
        '<w:pgMar w:top="%d" w:right="%d" w:bottom="%d" w:left="%d" '
        'w:header="708" w:footer="708" w:gutter="0"/>'
        '<w:pgBorders w:offsetFrom="page">'
        '<w:top w:val="thinThickSmallGap" w:sz="24" w:space="24" w:color="auto"/>'
        '<w:left w:val="thinThickSmallGap" w:sz="24" w:space="24" w:color="auto"/>'
        '<w:bottom w:val="thickThinSmallGap" w:sz="24" w:space="24" w:color="auto"/>'
        '<w:right w:val="thickThinSmallGap" w:sz="24" w:space="24" w:color="auto"/>'
        '</w:pgBorders>'
        '<w:cols w:space="708"/><w:docGrid w:linePitch="360"/>'
        '</w:sectPr>' % (PAGE_W, PAGE_H, MARGIN, MARGIN, MARGIN, MARGIN))
