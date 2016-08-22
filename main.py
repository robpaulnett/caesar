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
#
import webapp2
from caesar import encrypt

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar Encryption</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h3>
        <a href="/">Caesar Encryption</a>
    </h3>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.caesar.com/
    """
    def get(self):
    #    self.response.write('Hello world!')

        #crypto_header = "<h4>Do An Encryption</h4>"

        # a form for creating an encryption (rot13 or rot*)
        encrypt_form_input = """
        <form action="/rotall" method="GET">
            <label>
                <strong>Rotate by:</strong>
                <input type="text" name="encrypt_start"/>
            </label>
            <!--  #<div>%(error)s</div>    -->
            <br /><br />
            <label>
                <strong>Encrpyted Results:</strong>
                <br />
                <textarea type="text" name="encrypt_end" size="250" style="height:10em;width:35em;" value="self.response.write(encrypt_form_input)"></textarea>
            </label>
            <br />
            <input type="submit" value="Submit Query"/>
        </form>
        """
        # combine all the pieces to build the content of our response
        main_content = encrypt_form_input
        response = page_header + main_content + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/rotall', MainHandler)
], debug=True)
