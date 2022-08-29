
import re, uuid
from .TemplateEngine import *
from .TemplateEngine import TemplateOps

class MarkdownFormatter:
    @classmethod
    def format_item(self, item, item_level = 0):
        return "{}- {}".format('  ' * (item_level + 1), item)
    @classmethod
    def format_link(self, alt, link):
        return '[{}]({})'.format(alt, link)
    @classmethod
    def format_obj_link(self, spec):
        return self.format_link(spec.split('.')[-1], spec.replace('.', '/') + ".md")
    @classmethod
    def format_inline_code(self, arg):
        """

        :param arg:
        :type arg: str
        :return:
        :rtype:
        """
        nticks = arg.count("`")
        fence = "`"*(nticks+1)
        return fence + arg + fence
    @classmethod
    def format_code_block(self, arg):
        """

        :param arg:
        :type arg: str
        :return:
        :rtype:
        """
        nticks = arg.count("`")
        fence = "`"*(nticks+3)
        return fence + "python\n" + arg + "\n" + fence
    @classmethod
    def format_quote_block(self, arg):
        """

        :param arg:
        :type arg: str
        :return:
        :rtype:
        """

        return ">" + arg.replace("\n", "\n>")

    link_bar_template='<div class="container{boxed}">\n{links}\n</div>'
    link_row_template='  <div class="row">\n{cols}\n</div>'
    link_item_template='   <div class="col" markdown="1">\n{item}   \n</div>'
    @classmethod
    def format_grid(self, link_grid, boxed=False):
        return self.link_bar_template.format(links="\n".join(
            self.link_row_template.format(
                cols="\n".join(self.link_item_template.format(item=item) for item in row)
            )
            for row in link_grid if len(row) > 0
        ),
        boxed=' alert alert-secondary bg-light' if boxed else ""
        )
    @classmethod
    def split(self, links, ncols=3, pad=""):
        num_cols = ncols
        splits = []
        sub = []
        for x in links:
            sub.append(x)
            if len(sub) == num_cols:
                splits.append(sub)
                sub = []
        splits.append(sub + [pad] * (ncols - len(sub)))
        return splits

    collapse_template="""
<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
{header_fmt} <a class="collapse-link" data-toggle="collapse" href="#{name}" markdown="1">{header}</a> {opener}
 </div>
 <div class="collapsible-section collapsible-section-body collapse {show}" id="{name}" markdown="1">
 {content}
 </div>
</div>
"""
    collapse_opener = '<a class="float-right" data-toggle="collapse" href="#{name}"><i class="fa fa-chevron-down"></i></a>'
    def format_collapse_section(self, header, content, name=None, open=True, include_opener=True):
        header_fmt = ""
        while header.startswith("#"):
            header_fmt += "#"
            header = header[1:]
        if name is None:
            name = re.sub("\W", "", header) + "-" + str(uuid.uuid4())[:6]
        return self.collapse_template.format(
            header_fmt=header_fmt,
            header=header,
            content=content,
            name=name,
            show="show" if open else "",
            opener=self.collapse_opener.format(name=name) if include_opener else ""
        )

    def format_obj_link_grid(self, mems, ncols=3, boxed=True):
        links = self.split(
            [self.format_obj_link(l) for l in mems],
            ncols=ncols
        )
        return self.format_grid(links, boxed=boxed)

class MarkdownFormatDirective(TemplateFormatDirective):
    Link = "link", TemplateOps.wrap(MarkdownFormatter.format_link)
    ObjLink = "objlink", TemplateOps.wrap(MarkdownFormatter.format_obj_link)
    Item = "item", TemplateOps.wrap(MarkdownFormatter.format_item)
    Code = "code", TemplateOps.wrap(MarkdownFormatter.format_code_block)
    Quote = "quote", TemplateOps.wrap(MarkdownFormatter.format_quote_block)
    # Card = "card", TemplateOps.wrap(MarkdownFormatter.format_card)
    # Alert = "alert", TemplateOps.wrap(MarkdownFormatter.format_alert)
    Collapse = "collapse", TemplateOps.wrap(MarkdownFormatter.format_collapse_section)
    Grid = "grid", TemplateOps.wrap(MarkdownFormatter.format_grid)
    Split = "split", TemplateOps.wrap(MarkdownFormatter.split)
    ObjLinkGrid = "objlink_grid", TemplateOps.wrap(MarkdownFormatter.format_obj_link_grid)

