=======
Friends
=======

Friend management and social features.

Get Friend Requests
===================

.. http:get:: /api/friends/requested

   Retrieve pending friend requests.

   **Request Headers:**

   .. code-block:: http

      Accept: application/json
      Authorization: Bearer <token>

   **Response:**

   :statuscode 200: Friend requests retrieved
   :statuscode 304: Not Modified (cached)

   .. code-block:: json

      {
        "friend_requests": []
      }

Get Best Friends
================

.. http:get:: /api/friends/best

   Get the user's best friends list.

   **Response:**

   :statuscode 200: Best friends retrieved

Get Friends Ranking
===================

.. http:get:: /api/v2/friends/ranking

   Get friends ranking data.

   **Query Parameters:**

   :page: Page number (default: 1)

   **Example:**

   .. code-block:: http

      GET /api/v2/friends/ranking?page=1 HTTP/1.1

   **Response:**

   :statuscode 200: Ranking data retrieved

Friend Spots
============

.. http:get:: /api/friends/spots

   Get spots visited by friends.

   **Response:**

   :statuscode 200: Friend spots retrieved

Get Following
=============

.. http:get:: /api/friends/following

   Get list of users you are following.

   **Response:**

   :statuscode 200: Following list retrieved
   :statuscode 304: Not Modified (cached)

Friend Management
=================

The friend system supports:

* Friend requests (pending approval)
* Best friends (special designation)
* Following/followers model
* Spot sharing between friends

Privacy Considerations
======================

.. warning::
   Friend data may include location information. Handle with care.

.. note::
   Use caching with ETags to optimize friend list requests.
