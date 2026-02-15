========
Location
========

Location and place-related API endpoints.

Get Nearby Places
=================

.. http:get:: /api/location/places/nearby

   Search for places near a specific location.

   **Query Parameters:**

   :latitude: Latitude coordinate (required)
   :longitude: Longitude coordinate (required)
   :radius_km: Search radius in kilometers (required)

   **Example Request:**

   .. code-block:: http

      GET /api/location/places/nearby?latitude=34.727398&longitude=137.386059&radius_km=8.806088268921473 HTTP/1.1
      Host: www.wh00.ooo
      Authorization: Bearer <token>
      Content-Type: application/json

   **Response:**

   :statuscode 200: Places found

   .. code-block:: json

      {
        "location_places": [],
        "next_page": null
      }

   **Field Descriptions:**

   :location_places: Array of nearby places
   :next_page: URL for pagination (null if no more results)

Complete Footprint Upload
==========================

.. http:post:: /api/footprint/upload_complete

   Mark a footprint upload as complete.

   **Request Headers:**

   .. code-block:: http

      Content-Type: application/json
      Authorization: Bearer <token>
      Content-Length: 0

   **Response:**

   :statuscode 204: Upload completed (No Content)

   .. note::
      This endpoint returns no body content on success.

Search Implementation
=====================

The location search uses a radius-based algorithm:

1. Client calculates current search radius
2. API returns places within that radius
3. Pagination available via ``next_page`` parameter

**Radius Calculation Example:**

.. code-block:: python

   import math

   def calculate_distance(lat1, lon1, lat2, lon2):
       R = 6371  # Earth radius in km
       dlat = math.radians(lat2 - lat1)
       dlon = math.radians(lon2 - lon1)
       a = (math.sin(dlat/2) ** 2 + 
            math.cos(math.radians(lat1)) * 
            math.cos(math.radians(lat2)) * 
            math.sin(dlon/2) ** 2)
       c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
       return R * c

Performance Tips
================

.. tip::
   Start with a smaller radius (< 10km) for faster responses.

.. tip::
   Cache location results to minimize API calls.
