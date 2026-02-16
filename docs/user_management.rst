===============
User Management
===============

This section covers all user-related API endpoints.

Update User Profile
===================

.. http:patch:: /api/user

   Update user profile with FCM token, location token, and permissions.

   **Request Headers:**

   .. code-block:: http

      Content-Type: multipart/form-data; boundary=1d4ad73e7633a936
      Authorization: Bearer <token>
      User-Agent: app.whoo/0.41.6 iOS/18.7

   **Request Body:**

   .. code-block:: text

      --boundary
      Content-Disposition: form-data; name="user[fcm_token]"

      f5uKXCePi0OBn5tFCGiyV8:APA91bFajXXZkP4qpu8YriYnhIs9mh9LG...
      --boundary
      Content-Disposition: form-data; name="user[location_token]"

      3a74399dd5579c51696aef1f823953b0be38dbe0692a60c5480132dffad0429f
      --boundary
      Content-Disposition: form-data; name="user[permission]"

      authorized
      --boundary--

   **Response:**

   :statuscode 200: User updated successfully

   .. code-block:: json

      {
        "user": {
          "id": 15617791,
          "uid": 26379416387,
          "username": "asahi0900",
          "display_name": "あさひ",
          "birthday": "2000-03-09",
          "profile_image": "https://dij5764lbzlpu.cloudfront.net/...",
          "online": false,
          "private_mode": false,
          "country_code": "JP",
          "login_days": 2,
          "whoo_supporter": false,
          "user_app_icons": [
            {
              "id": 58239521,
              "app_icon": {
                "id": 1,
                "icon_type": "donut"
              },
              "icon_state": "get"
            }
          ]
        }
      }

Update Online Status
====================

.. http:patch:: /api/user/online

   Update the user's online status.

   **Request Headers:**

   .. code-block:: http

      Accept: application/json
      Authorization: Bearer <token>
      Content-Length: 0

   **Response:**

   :statuscode 200: Status updated

   .. code-block:: json

      {
        "send_location_token": false,
        "confirm_alert": false,
        "is_whoo_supporter": false,
        "linq_ads_pages": []
      }

Update User Location
====================

.. http:patch:: /api/user/location

   Update the user's current location with device and battery info.

   **Request Headers:**

   .. code-block:: http

      Content-Type: application/json
      Authorization: Bearer <token>
      Upload-Complete: ?1

   **Request Body:**

   .. code-block:: json

      {
        "user_location": {
          "latitude": 34.73293285020455,
          "longitude": 137.37622463868036,
          "horizontal_accuracy": 10.867639445491365,
          "speed": 0,
          "stayed_at": "2026-02-15 09:41:07 +0000",
          "getting_location_type": 2
        },
        "user_device": {
          "os_info": "ios",
          "os_version": "18.7"
        },
        "user_battery": {
          "state": 1,
          "level": 0.4
        },
        "user_spot": {
          "id": 15509353
        },
        "app_state": {
          "active": true
        }
      }

   **Response:**

   :statuscode 200: Location updated

   .. code-block:: json

      {
        "u": false,
        "df": 1.0,
        "sdf": 1,
        "rdf": 1,
        "ed": 28
      }

   **Field Descriptions:**

   :user_location.latitude: Latitude coordinate
   :user_location.longitude: Longitude coordinate
   :user_location.horizontal_accuracy: GPS accuracy in meters
   :user_location.speed: Current speed in m/s
   :user_location.stayed_at: Timestamp when user arrived (ISO 8601)
   :user_location.getting_location_type: Location method (2=Network)
   :user_battery.level: Battery level (0.0-1.0)
   :user_battery.state: Battery state (1=charging)

Get User Notifications
=======================

.. http:get:: /api/user/notifications

   Retrieve user notifications.

   **Response:**

   :statuscode 304: Not Modified (cached)
   :statuscode 200: Notifications retrieved

Get User Spots
==============

.. http:get:: /api/user/spots

   Get a list of user's saved spots.

   **Response:**

   :statuscode 200: Spots retrieved
   :statuscode 304: Not Modified (cached)

Watch Log
=========

.. http:get:: /api/v2/watch_log

   Get user watch log with pagination.

   **Query Parameters:**

   :page: Page number (default: 1)

   **Example:**

   .. code-block:: http

      GET /api/v2/watch_log?page=1 HTTP/1.1

   **Response:**

   :statuscode 200: Watch log retrieved
   :statuscode 304: Not Modified (cached)

Sleep Time Friends
==================

.. http:get:: /api/sleep_time/friends

   Get friends' sleep time information.

   **Response:**

   :statuscode 200: Sleep time data retrieved

HTTP Caching
============

Most endpoints support ETags for bandwidth optimization:

.. code-block:: http

   GET /api/user/spots HTTP/1.1
   If-None-Match: W/"10988daed61d7560bf115dfcc9b0b8f4"

   Response:
   HTTP/1.1 304 Not Modified
