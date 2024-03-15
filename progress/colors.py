# -*- coding: utf-8 -*-

# Copyright (c) 2020 Georgios Verigakis <verigak@gmail.com>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
'''
ANSI 控制序列主要用于在文本终端中控制字符颜色的显示，
它们在 Unix-like 系统（如 Linux）的终端中非常普遍和有效。
这些控制序列是基于 ANSI 标准，它们在早期的计算机系统中用于在文本模式下改变字符的显示属性，如颜色、亮度、下划线等。

设置文本字体样式
\033[0m 默认样式
\033[1m 粗体
\033[4m 下划线
\033[5m 闪烁
\033[7m 反向（阴阳）
\033[9m 隐藏
\033[21m 非粗体
\033[24m 非下划线
\033[25m 非闪烁
\033[27m 非反向
\033[90m 不可见

设置背景色
\033[40m 黑色背景
\033[41m 红色背景
\033[42m 绿色背景
\033[43m 黄色背景
\033[44m 蓝色背景
\033[45m 紫色背景
\033[46m 青色背景
\033[47m 白色背景

设置前景色
\033[30m 黑色前景
\033[31m 红色前景
\033[32m 绿色前景
\033[33m 黄色前景
\033[34m 蓝色前景
\033[35m 紫色前景
\033[36m 青色前景
\033[37m 白色前景


'''
from functools import partial


COLORS = ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan',
          'white')
STYLES = ('bold', 'faint', 'italic', 'underline', 'blink', 'blink2',
          'negative', 'concealed', 'crossed')


def color(s, fg=None, bg=None, style=None):
    sgr = []

    if fg:
        if fg in COLORS:
            sgr.append(str(30 + COLORS.index(fg)))
        elif isinstance(fg, int) and 0 <= fg <= 255:
            sgr.append('38;5;%d' % int(fg))
        else:
            raise Exception('Invalid color "%s"' % fg)

    if bg:
        if bg in COLORS:
            sgr.append(str(40 + COLORS.index(bg)))
        elif isinstance(bg, int) and 0 <= bg <= 255:
            sgr.append('48;5;%d' % bg)
        else:
            raise Exception('Invalid color "%s"' % bg)

    if style:
        for st in style.split('+'):
            if st in STYLES:
                sgr.append(str(1 + STYLES.index(st)))
            else:
                raise Exception('Invalid style "%s"' % st)

    if sgr:
        prefix = '\x1b[' + ';'.join(sgr) + 'm'
        suffix = '\x1b[0m'
        return prefix + s + suffix
    else:
        return s


# Foreground shortcuts
black = partial(color, fg='black')
red = partial(color, fg='red')
green = partial(color, fg='green')
yellow = partial(color, fg='yellow')
blue = partial(color, fg='blue')
magenta = partial(color, fg='magenta')
cyan = partial(color, fg='cyan')
white = partial(color, fg='white')

# Style shortcuts
bold = partial(color, style='bold')
faint = partial(color, style='faint')
italic = partial(color, style='italic')
underline = partial(color, style='underline')
blink = partial(color, style='blink')
blink2 = partial(color, style='blink2')
negative = partial(color, style='negative')
concealed = partial(color, style='concealed')
crossed = partial(color, style='crossed')
