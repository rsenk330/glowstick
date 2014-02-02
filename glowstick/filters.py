"""Convert paths to absolute paths in Less

Issue: https://github.com/jezdez/django_compressor/issues/226
Source: http://stackoverflow.com/a/14842293/1527753

"""
import sys

from compressor.filters.base import CompilerFilter
from compressor.filters.css_default import CssAbsoluteFilter


class LessFilter(CompilerFilter):
    def __init__(self, content, attrs, **kwargs):
        super(LessFilter, self).__init__(content, command='lessc {infile} {outfile} && autoprefixer {outfile}', **kwargs)

    def input(self, **kwargs):
        content = super(LessFilter, self).input(**kwargs)
        return CssAbsoluteFilter(content).input(**kwargs)
