=====
Rooms
=====

Chat room and group conversation endpoints.

Get Unread Message Count
=========================

.. http:get:: /api/rooms/unread_message_count

   Get the count of unread messages across all rooms.

   **Request Headers:**

   .. code-block:: http

      Content-Type: application/json
      Authorization: Bearer <token>
      If-None-Match: W/"bc4afc8fc139c09611ab115cbdf43013"

   **Response:**

   :statuscode 200: Unread count retrieved
   :statuscode 304: Not Modified (cached)

   .. code-block:: json

      {
        "unread_count": 0
      }

Get Active Appointment Places
==============================

.. http:get:: /api/room/active_appointment_places

   Retrieve active appointment places for rooms.

   **Request Headers:**

   .. code-block:: http

      Content-Type: application/json
      Authorization: Bearer <token>

   **Response:**

   :statuscode 200: Appointment places retrieved
   :statuscode 304: Not Modified (cached)

   .. code-block:: json

      {
        "appointment_places": []
      }

   .. note::
      Appointment places are locations where room members plan to meet.

Room Types
==========

Whoo supports different room types:

1. **Direct Messages**: One-on-one conversations
2. **Group Rooms**: Multiple participants
3. **Appointment Rooms**: Location-based meetup planning

Room Features
=============

Rooms support:

* Real-time messaging via WebSocket
* Unread message tracking
* Location sharing and appointments
* Message history with pagination

Appointment System
==================

The appointment system allows users to:

1. Create meeting appointments
2. Set appointment locations
3. Track active appointments
4. Get notifications for upcoming meetings

**Appointment Place Structure:**

.. code-block:: json

   {
     "id": 12345,
     "name": "Starbucks Shibuya",
     "latitude": 35.6595,
     "longitude": 139.7004,
     "appointment_time": "2026-02-15T19:00:00+09:00",
     "participants": [
       {
         "user_id": 15617791,
         "status": "confirmed"
       }
     ]
   }

Best Practices
==============

.. tip::
   Poll unread count periodically or use WebSocket for real-time updates.

.. tip::
   Cache appointment places to reduce API calls.

.. note::
   Use ETags for efficient polling of unread messages.
