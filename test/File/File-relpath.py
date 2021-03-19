#!/usr/bin/env python
#
# MIT License
#
# Copyright The SCons Foundation
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
Test that .relpath works on file nodes.
Specifically ${TARGET.relpath}, ${SOURCE.relpath} match expected path
"""

import os

import TestSCons

test = TestSCons.TestSCons()

test.subdir('src', ['src', 'dir'])

test.dir_fixture('fixture/relpath')
test.run('-Q', chdir='base', status=0, stdout="""\
../foo/dir build/file1
%s %s
src/file
%s
src/file
%s
""" % (os.path.abspath('base/../foo/dir'), os.path.abspath('base/build/file1'), os.path.abspath('base/src/file'),
       os.path.abspath('base/src/file')))
