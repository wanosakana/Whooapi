=====
Other
=====

Additional API endpoints and utilities.

Map Style Validation
====================

.. http:post:: /api/ios/map_style/validation

   Validate iOS map style configuration.

   **Request Headers:**

   .. code-block:: http

      Content-Type: application/json
      Authorization: Bearer <token>
      Content-Length: 0

   **Response:**

   :statuscode 200: Validation successful

   .. code-block:: json

      {
        "result": true
      }

   .. note::
      This endpoint validates custom map styles for iOS devices.

Get User's Footprint List
==========================

.. http:get:: /api/user/footprint_list

   Retrieve the user's location history (footprints).

   **Query Parameters:**

   :page: Page number (optional)

   **Response:**

   :statuscode 200: Footprint list retrieved

   .. code-block:: json

      {
        "footprints": [],
        "next_page": null
      }

Get Original Stamp Sheets
==========================

.. http:get:: /api/user/original_stamp_sheets

   Get user's custom stamp sheet collections.

   **Response:**

   :statuscode 404: No stamp sheets found
   :statuscode 200: Stamp sheets retrieved

User Profile Picture
====================

.. http:get:: /api/user/profile_picture

   Get the user's profile picture URL.

   **Response:**

   :statuscode 200: Profile picture URL retrieved

   .. code-block:: json

      {
        "profile_picture_url": "https://dij5764lbzlpu.cloudfront.net/..."
      }

Search Users
============

.. http:get:: /api/users/search

   Search for users by username or display name.

   **Query Parameters:**

   :q: Search query string
   :page: Page number (default: 1)
   :limit: Results per page (default: 20)

   **Example:**

   .. code-block:: http

      GET /api/users/search?q=asahi&page=1 HTTP/1.1

   **Response:**

   :statuscode 200: Search results retrieved

   .. code-block:: json

      {
        "users": [
          {
            "id": 15617791,
            "username": "asahi0900",
            "display_name": "あさひ",
            "profile_image": "https://..."
          }
        ],
        "total": 1,
        "page": 1
      }

Get App Configuration
=====================

.. http:get:: /api/config

   Get application configuration and feature flags.

   **Response:**

   :statuscode 200: Configuration retrieved

   .. code-block:: json

      {
        "features": {
          "new_ui": true,
          "beta_features": false
        },
        "api_version": "2.0",
        "min_app_version": "0.40.0"
      }

Health Check
============

.. http:get:: /health

   Check API server health status.

   **Response:**

   :statuscode 200: Server is healthy

   .. code-block:: json

      {
        "status": "ok",
        "timestamp": "2026-02-15T18:43:02+09:00"
      }

CDN Resources
=============

Static assets are served from CloudFront:

**Base URL:** ``https://dij5764lbzlpu.cloudfront.net/``

Resource Types:

* Profile images: ``/profile_images/images/``
* App icons: ``/app_icons/``
* Stamp images: ``/stamps/``
* Map tiles: ``/map_tiles/``

**Example Profile Image URL:**

.. code-block:: text

   https://dij5764lbzlpu.cloudfront.net/profile_images/images/5C616E89-7223-472E-8DD2-89A9F5FA45B6.jpeg

Error Responses
===============

Standard error response format:

.. code-block:: json

   {
     "error": {
       "code": "invalid_request",
       "message": "Invalid parameters provided",
       "details": {
         "field": "latitude",
         "reason": "must be a valid number"
       }
     }
   }

Common Error Codes:

:invalid_request: Malformed request
:unauthorized: Authentication required
:forbidden: Insufficient permissions
:not_found: Resource not found
:rate_limit_exceeded: Too many requests
:internal_error: Server error

Rate Limiting
=============

The API implements rate limiting:

* Standard users: 100 requests per minute
* Premium users: 500 requests per minute

Rate limit headers:

.. code-block:: http

   X-RateLimit-Limit: 100
   X-RateLimit-Remaining: 95
   X-RateLimit-Reset: 1644927600

Pagination
==========

Paginated endpoints follow this pattern:

.. code-block:: json

   {
     "items": [...],
     "page": 1,
     "per_page": 20,
     "total": 150,
     "next_page": "/api/resource?page=2"
   }

Best Practices
==============

.. tip::
   Always check API response status codes.

.. tip::
   Implement exponential backoff for retries.

.. tip::
   Use HTTPS for all API requests.

.. warning::
   Never hardcode authentication tokens in your application.
