###
# Copyright (c) 2005, Daniel DiPaolo
# Copyright (c) 2010-2021, Valentin Lorentz
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
###

from supybot.test import *

class LartTestCase(ChannelPluginTestCase):
    plugins = ('Lart', 'User')

    def setUp(self):
        ChannelPluginTestCase.setUp(self)
        # Create a valid user to use
        self.prefix = 'mf!bar@baz'
        self.irc.feedMsg(ircmsgs.privmsg(self.nick, 'register tester moo',
                                         prefix=self.prefix))
        m = self.irc.takeMsg() # Response to register.

    def testAdd(self):
        self.assertError('lart add foo')  # needs $who
        self.assertNotError('lart add smacks $who')

    def testLart(self):
        self.assertError('lart foo')  # no praises!
        self.assertNotError('lart add smacks $who')
        self.assertAction('lart foo', 'smacks foo')

    def testMeInReason(self):
        self.assertNotError('lart add makes $who sit by me')
        self.assertAction('lart foo', 'makes foo sit by me')

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
