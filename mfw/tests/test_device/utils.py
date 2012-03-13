# vim: set fileencoding=utf-8 :
"""
Unittest module of ...


AUTHOR:
    lambdalisue[Ali su ae] (lambdalisue@hashnote.net)
    
License:
    The MIT License (MIT)

    Copyright (c) 2012 Alisue allright reserved.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to
    deal in the Software without restriction, including without limitation the
    rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
    sell copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
    IN THE SOFTWARE.

"""
from __future__ import with_statement
from mfw.device.base import Device
from mfw.device import detect

def test_detect_with_user_agent(testcase, user_agent):
    kind, name, model, version, user_agent = user_agent

    meta = {}
    meta['HTTP_USER_AGENT'] = user_agent

    device = detect(meta)

    testcase.assertTrue(isinstance(device, Device))
    testcase.assertEqual(device.kind, kind)
    testcase.assertEqual(device.name, name)
    testcase.assertEqual(device.model, model)
    if device.version:
        testcase.assertTrue(device.version.startswith(version),
                '"%s" does not start with "%s"' % (
                    device.version,
                    version,
                ))
    else:
        testcase.assertEqual(device.version, version)

def test_detect_with_user_agent_mobile(testcase, user_agent):
    kind, name, model, version, cookie, user_agent, remote_addr, addition = user_agent

    meta = dict(addition)
    meta['HTTP_USER_AGENT'] = user_agent
    meta['REMOTE_ADDR'] = remote_addr

    device = detect(meta)

    testcase.assertTrue(isinstance(device, Device))
    testcase.assertEqual(device.kind, kind)
    testcase.assertEqual(device.name, name)
    testcase.assertEqual(device.model, model)
    if device.version:
        testcase.assertTrue(device.version.startswith(version),
                '"%s" does not start with "%s"' % (
                    device.version,
                    version,
                ))
    else:
        testcase.assertEqual(device.version, version)
    testcase.assertEqual(device.support_cookie, cookie)
    if remote_addr == '127.0.0.1':
        testcase.assertFalse(device.reliable,
                    '"127.0.0.1" is not reliable'
                )
    else:
        testcase.assertTrue(device.reliable,
                    '"%s" is not within %s carrier CIDR' % (
                        remote_addr, device.carrier,
                ))

    testcase.assertEqual(device.uid, 'A12345')


