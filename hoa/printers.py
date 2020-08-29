# -*- coding: utf-8 -*-
#
# MIT License
#
# Copyright (c) 2020 Whitemech
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
"""This module contains """
from functools import singledispatch

from hoa.ast.acceptance import AcceptanceAtom, AcceptanceCondition
from hoa.ast.boolean_expression import BinaryOp, FalseFormula, TrueFormula, UnaryOp
from hoa.ast.label import LabelAlias, LabelAtom, LabelExpression


@singledispatch
def acceptance_condition_to_string(_: AcceptanceCondition):
    return str(_)


@acceptance_condition_to_string.register
def _(f: AcceptanceAtom):
    return f"{f.atom_type.value}({'!' if f.negated else ''}{f.acceptance_set})"


@acceptance_condition_to_string.register
def _(f: BinaryOp):
    return (
        "("
        + f" {f.SYMBOL} ".join(map(acceptance_condition_to_string, f.operands))
        + ")"
    )


@acceptance_condition_to_string.register
def _(_acceptance_condition: TrueFormula):
    return "t"


@acceptance_condition_to_string.register
def _(_acceptance_condition: FalseFormula):
    return "f"


@singledispatch
def label_expression_to_string(_: LabelExpression):
    return str(_)


@label_expression_to_string.register
def _(f: LabelAtom):
    return f"{f.proposition}"


@label_expression_to_string.register
def _(f: LabelAlias):
    return f"{f.alias}"


@label_expression_to_string.register
def _(f: BinaryOp):
    return "(" + f" {f.SYMBOL} ".join(map(label_expression_to_string, f.operands)) + ")"


@label_expression_to_string.register
def _(f: UnaryOp):
    return f"({f.SYMBOL}{label_expression_to_string(f.argument)})"


@label_expression_to_string.register
def _(_f: TrueFormula):
    return "t"


@label_expression_to_string.register
def _(_f: FalseFormula):
    return "f"
