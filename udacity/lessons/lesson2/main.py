#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 28 November 2013 Edited to test github
import webapp2

form="""
<form method="post" action="/testform">
	<select name="r">
		<option value="1">the number one</option>
		<option value=>two</option>
		<option>three</option>
	</select>
	<label>
		one
		<input type = "radio" name="q" value="1">
	</label>
	<label>
		two
		<input type = "radio" name="q" value="2">
	</label>
	<label>
		three
		<input type = "radio" name="q" value="3">
	</label>
	<br />
	<input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)
		
class TestHandler(webapp2.RequestHandler):
	def post(self):
		#q = self.request.get("q")
		#self.response.out.write(q)
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write(self.request)
		
app = webapp2.WSGIApplication([
    ('/', MainHandler),('/testform', TestHandler)
], debug=True)

