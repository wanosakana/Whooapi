==============
Authentication
==============

Overview
========

The Whoo API uses JWT (JSON Web Token) bearer authentication for all requests.

Token Format
============

.. code-block:: text

   Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNTYxNzc5MX0.070k3MDdDhryta3WumSieej0bB2PSpnRhFYcf_W85oM

Token Structure
===============

Header
------

.. code-block:: json

   {
     "alg": "HS256"
   }

Payload
-------

.. code-block:: json

   {
     "user_id": 15617791
   }

Using Authentication
====================

Include the token in every request:

.. code-block:: http

   GET /api/user HTTP/1.1
   Host: www.wh00.ooo
   Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNTYxNzc5MX0...
   Accept: application/json
   User-Agent: app.whoo/0.41.6 iOS/18.7

Session Management
==================

The API also uses session cookies which are automatically managed:

Cookie: ``_message_backend_session``

Cookie Properties:

* ``path=/``
* ``httponly``
* ``samesite=lax``

.. warning::
   Keep your authentication tokens secure. Never commit them to version control.
