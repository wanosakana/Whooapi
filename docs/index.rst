===================
Whoo API Reference
===================

Welcome to the Whoo API documentation. This reference provides comprehensive information about all available API endpoints.

.. note::
   This documentation is generated from network traffic analysis.
   Base URL: ``https://www.wh00.ooo``

Contents
========

.. toctree::
   :maxdepth: 2
   :caption: API Reference:

   authentication
   user_management
   location
   friends
   messaging
   rooms
   premium
   challenges
   other

Quick Start
===========

Authentication
--------------

All API requests require authentication using a Bearer token:

.. code-block:: http

   Authorization: Bearer <your_jwt_token>

Common Headers
--------------

* ``User-Agent``: app.whoo/0.41.6 iOS/18.7
* ``Accept``: application/json
* ``Accept-Language``: ja-JP
* ``Accept-Encoding``: gzip, deflate, br
* ``Content-Type``: application/json

Response Format
---------------

All responses return JSON with appropriate HTTP status codes:

* ``200 OK``: Request successful
* ``304 Not Modified``: Resource not modified (cached)
* ``404 Not Found``: Resource not found
* ``503 Service Unavailable``: Service temporarily unavailable

Rate Limiting
-------------

The API implements caching using ETags. Include the ``If-None-Match`` header to optimize bandwidth.
