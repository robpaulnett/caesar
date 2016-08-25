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
import cgi

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

# a form for creating an encryption (rot13 or rot*)
rotate_form_input = """
<form action="/" method="POST">
    <label>
        <strong>Rotate by:</strong>
        <input type="text" name="rotatetimes" value="%(rotatetimes)s"/>
    </label>
    <br /><br />
    <label>
        <strong>Encrpytion:</strong>
        <br />
        <input type="text" name="encrypttext" size="250" style="height:10em;width:35em;" value="%(encrypttext)s"/>
    </label>
    <br />
    <input type="submit" value="Submit Query"/>
</form>
"""

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.caesar.com/
    """
    def write_form(self, rotatetimes="", encrypttext=""):
        self.response.out.write(rotate_form_input % {"rotatetimes": rotatetimes,
                                                        "encrypttext": encrypttext})

    def get(self):
        #PUT FORM ON SCREEN
        #response = page_header + rotate_form_input + page_footer
        self.write_form()

    def post(self):
        # look inside the request to figure out what the user typed
        number_rotations = self.request.get('rotatetimes')
        user_raw_inputs = self.request.get('encrypttext')
        encrypted_item = encrypt(user_raw_inputs, number_rotations)
        # combine all the pieces to build the content of our response
        main_content = encrypted_item
        response = page_header + main_content + page_footer
        self.response.out.write(response)


app = webapp2.WSGIApplication([
('/', Index),
], debug=True)
